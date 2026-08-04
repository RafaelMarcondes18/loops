
## Security Review — Integração CHIA

**Action:** `anthropics/claude-code-security-review@main`
**Trigger:** Pull Request aberto ou atualizado
**Workflow:** `.github/workflows/security-review.yml`
**Modelo:** claude-haiku-4-5-20251001
**Foco:** agent loops — infinite loop, token budget, prompt injection, SSRF
**Instrução:** `.claude/security-scan-instructions.txt` (agent-scan)
**Exclusões FP:** `.claude/security-false-positives.txt`
**Secret necessário:** `ANTHROPIC_API_KEY` em Settings → Secrets → Actions