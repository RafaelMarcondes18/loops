#!/usr/bin/env python3
"""
Universal Loop Runner — executa prompts pre-definidos via qualquer AI
Compativel com: Claude (Anthropic), OpenAI/Codex, Ollama, OpenRouter,
                Antigravity, qualquer API OpenAI-compatible

Uso:
  py runner.py aji/morning-pipeline.loop.md
  py runner.py aji/morning-pipeline.loop.md --provider openai --model gpt-4o
  py runner.py aji/morning-pipeline.loop.md --dry-run
"""
import sys
import os
import json
import argparse
import logging
import subprocess
import urllib.request
import urllib.error
from pathlib import Path
from datetime import datetime
import re

try:
    import anthropic as _anthropic_sdk
    HAS_ANTHROPIC = True
except ImportError:
    HAS_ANTHROPIC = False

try:
    import openai as _openai_sdk
    HAS_OPENAI = True
except ImportError:
    HAS_OPENAI = False

LOOPS_DIR = Path(__file__).parent
CONFIG_PATH = LOOPS_DIR / "config.json"
OUTPUT_DIR  = LOOPS_DIR / "output"
OUTPUT_DIR.mkdir(exist_ok=True)


# ── Config ────────────────────────────────────────────────────────────────────

def load_config() -> dict:
    if CONFIG_PATH.exists():
        return json.loads(CONFIG_PATH.read_text(encoding="utf-8"))
    return {}


# ── Loop file parser ──────────────────────────────────────────────────────────
#
# Formato do arquivo .loop.md:
#
#   --- meta
#   name: meu-loop
#   schedule: 17 7 * * 1-5
#   provider: anthropic
#   model: claude-haiku-4-5-20251001
#   description: O que este loop faz
#   ---
#
#   --- commands
#   label | comando | diretorio_de_trabalho
#   ---
#
#   --- prompt
#   Texto do prompt. Use {label} para injetar output dos comandos.
#   ---

def parse_section(content: str, tag: str) -> str:
    pattern = rf"---\s*{tag}\s*\n(.*?)\n---"
    match = re.search(pattern, content, re.DOTALL | re.IGNORECASE)
    return match.group(1).strip() if match else ""


def parse_meta(content: str) -> dict:
    meta = {}
    raw = parse_section(content, "meta")
    for line in raw.splitlines():
        if ":" in line:
            key, _, val = line.partition(":")
            meta[key.strip()] = val.strip()
    return meta


def parse_commands(content: str) -> list[dict]:
    commands = []
    raw = parse_section(content, "commands")
    for line in raw.splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        parts = [p.strip() for p in line.split("|")]
        if len(parts) >= 2:
            commands.append({
                "label": parts[0],
                "cmd":   parts[1],
                "cwd":   parts[2] if len(parts) > 2 else str(LOOPS_DIR),
            })
    return commands


def parse_prompt(content: str) -> str:
    return parse_section(content, "prompt")


def load_loop(path: Path) -> tuple[dict, list[dict], str]:
    text = path.read_text(encoding="utf-8")
    return parse_meta(text), parse_commands(text), parse_prompt(text)


# ── Pre-commands ──────────────────────────────────────────────────────────────

def run_commands(commands: list[dict], log: logging.Logger) -> dict[str, str]:
    outputs = {}
    for cmd_cfg in commands:
        label = cmd_cfg["label"]
        cmd   = cmd_cfg["cmd"]
        cwd   = cmd_cfg["cwd"]
        log.info(f"  [{label}] {cmd}")
        try:
            result = subprocess.run(
                cmd, shell=True, cwd=cwd,
                capture_output=True, text=True, timeout=120
            )
            out = (result.stdout + result.stderr).strip()
            outputs[label] = out or "(sem output)"
            if result.returncode != 0:
                outputs[label] = f"[EXIT {result.returncode}]\n{out}"
        except subprocess.TimeoutExpired:
            outputs[label] = "[TIMEOUT]"
        except Exception as e:
            outputs[label] = f"[ERRO] {e}"
    return outputs


# ── AI Providers ──────────────────────────────────────────────────────────────

def call_anthropic(prompt: str, model: str, config: dict) -> str:
    api_key = (config.get("anthropic_api_key") or
               os.environ.get("ANTHROPIC_API_KEY", ""))
    if not api_key:
        raise RuntimeError("ANTHROPIC_API_KEY nao configurada")

    if HAS_ANTHROPIC:
        client = _anthropic_sdk.Anthropic(api_key=api_key)
        msg = client.messages.create(
            model=model or "claude-sonnet-4-6",
            max_tokens=4096,
            messages=[{"role": "user", "content": prompt}]
        )
        return msg.content[0].text
    else:
        return _http_openai_compat(
            prompt, model or "claude-sonnet-4-6",
            base_url="https://api.anthropic.com/v1",
            api_key=api_key,
            extra_headers={"anthropic-version": "2023-06-01"}
        )


def call_openai(prompt: str, model: str, config: dict) -> str:
    api_key = (config.get("openai_api_key") or
               os.environ.get("OPENAI_API_KEY", ""))
    if not api_key:
        raise RuntimeError("OPENAI_API_KEY nao configurada")

    if HAS_OPENAI:
        client = _openai_sdk.OpenAI(api_key=api_key)
        resp = client.chat.completions.create(
            model=model or "gpt-4o",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=4096
        )
        return resp.choices[0].message.content
    else:
        return _http_openai_compat(
            prompt, model or "gpt-4o",
            base_url="https://api.openai.com/v1",
            api_key=api_key
        )


def call_ollama(prompt: str, model: str, config: dict) -> str:
    url = config.get("ollama_url", "http://localhost:11434") + "/api/generate"
    payload = json.dumps({
        "model": model or "llama3",
        "prompt": prompt,
        "stream": False
    }).encode("utf-8")
    req = urllib.request.Request(url, data=payload,
                                 headers={"Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=120) as r:
        return json.loads(r.read())["response"]


def call_generic(prompt: str, model: str, config: dict, provider: str) -> str:
    provider_cfg = config.get("providers", {}).get(provider, {})
    if not provider_cfg:
        raise RuntimeError(
            f"Provider '{provider}' nao encontrado em config.json. "
            f"Adicione uma entrada em 'providers'."
        )
    return _http_openai_compat(
        prompt,
        model or provider_cfg.get("default_model", "default"),
        base_url=provider_cfg["base_url"].rstrip("/"),
        api_key=provider_cfg.get("api_key", "")
    )


def _http_openai_compat(prompt: str, model: str, base_url: str,
                         api_key: str, extra_headers: dict | None = None) -> str:
    url = base_url + "/chat/completions"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}",
    }
    if extra_headers:
        headers.update(extra_headers)
    payload = json.dumps({
        "model": model,
        "messages": [{"role": "user", "content": prompt}],
        "max_tokens": 4096
    }).encode("utf-8")
    req = urllib.request.Request(url, data=payload, headers=headers)
    with urllib.request.urlopen(req, timeout=120) as r:
        return json.loads(r.read())["choices"][0]["message"]["content"]


PROVIDERS = {
    "anthropic": call_anthropic,
    "claude":    call_anthropic,
    "openai":    call_openai,
    "codex":     call_openai,
    "ollama":    call_ollama,
}


# ── Main ──────────────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(description="Universal Loop Runner")
    parser.add_argument("loop_file", help="Caminho para o arquivo .loop.md")
    parser.add_argument("--provider", help="Provider de AI (anthropic/openai/ollama/antigravity/...)")
    parser.add_argument("--model",    help="Modelo override")
    parser.add_argument("--dry-run",  action="store_true",
                        help="Mostra prompt sem chamar AI")
    args = parser.parse_args()

    loop_path = Path(args.loop_file)
    if not loop_path.is_absolute():
        loop_path = LOOPS_DIR / loop_path
    if not loop_path.exists():
        print(f"ERRO: arquivo nao encontrado: {loop_path}")
        sys.exit(1)

    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s  %(message)s",
        datefmt="%H:%M:%S"
    )
    log = logging.getLogger("runner")

    config   = load_config()
    meta, commands, prompt_template = load_loop(loop_path)

    loop_name = meta.get("name", loop_path.stem)
    provider  = args.provider or meta.get("provider") or config.get("default_provider", "anthropic")
    model     = args.model    or meta.get("model", "")

    log.info(f"Loop: {loop_name}")
    log.info(f"Provider: {provider} | Model: {model or 'default'}")

    # Rodar pre-commands e injetar outputs no prompt
    cmd_outputs = {}
    if commands:
        log.info("Executando comandos pre-loop...")
        cmd_outputs = run_commands(commands, log)

    prompt = prompt_template
    for label, output in cmd_outputs.items():
        prompt = prompt.replace(f"{{{label}}}", output)

    if args.dry_run:
        print("\n" + "="*60)
        print(f"DRY RUN — {loop_name}")
        print("="*60)
        print(f"Provider: {provider}  Model: {model or 'default'}\n")
        print("PROMPT:\n")
        print(prompt)
        print("="*60)
        return

    # Chamar AI
    log.info("Chamando AI...")
    try:
        if provider in PROVIDERS:
            result = PROVIDERS[provider](prompt, model, config)
        else:
            result = call_generic(prompt, model, config, provider)
    except Exception as e:
        log.error(f"FALHA ao chamar AI: {e}")
        ts = datetime.now().strftime("%Y-%m-%d_%H-%M")
        (OUTPUT_DIR / f"{ts}_{loop_name}.md").write_text(
            f"# {loop_name}\n**{ts}** | ERRO\n\n```\n{e}\n```\n",
            encoding="utf-8"
        )
        sys.exit(1)

    # Salvar resultado
    ts = datetime.now().strftime("%Y-%m-%d_%H-%M")
    out_path = OUTPUT_DIR / f"{ts}_{loop_name}.md"
    out_path.write_text(
        f"# {loop_name}\n**{ts}** | {provider} / {model or 'default'}\n\n---\n\n{result}\n",
        encoding="utf-8"
    )
    log.info(f"Salvo: {out_path}")
    print(result)


if __name__ == "__main__":
    main()
