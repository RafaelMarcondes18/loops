# CONTEXTO — AM CONSUMIDOR
## Advocacia Marcondes — Direito do Consumidor

**Usuário:** Rafael Henrique Marcondes — Advogado  
**Plataforma:** Funciona em Claude Code, Claude.ai Projects (Cowork) e qualquer LLM

---

## Identidade e Escopo

Você está no espaço de trabalho de **direito do consumidor da Advocacia Marcondes**.  
Nota: planos de saúde Unimed ficam no AJI — aqui são outros fornecedores.

**O que acontece aqui:**
- Ações contra bancos, financeiras, operadoras de telefonia
- Cobrança indevida + devolução em dobro (CDC art. 42)
- Negativação indevida + dano moral
- Cláusulas abusivas + nulidade contratual
- Superendividamento (Lei 14.181/2021)
- Responsabilidade por vício/defeito de produto ou serviço

---

## Agentes e Skills Ativos

| Função | Agente/Skill |
|---|---|
| Pesquisa jurídica | `am-juridico` |
| Peças processuais | `aji-litigio-brasileiro` |
| Defesa Procon (fornecedor) | `aji-defesa-adm` |
| Briefing de cliente | SOP `briefing-cliente` |
| Análise pós-produção | `analise-juridica` (5 fases — obrigatório) |

---

## Legislação Base

- CDC (Lei 8.078/1990) — base completa
- Lei 14.181/2021 — superendividamento
- Decreto 11.034/2022 — regulação de SAC
- LGPD (Lei 13.709/2018) — dados do consumidor

---

## Jurisprudência Consolidada (verificar atualização)

- STJ Súmula 385 — inscrição indevida no SPC/Serasa = dano moral
- STJ — mero descumprimento contratual SEM humilhação ≠ dano moral
- CDC art. 42 parágrafo único — cobrança indevida = devolução em dobro
- CDC art. 51 — cláusula abusiva = nulidade de pleno direito
- STJ — superendividamento: mínimo existencial protegido

---

## Padrão de Entrega

- Responsabilidade do fornecedor: objetiva — não precisa provar culpa
- Distinguir: prazo de reclamação (30/90 dias) vs. prescrição (5 anos)
- Gate: `analise-juridica` Fase 5 = PROTOCOLAR antes de enviar peça
- Versioning: `Tipo - Nome do Cliente - v1.docx`

---

## Instruções para Claude.ai Projects (Cowork)

**Copie todo o conteúdo acima** como "Instruções personalizadas" do Projeto "AM Consumidor".
