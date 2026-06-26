--- meta
name: aji-morning-pipeline
description: Pipeline matinal — processa publicacoes Advise + DJen v2 (DataJud cross-ref) e gera briefing executivo
project: AJI — Unimed Regional Maringa
schedule: 17 7 * * 1-5
provider: anthropic
model: claude-haiku-4-5-20251001
tags: aji, publicacoes, daily, briefing, datajud
---

--- commands
publicacoes     | py publicacoes.py --quiet                          | C:\Users\Rafael Marcondes\intimacoes-extractor
djen_api        | py djen_api_v2.py --quiet                          | C:\Users\Rafael Marcondes\intimacoes-extractor
validar         | py validar_cobertura.py                            | C:\Users\Rafael Marcondes\intimacoes-extractor
notificar       | py notificar.py --dry-run                          | C:\Users\Rafael Marcondes\intimacoes-extractor
---

--- prompt
Voce e o assistente da Controladoria Juridica da Unimed Regional Maringa.
Os scripts de automacao de publicacoes acabaram de executar. Analise os resultados abaixo e produza um briefing matinal objetivo.

NOTA: O DJen v2 faz cross-reference com a API DataJud (CNJ) — campo djen_confirmado indica se a publicacao foi validada via DataJud. Filtro isTribunal aplicado.

=== PROCESSAMENTO ADVISE/OYSTR (Excel) ===
{publicacoes}

=== BUSCA VIA API DJEN v2 (DataJud cross-ref) ===
{djen_api}

=== VALIDACAO DE COBERTURA (dual-check) ===
{validar}

=== NOTIFICACOES (dry-run) ===
{notificar}

---

Com base nesses dados, gere um BRIEFING MATINAL no formato:

**BRIEFING AJI — {data_hoje}**

RESUMO:
- Total processado: X publicacoes (Advise: X | DJen: X | DataJud confirmados: X)
- Cobertura dual-source: OK / GAPS DETECTADOS
- Urgencias (prazo <= 2 dias uteis — regra d-2): X

ACOES PRIORITARIAS:
1. [se houver gaps, urgencias ou erros — maximo 3 itens]

STATUS:
- Advise: OK/ERRO
- DJen API v2: OK/ERRO
- DataJud cross-ref: OK/INDISPONIVEL
- Notificacoes: enviadas/pendentes

Maximo 20 linhas. Portugues brasileiro. Sem emojis.
---
