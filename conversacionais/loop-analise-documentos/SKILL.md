---
name: loop-analise-documentos
description: Use para análise completa de documentos longos ou complexos, incluindo contexto, síntese, pontos críticos, riscos, perguntas, plano de ação e revisão final. Comparação é opcional quando houver múltiplos documentos.
metadata:
  mode: conversational
  stages: "10"
---

# Análise de Documentos

## Execução

Leia [o roteiro completo](references/roteiro.md) ao iniciar. Execute as 10 etapas na ordem indicada, reaproveitando contexto, documentos e resultados anteriores. Os campos [INSIRA] e [COLE] são entradas do modelo original: use dados já disponíveis sem pedir ao usuário que os cole novamente.

Selecione este loop pelo objetivo do pedido; não exija seu nome nem comando especial. Informe brevemente o loop escolhido. Se o pedido for uma entrega pontual, use a skill especializada suficiente e não imponha o ciclo completo. Pedido de configurar ou explicar o loop não é pedido de executar uma análise real.

Avance nas etapas com evidência suficiente sem pedir autorização a cada etapa. Pergunte apenas o que falta e altera materialmente a entrega. Se uma dependência essencial estiver ausente, marque a etapa como pendente, avance só no trabalho independente e não apresente conclusão apoiada em dados inexistentes. Preserve as condições e validações humanas do roteiro.

Mantenha um registro compacto: etapa, situação (concluída, parcial, pendente ou não aplicável), evidência, resultado e próxima dependência. Ao retomar, use esse registro e os dados confirmados. Persista artefatos apenas no projeto correspondente quando a tarefa exigir, nunca dados de casos nos repositórios globais de skills. Não prometa memória entre conversas sem registro acessível.

Separe fatos, hipóteses e recomendações. Para fatos, indique documento, página, cláusula, linha ou registro quando disponível. Use {VARIÁVEL} para dado ausente. Responsáveis, metas e prazos propostos devem ser identificados como sugestões, sem inventar atribuições aprovadas. Em análise jurídica concreta, consulte fontes oficiais atuais e mantenha revisão profissional antes de assinatura ou protocolo.

Demandas da Unimed pertencem ao projeto controladoria-juridica; demandas do escritório, ao advocacia-marcondes. Confirme o contexto existente e respeite esse isolamento. O loop é uma sequência na conversa, não um serviço em execução: indicadores e frequências propostas não criam monitoramento, alertas, tarefas agendadas, chamadas pagas de API ou contatos com terceiros.

## Critérios específicos

Na etapa 8, compare apenas se houver dois ou mais documentos ou versões e pertinência ao pedido. Com documento único, registre não aplicável e prossiga à etapa 9. Diferencie leitura integral de análise de trechos. Preserve ressalvas e localização das evidências; preparar comunicação não autoriza envio.

## Etapas

1. Contexto do documento.
2. Resumo estruturado.
3. Pontos críticos.
4. Riscos e implicações.
5. Perguntas e dúvidas.
6. Síntese executiva.
7. Plano de ação.
8. Comparação entre documentos.
9. Resumo para comunicação.
10. Checklist final da análise.

## Skills de apoio

- `sintetizador-de-relatorios-extensos`: carregar a skill irmã `../sintetizador-de-relatorios-extensos/SKILL.md` apenas quando sua especialidade for necessária à etapa.
- `analista-comparativo-de-documentos`: carregar a skill irmã `../analista-comparativo-de-documentos/SKILL.md` apenas quando sua especialidade for necessária à etapa.
- `gerador-de-planos-de-acao`: carregar a skill irmã `../gerador-de-planos-de-acao/SKILL.md` apenas quando sua especialidade for necessária à etapa.
- `editor-executivo-de-textos`: carregar a skill irmã `../editor-executivo-de-textos/SKILL.md` apenas quando sua especialidade for necessária à etapa.

O roteiro contém o procedimento completo. Se uma skill de apoio não estiver instalada, siga o roteiro e informe apenas limitações relevantes. Não instale dependências ou delegue trabalho automaticamente.

## Conclusão e revisão

Consolide a entrega final prevista no roteiro, as fontes utilizadas, as decisões propostas, as pendências e os próximos passos. Considere concluído o ciclo somente quando as etapas aplicáveis tiverem entrega verificável; caso contrário, entregue resultado parcial identificado. Corrija inconsistências encontradas na revisão final e reveja as etapas afetadas. Se depender de nova evidência, registre a pendência e pare essa parte, sem repetir indefinidamente. Uma nova rodada exige novos dados, um marco de revisão definido ou pedido do usuário.
