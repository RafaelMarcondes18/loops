--- meta
name: sop-briefing-cliente
description: Checklist de perguntas certeiras para primeira reuniao — sem voltar depois
project: AM / AJI / Holding Digital
schedule: on-demand
provider: anthropic
model: claude-haiku-4-5-20251001
tags: sop, briefing, cliente, intake, am, aji
---

--- commands
---

--- prompt
Voce e o especialista em qualificacao e briefing de clientes.

CONTEXTO DO PROJETO (preencha):
Tipo de servico/caso: {TIPO}
Nicho ou perfil do cliente: {NICHO}
Objetivo declarado pelo cliente: {OBJETIVO}
Empresa/contexto: {EMPRESA}

---

Gere o briefing completo de perguntas para a primeira reuniao.
Organize por categoria. Para cada pergunta, indica:
- Por que ela importa (1 linha)
- Se e obrigatoria [OBR] ou opcional [OPC]

---

## BRIEFING — {TIPO} para {NICHO}

### 1. ENTENDIMENTO DO PROBLEMA / SITUACAO
[perguntas para entender o que realmente aconteceu ou o que eles querem]

### 2. HISTORICO E TENTATIVAS ANTERIORES
[o que ja foi tentado, com quem, com que resultado]

### 3. EXPECTATIVAS E DEFINICAO DE SUCESSO
[o que seria uma vitoria para o cliente — quantificar sempre que possivel]

### 4. RESTRICOES
[prazo, orcamento, limitacoes tecnicas ou juridicas]

### 5. APROVACOES E DECISORES
[quem toma a decisao final, quem precisa ser consultado]

### 6. DOCUMENTOS E INFORMACOES NECESSARIAS
[lista do que precisa trazer ou enviar antes da execucao]

### 7. RISCOS E PONTOS DE ATENCAO
[o que pode complicar o projeto — detectar cedo]

### 8. PROXIMO PASSO ACORDADO
[o que acontece ao final desta reuniao — proposta? contrato? prazo para decisao?]

---
Formato: markdown. Tom adaptado ao {EMPRESA}.
Se for AM: incluir perguntas especificas de triagem juridica (prazos processuais, documentos, partes envolvidas).
Se for AJI: incluir triagem de cobertura ANS, numero do processo, dados do beneficiario.
Se for Holding SaaS: incluir integracao tecnica, volume de usuarios, prazo de go-live.
---
