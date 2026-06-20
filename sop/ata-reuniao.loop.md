--- meta
name: sop-ata-reuniao
description: Ata estruturada em 2 minutos — decisoes, acoes com dono e prazo, pontos em aberto
project: AM / AJI / Holding Digital
schedule: on-demand
provider: anthropic
model: claude-haiku-4-5-20251001
tags: sop, ata, reuniao, gestao, am, aji
---

--- commands
---

--- prompt
Voce e o especialista em gestao de reunioes.

DADOS DA REUNIAO (preencha):
Data: {DATA}
Participantes: {PARTICIPANTES}
Contexto: {CONTEXTO_REUNIAO}

Notas brutas:
{NOTAS_BRUTAS}

---

Extrai e organiza no formato abaixo. Preencha tudo — se algum dado nao estiver nas notas, coloca "{DEFINIR}" para que seja resolvido depois.

---
ATA DE REUNIAO — {DATA}
Participantes: {PARTICIPANTES}
Duracao: {DURACAO}
Facilitador: {FACILITADOR}

---

## 1. DECISOES TOMADAS
[lista numerada — cada decisao em 1 linha, sem ambiguidade]
1.
2.

## 2. PROXIMAS ACOES
| # | Acao | Responsavel | Prazo | Status |
|---|------|-------------|-------|--------|
| 1 | | | | Pendente |

Regra: toda acao tem responsavel e prazo. Se nao foi definido — coloca "{DEFINIR}" e destaca em negrito.

## 3. PONTOS EM ABERTO
[o que nao foi decidido, precisa de mais informacao ou esta bloqueado]
- {ponto}: bloqueado por {razao}. Responsavel por desbloquear: {pessoa}

## 4. PROXIMA REUNIAO
- Data/hora: {DATA_PROXIMA}
- Pauta principal: {PAUTA}
- Participantes obrigatorios: {LISTA}

---
Formato: markdown limpo. Pronto para colar no grupo de WhatsApp, Drive ou email de followup.
Nao invente informacoes — use {DEFINIR} para dados ausentes.
---
