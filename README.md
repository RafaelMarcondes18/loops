# Loops — Sistema de Prompts Autonomos

Executa prompts pre-definidos via qualquer AI (Claude, OpenAI/Codex, Ollama, Antigravity, OpenRouter) sem depender de sessao do Claude Code ativa.

## Estrutura

```
loops/
├── runner.py              # Runner universal — chama qualquer API AI
├── config.json            # API keys e providers (nao commitar com keys)
├── run-loop.bat           # Wrapper para Task Scheduler
├── install-scheduler.bat  # Registra todos os loops no Windows (executar como Admin)
│
├── aji/                   # AJI — Controladoria Juridica Unimed
│   ├── morning-pipeline.loop.md   # Seg-Sex 7:17h
│   ├── dual-check.loop.md         # Seg-Sex 11:23h
│   └── cpj-sync.loop.md           # Seg-Sex 8:45h
│
├── am/                    # Advocacia Marcondes
│   ├── weekly-report.loop.md      # Segundas 9:21h
│   └── projudi-monitor.loop.md    # Seg-Sex 10:43h
│
├── iudex/                 # Iudex SaaS
│   └── deploy-health.loop.md      # Seg-Sex 8:37h
│
├── seguranca/             # Auditoria de seguranca
│   └── security-review.loop.md    # Sextas 14:51h
│
├── n8n/                   # n8n Hetzner
│   └── health-check.loop.md       # Quartas 9:11h
│
└── output/                # Resultados de cada execucao (YYYY-MM-DD_HH-MM_nome.md)
```

## Formato dos arquivos .loop.md

```
--- meta
name: nome-do-loop
description: O que este loop faz
project: Nome do projeto
schedule: CRON_EXPRESSION   # 5 campos, hora local
provider: anthropic          # anthropic | openai | codex | ollama | antigravity | openrouter
model: claude-haiku-4-5-20251001
---

--- commands
label | comando shell | diretorio de trabalho
---

--- prompt
Texto do prompt. Use {label} para injetar output dos comandos.
---
```

## Instalacao

### 1. Configurar API keys

Edite `config.json` e preencha a key do provider que vai usar:
```json
{
  "default_provider": "anthropic",
  "anthropic_api_key": "sk-ant-...",
  ...
}
```

Ou via variavel de ambiente (mais seguro):
```
set ANTHROPIC_API_KEY=sk-ant-...
```

### 2. Instalar dependencias (opcional — fallback HTTP disponivel)

```
pip install anthropic openai
```

### 3. Registrar no Task Scheduler

Execute `install-scheduler.bat` como Administrador (uma unica vez).

## Uso manual

```bat
# Executar um loop agora
run-loop.bat aji\morning-pipeline.loop.md

# Testar sem chamar AI
run-loop.bat aji\morning-pipeline.loop.md --dry-run

# Usar provider diferente
run-loop.bat am\weekly-report.loop.md --provider openai --model gpt-4o
```

## Providers suportados

| Provider | Requer | Notas |
|---|---|---|
| `anthropic` / `claude` | ANTHROPIC_API_KEY | Padrao |
| `openai` / `codex` | OPENAI_API_KEY | |
| `ollama` | Servidor local | http://localhost:11434 |
| `antigravity` | config.json providers.antigravity | |
| `openrouter` | config.json providers.openrouter | Acesso a multiplos modelos |
| `groq` | config.json providers.groq | Rapido e barato |
| Qualquer OpenAI-compat | config.json providers.{nome} | Adicione base_url + api_key |

## Adicionar novo provider

Em `config.json`:
```json
"providers": {
  "meu-provider": {
    "base_url": "https://api.meu-provider.com/v1",
    "api_key": "...",
    "default_model": "modelo-padrao"
  }
}
```

Depois use: `run-loop.bat meu-loop.loop.md --provider meu-provider`
