---
name: loop-performance-fornecedores
description: Use para avaliar fornecedores, preparar QBR, criar scorecard, investigar baixa performance ou decidir entre desenvolver, manter e substituir um fornecedor.
metadata:
  mode: conversational
  stages: "7"
---

# Performance e Desenvolvimento de Fornecedores

## Execução

Leia [o roteiro completo](references/roteiro.md) ao iniciar. Execute as 7 etapas na ordem indicada, reaproveitando contexto, documentos e resultados anteriores. Os campos [INSIRA] e [COLE] são entradas do modelo original: use dados já disponíveis sem pedir ao usuário que os cole novamente.

Selecione este loop pelo objetivo do pedido; não exija seu nome nem comando especial. Informe brevemente o loop escolhido. Se o pedido for uma entrega pontual, use a skill especializada suficiente e não imponha o ciclo completo. Pedido de configurar ou explicar o loop não é pedido de executar uma análise real.

Avance nas etapas com evidência suficiente sem pedir autorização a cada etapa. Pergunte apenas o que falta e altera materialmente a entrega. Se uma dependência essencial estiver ausente, marque a etapa como pendente, avance só no trabalho independente e não apresente conclusão apoiada em dados inexistentes. Preserve as condições e validações humanas do roteiro.

Mantenha um registro compacto: etapa, situação (concluída, parcial, pendente ou não aplicável), evidência, resultado e próxima dependência. Ao retomar, use esse registro e os dados confirmados. Persista artefatos apenas no projeto correspondente quando a tarefa exigir, nunca dados de casos nos repositórios globais de skills. Não prometa memória entre conversas sem registro acessível.

Separe fatos, hipóteses e recomendações. Para fatos, indique documento, página, cláusula, linha ou registro quando disponível. Use {VARIÁVEL} para dado ausente. Responsáveis, metas e prazos propostos devem ser identificados como sugestões, sem inventar atribuições aprovadas. Em análise jurídica concreta, consulte fontes oficiais atuais e mantenha revisão profissional antes de assinatura ou protocolo.

Demandas da Unimed pertencem ao projeto controladoria-juridica; demandas do escritório, ao advocacia-marcondes. Confirme o contexto existente e respeite esse isolamento. O loop é uma sequência na conversa, não um serviço em execução: indicadores e frequências propostas não criam monitoramento, alertas, tarefas agendadas, chamadas pagas de API ou contatos com terceiros.

## Critérios específicos

Separe problemas sob controle do fornecedor daqueles causados ou compartilhados pelo comprador. Pesos e metas sugeridos são propostas. Não classifique performance sem dados; registre condições de continuidade e evidências para revisão.

## Etapas

1. Contexto e importância do fornecedor.
2. Scorecard de performance.
3. Diagnóstico de desvios.
4. Segmentação da relação.
5. Plano de desenvolvimento.
6. QBR e governança.
7. Decisão sobre continuidade.

## Skills de apoio

- `arquitetar-kpis-e-performance`: carregar a skill irmã `../arquitetar-kpis-e-performance/SKILL.md` apenas quando sua especialidade for necessária à etapa.
- `analista-de-processos-e-gargalos`: carregar a skill irmã `../analista-de-processos-e-gargalos/SKILL.md` apenas quando sua especialidade for necessária à etapa.
- `gerador-de-planos-de-acao`: carregar a skill irmã `../gerador-de-planos-de-acao/SKILL.md` apenas quando sua especialidade for necessária à etapa.

O roteiro contém o procedimento completo. Se uma skill de apoio não estiver instalada, siga o roteiro e informe apenas limitações relevantes. Não instale dependências ou delegue trabalho automaticamente.

## Conclusão e revisão

Consolide a entrega final prevista no roteiro, as fontes utilizadas, as decisões propostas, as pendências e os próximos passos. Considere concluído o ciclo somente quando as etapas aplicáveis tiverem entrega verificável; caso contrário, entregue resultado parcial identificado. Corrija inconsistências encontradas na revisão final e reveja as etapas afetadas. Se depender de nova evidência, registre a pendência e pare essa parte, sem repetir indefinidamente. Uma nova rodada exige novos dados, um marco de revisão definido ou pedido do usuário.
