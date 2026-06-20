--- meta
name: aji-cpj-sync
description: Sincronizacao com CPJ-3C — registra novos processos extraidos no sistema
project: AJI — Unimed Regional Maringa
schedule: 45 8 * * 1-5
provider: anthropic
model: claude-haiku-4-5-20251001
tags: aji, cpj, sync, daily
---

--- commands
cpj_sync | py cpj_sync.py | C:\Users\Rafael Marcondes\intimacoes-extractor
---

--- prompt
Voce e o assistente da Controladoria Juridica da Unimed Regional Maringa.

O script de sincronizacao com o CPJ-3C acabou de executar:

=== OUTPUT CPJ SYNC ===
{cpj_sync}

---

Produza um relatorio de sincronizacao:

SINCRONIZACAO CPJ — {data_hoje}
- Registros enviados ao CPJ: X
- Erros de conexao/SQL: X (se houver, liste)
- Processos duplicados ignorados: X
- Status: SUCESSO / FALHA PARCIAL / FALHA TOTAL

Se FALHA: indique se e necessaria intervencao humana imediata.
Maximo 10 linhas. Portugues brasileiro.
---
