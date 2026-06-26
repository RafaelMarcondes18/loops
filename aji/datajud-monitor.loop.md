--- meta
name: aji-datajud-monitor
description: Monitor DataJud CNJ — jurimetria diaria dos 16 processos AM ativos com alertas de prazo
project: AJI — Unimed Regional Maringa
schedule: 15 8 * * 1-5
provider: anthropic
model: claude-haiku-4-5-20251001
tags: aji, datajud, cnj, jurimetria, monitor, daily
---

--- commands
datajud | py datajud_monitor.py --quiet | C:\Users\Rafael Marcondes\intimacoes-extractor
---

--- prompt
Voce e o monitor de jurimetria da Advocacia Marcondes via API DataJud CNJ.
16 processos AM monitorados diariamente. API key configurada — TJPR confirmado OK.

Resultado do monitor DataJud:
{datajud}

---

Produza um RELATORIO DE JURIMETRIA no formato:

DATAJUD MONITOR — {data_hoje}
- Processos consultados: X / 16
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
