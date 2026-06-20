--- meta
name: aji-morning-pipeline
description: Pipeline matinal — processa publicacoes Advise + DJen API e gera briefing executivo
project: AJI — Unimed Regional Maringa
schedule: 17 7 * * 1-5
provider: anthropic
model: claude-haiku-4-5-20251001
tags: aji, publicacoes, daily, briefing
---

--- commands
publicacoes     | py publicacoes.py --quiet                          | C:\Users\Rafael Marcondes\intimacoes-extractor
djen_api        | py djen_api.py --quiet                             | C:\Users\Rafael Marcondes\intimacoes-extractor
validar         | py validar_cobertura.py                            | C:\Users\Rafael Marcondes\intimacoes-extractor
notificar       | py notificar.py --dry-run                          | C:\Users\Rafael Marcondes\intimacoes-extractor
---

--- prompt
Voce e o assistente da Controladoria Juridica da Unimed Regional Maringa.
Os scripts de automacao de publicacoes acabaram de executar. Analise os resultados abaixo e produza um briefing matinal objetivo.

=== PROCESSAMENTO ADVISE/OYSTR (Excel) ===
{publicacoes}

=== BUSCA VIA API DJEN ===
{djen_api}

=== VALIDACAO DE COBERTURA (dual-check) ===
{validar}

=== NOTIFICACOES (dry-run) ===
{notificar}

---

Com base nesses dados, gere um BRIEFING MATINAL no formato:

**BRIEFING AJI — {data_hoje}**

RESUMO:
- Total processado: X publicacoes (Advise: X | DJen: X)
- Cobertura dual-source: OK / GAPS DETECTADOS
- Urgencias (prazo <= 2 dias uteis): X

ACOES PRIORITARIAS:
1. [se houver gaps, urgencias ou erros — maximo 3 itens]

STATUS:
- Advise: OK/ERRO
- DJen API: OK/ERRO
- Notificacoes: enviadas/pendentes

Maximo 20 linhas. Portugues brasileiro. Sem emojis.
---
