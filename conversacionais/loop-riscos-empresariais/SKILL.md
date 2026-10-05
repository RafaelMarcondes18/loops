---
name: loop-riscos-empresariais
description: Use para criar, revisar ou aprimorar plano de gestão de riscos, matriz ou registro de riscos de processos, projetos, áreas, decisões e operações, com controles, tratamento e sinais de alerta.
metadata:
  mode: conversational
  stages: "8"
---

# Gestão de Riscos Empresariais

## Execução

Leia [o roteiro completo](references/roteiro.md) ao iniciar. Execute as 8 etapas na ordem indicada, reaproveitando contexto, documentos e resultados anteriores. Os campos [INSIRA] e [COLE] são entradas do modelo original: use dados já disponíveis sem pedir ao usuário que os cole novamente.

Selecione este loop pelo objetivo do pedido; não exija seu nome nem comando especial. Informe brevemente o loop escolhido. Se o pedido for uma entrega pontual, use a skill especializada suficiente e não imponha o ciclo completo. Pedido de configurar ou explicar o loop não é pedido de executar uma análise real.

Avance nas etapas com evidência suficiente sem pedir autorização a cada etapa. Pergunte apenas o que falta e altera materialmente a entrega. Se uma dependência essencial estiver ausente, marque a etapa como pendente, avance só no trabalho independente e não apresente conclusão apoiada em dados inexistentes. Preserve as condições e validações humanas do roteiro.

Mantenha um registro compacto: etapa, situação (concluída, parcial, pendente ou não aplicável), evidência, resultado e próxima dependência. Ao retomar, use esse registro e os dados confirmados. Persista artefatos apenas no projeto correspondente quando a tarefa exigir, nunca dados de casos nos repositórios globais de skills. Não prometa memória entre conversas sem registro acessível.

Separe fatos, hipóteses e recomendações. Para fatos, indique documento, página, cláusula, linha ou registro quando disponível. Use {VARIÁVEL} para dado ausente. Responsáveis, metas e prazos propostos devem ser identificados como sugestões, sem inventar atribuições aprovadas. Em análise jurídica concreta, consulte fontes oficiais atuais e mantenha revisão profissional antes de assinatura ou protocolo.

Demandas da Unimed pertencem ao projeto controladoria-juridica; demandas do escritório, ao advocacia-marcondes. Confirme o contexto existente e respeite esse isolamento. O loop é uma sequência na conversa, não um serviço em execução: indicadores e frequências propostas não criam monitoramento, alertas, tarefas agendadas, chamadas pagas de API ou contatos com terceiros.

## Critérios específicos

Defina critérios qualitativos e evidências antes de classificar. Não use notas numéricas sem base. Controle descrito não comprova execução ou eficácia. Diferencie exposição antes dos controles e risco residual; sem evidência, indique que o residual não está validado. Aceitação do risco depende da alçada real.

## Etapas

1. Escopo do risco.
2. Identificação de riscos.
3. Avaliação de probabilidade e impacto.
4. Controles existentes.
5. Dependências e concentração.
6. Tratamento de riscos.
7. Indicadores e gatilhos.
8. Registro executivo de riscos.

## Skills de apoio

- `analista-de-processos-e-gargalos`: carregar a skill irmã `../analista-de-processos-e-gargalos/SKILL.md` apenas quando sua especialidade for necessária à etapa.
- `gerador-de-planos-de-acao`: carregar a skill irmã `../gerador-de-planos-de-acao/SKILL.md` apenas quando sua especialidade for necessária à etapa.
- `arquitetar-kpis-e-performance`: carregar a skill irmã `../arquitetar-kpis-e-performance/SKILL.md` apenas quando sua especialidade for necessária à etapa.

O roteiro contém o procedimento completo. Se uma skill de apoio não estiver instalada, siga o roteiro e informe apenas limitações relevantes. Não instale dependências ou delegue trabalho automaticamente.

## Conclusão e revisão

Consolide a entrega final prevista no roteiro, as fontes utilizadas, as decisões propostas, as pendências e os próximos passos. Considere concluído o ciclo somente quando as etapas aplicáveis tiverem entrega verificável; caso contrário, entregue resultado parcial identificado. Corrija inconsistências encontradas na revisão final e reveja as etapas afetadas. Se depender de nova evidência, registre a pendência e pare essa parte, sem repetir indefinidamente. Uma nova rodada exige novos dados, um marco de revisão definido ou pedido do usuário.
