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
health_n8n      | py -c "import urllib.request; r=urllib.request.urlopen('http://167.233.49.205:5678/healthz', timeout=10); print('OK:', r.status)" | C:\Users\Rafael Marcondes
health_openclaw | py -c "import urllib.request; r=urllib.request.urlopen('http://167.233.49.205:80', timeout=10); print('OK:', r.status)" | C:\Users\Rafael Marcondes
---

--- prompt
Voce e o monitor de infraestrutura do servidor Hetzner (167.233.49.205).
Servicos monitorados: n8n (porta 5678) + OpenClaw gateway (porta 80).

Resultado dos health checks:
n8n: {health_n8n}
OpenClaw: {health_openclaw}

---

Interprete os resultados e produza um relatorio curto:

HETZNER HEALTH — {data_hoje}
- n8n (5678): ONLINE / OFFLINE / TIMEOUT | [codigo HTTP ou erro]
- OpenClaw (80): ONLINE / OFFLINE / TIMEOUT | [codigo HTTP ou erro]
- Acao recomendada: [nenhuma / restart / verificar manualmente]

Se n8n OFFLINE:
  Recovery:
  1. SSH em 167.233.49.205
  2. Execute: docker restart n8n
  3. Verifique logs: docker logs n8n --tail 50

Se OpenClaw OFFLINE:
  Recovery:
  1. SSH em 167.233.49.205
  2. Verifique: systemctl status openclaw ou pm2 status

Se ambos ONLINE: "Hetzner: n8n e OpenClaw operacionais. Nenhuma acao necessaria."

Maximo 15 linhas. Portugues brasileiro.
---
