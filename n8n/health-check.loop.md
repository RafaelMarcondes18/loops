--- meta
name: n8n-health-check
description: Health check do servidor n8n no Hetzner — verifica disponibilidade e workflows ativos
project: n8n AI Stack
schedule: 11 9 * * 3
provider: anthropic
model: claude-haiku-4-5-20251001
tags: n8n, hetzner, infra, monitor, quarta
---

--- commands
health | py -c "import urllib.request; r=urllib.request.urlopen('http://{N8N_HOST}:5678/healthz', timeout=10); print('OK:', r.status)" | C:\Users\Rafael Marcondes
---

--- prompt
Voce e o monitor de infraestrutura do servidor n8n hospedado no Hetzner.

Resultado do health check:
{health}

---

Interprete o resultado e produza um relatorio curto:

N8N HEALTH — {data_hoje}
- Servidor: ONLINE / OFFLINE / TIMEOUT
- Status HTTP: [codigo ou erro]
- Acao recomendada: [nenhuma / restart / verificar manualmente]

Se OFFLINE:
  Instrucoes de recovery:
  1. Acesse o VPS Oracle (backup) ou Hetzner via SSH
  2. Execute: docker restart n8n  (ou o comando de restart configurado)
  3. Verifique logs: docker logs n8n --tail 50

Se ONLINE: "n8n: operacional. Nenhuma acao necessaria."

Maximo 12 linhas. Portugues brasileiro.

NOTA: Substitua {N8N_HOST} pelo IP real do servidor Hetzner em config.json antes de usar.
---
