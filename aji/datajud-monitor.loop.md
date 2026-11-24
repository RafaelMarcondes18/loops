--- meta
name: aji-datajud-monitor
description: Monitor DataJud CNJ — movimentacoes diarias dos processos da lista config.json com alertas de prazo d-2
project: AJI — Unimed Regional Maringa
schedule: 15 8 * * 1-5
provider: anthropic
model: claude-haiku-4-5-20251001
tags: aji, datajud, cnj, jurimetria, monitor, daily
---

--- commands
datajud | py datajud_monitor.py --quiet | C:\Users\1217\Quadrados\controladoria-juridica\automacoes\intimacoes-extractor
---

--- prompt
Voce e o monitor DataJud da Controladoria Juridica da Unimed Regional Maringa.
Os processos monitorados sao os da lista config.json do intimacoes-extractor. Nao trate processos da Advocacia Marcondes neste quadrado.

Resultado do monitor DataJud:
{datajud}

---

Produza um RELATORIO DE JURIMETRIA no formato:

DATAJUD MONITOR — {data_hoje}
- Processos consultados: X (total da lista)
- Novas movimentacoes: X
- Prazos criticos (d-2 ou menos): X

URGENCIAS (d-2):
[lista com numero do processo | movimento | prazo fatal | dias restantes]

MOVIMENTACOES DO DIA:
[numero | tribunal | tipo de movimento | data]

STATUS API:
- DataJud TJPR: OK/ERRO
- Supabase sync: OK/ERRO
- Telegram: notificado/pendente

Se sem movimentacoes novas: "DataJud: sem novas movimentacoes hoje."

Maximo 25 linhas. Portugues brasileiro. Sem emojis.
---
