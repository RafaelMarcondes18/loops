---
name: loop-melhoria-processos
description: Use para mapear e melhorar um processo de ponta a ponta, investigar gargalos e retrabalho, redesenhar responsabilidades e preparar transição antes de automatizar.
metadata:
  mode: conversational
  stages: "12"
---

# Mapeamento e Melhoria de Processos

## Execução

Leia [o roteiro completo](references/roteiro.md) ao iniciar. Execute as 12 etapas na ordem indicada, reaproveitando contexto, documentos e resultados anteriores. Os campos [INSIRA] e [COLE] são entradas do modelo original: use dados já disponíveis sem pedir ao usuário que os cole novamente.

Selecione este loop pelo objetivo do pedido; não exija seu nome nem comando especial. Informe brevemente o loop escolhido. Se o pedido for uma entrega pontual, use a skill especializada suficiente e não imponha o ciclo completo. Pedido de configurar ou explicar o loop não é pedido de executar uma análise real.

Avance nas etapas com evidência suficiente sem pedir autorização a cada etapa. Pergunte apenas o que falta e altera materialmente a entrega. Se uma dependência essencial estiver ausente, marque a etapa como pendente, avance só no trabalho independente e não apresente conclusão apoiada em dados inexistentes. Preserve as condições e validações humanas do roteiro.

Mantenha um registro compacto: etapa, situação (concluída, parcial, pendente ou não aplicável), evidência, resultado e próxima dependência. Ao retomar, use esse registro e os dados confirmados. Persista artefatos apenas no projeto correspondente quando a tarefa exigir, nunca dados de casos nos repositórios globais de skills. Não prometa memória entre conversas sem registro acessível.

Separe fatos, hipóteses e recomendações. Para fatos, indique documento, página, cláusula, linha ou registro quando disponível. Use {VARIÁVEL} para dado ausente. Responsáveis, metas e prazos propostos devem ser identificados como sugestões, sem inventar atribuições aprovadas. Em análise jurídica concreta, consulte fontes oficiais atuais e mantenha revisão profissional antes de assinatura ou protocolo.

Demandas da Unimed pertencem ao projeto controladoria-juridica; demandas do escritório, ao advocacia-marcondes. Confirme o contexto existente e respeite esse isolamento. O loop é uma sequência na conversa, não um serviço em execução: indicadores e frequências propostas não criam monitoramento, alertas, tarefas agendadas, chamadas pagas de API ou contatos com terceiros.

## Critérios específicos

Preserve a sequência AS IS, fatos e métricas, gargalos, causas, riscos e controles, priorização, TO BE, governança, indicadores, piloto e revisão. Não pule o diagnóstico para recomendar tecnologia. Não remova controle apenas por gerar demora. Um fluxo futuro é proposta até sua validação operacional.

## Etapas

1. Clareza do processo e do resultado esperado.
2. Mapeamento do processo atual.
3. Validação com fatos e métricas.
4. Gargalos, desperdícios e pontos de fricção.
5. Análise de causas raiz.
6. Riscos, controles e dependências.
7. Priorização das oportunidades de melhoria.
8. Desenho do processo futuro.
9. Papéis, responsabilidades e governança.
10. Indicadores e pontos de controle.
11. Plano de transição e teste.
12. Validação crítica e dossiê executivo.

## Skills de apoio

- `analista-de-processos-e-gargalos`: carregar a skill irmã `../analista-de-processos-e-gargalos/SKILL.md` apenas quando sua especialidade for necessária à etapa.
- `criador-de-manuais-profissionais`: carregar a skill irmã `../criador-de-manuais-profissionais/SKILL.md` apenas quando sua especialidade for necessária à etapa.
- `arquitetar-kpis-e-performance`: carregar a skill irmã `../arquitetar-kpis-e-performance/SKILL.md` apenas quando sua especialidade for necessária à etapa.
- `gerador-de-planos-de-acao`: carregar a skill irmã `../gerador-de-planos-de-acao/SKILL.md` apenas quando sua especialidade for necessária à etapa.

O roteiro contém o procedimento completo. Se uma skill de apoio não estiver instalada, siga o roteiro e informe apenas limitações relevantes. Não instale dependências ou delegue trabalho automaticamente.

## Conclusão e revisão

Consolide a entrega final prevista no roteiro, as fontes utilizadas, as decisões propostas, as pendências e os próximos passos. Considere concluído o ciclo somente quando as etapas aplicáveis tiverem entrega verificável; caso contrário, entregue resultado parcial identificado. Corrija inconsistências encontradas na revisão final e reveja as etapas afetadas. Se depender de nova evidência, registre a pendência e pare essa parte, sem repetir indefinidamente. Uma nova rodada exige novos dados, um marco de revisão definido ou pedido do usuário.
