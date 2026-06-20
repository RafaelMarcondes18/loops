--- meta
name: security-review-intimacoes
description: Revisao semanal do plano de seguranca do intimacoes-extractor — rastreia itens pendentes
project: intimacoes-extractor
schedule: 51 14 * * 5
provider: anthropic
model: claude-sonnet-4-6
tags: seguranca, auditoria, semanal, sexta
---

--- commands
plano     | type "C:\Users\Rafael Marcondes\.claude\plans\curried-squishing-naur.md" | C:\Users\Rafael Marcondes
extractor | type "C:\Users\Rafael Marcondes\intimacoes-extractor\extractor.py"        | C:\Users\Rafael Marcondes
config    | type "C:\Users\Rafael Marcondes\intimacoes-extractor\configurar.py"       | C:\Users\Rafael Marcondes
cpj_sync  | type "C:\Users\Rafael Marcondes\intimacoes-extractor\cpj_sync.py"         | C:\Users\Rafael Marcondes
notificar | type "C:\Users\Rafael Marcondes\intimacoes-extractor\notificar.py"        | C:\Users\Rafael Marcondes
---

--- prompt
Voce e o auditor de segurança do projeto intimacoes-extractor da Unimed Regional Maringa.

PLANO DE SEGURANÇA (referencia):
{plano}

CODIGO ATUAL:

extractor.py:
{extractor}

configurar.py:
{config}

cpj_sync.py:
{cpj_sync}

notificar.py:
{notificar}

---

Com base no plano e no codigo atual, verifique o status de cada item:

| Severidade | Item | Status | Evidencia no codigo |
|---|---|---|---|
| ALTA | keyring para senha SQL | FEITO / PENDENTE | [trecho relevante ou ausencia] |
| ALTA | Flag LGPD + guard Gemini | FEITO / PENDENTE | |
| MEDIA | Audit log (audit_logger.py) | FEITO / PENDENTE | |
| MEDIA | Path traversal check | FEITO / PENDENTE | |
| BAIXA | Timeout COM Outlook | FEITO / PENDENTE | |
| BAIXA | requirements.txt fixado | FEITO / PENDENTE | |

RESUMO:
- Itens ALTA pendentes: X
- Itens MEDIA pendentes: X
- Proxima acao recomendada: [especifica]

Se todos os itens ALTA estiverem implementados, diga "ALTAS CONCLUIDAS — este loop pode ser desativado."
Portugues brasileiro.
---
