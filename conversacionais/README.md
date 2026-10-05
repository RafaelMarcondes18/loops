# Loops conversacionais de gestão

Sete roteiros fornecidos por Rafael, com 60 etapas. O assistente seleciona o loop pelo objetivo da atividade e executa as etapas na conversa, reutilizando resultados anteriores. Dados ausentes geram pendências explícitas. Os prompts originais estão nas referências de cada skill.

| Loop | Etapas | Invocação explícita no Codex |
|---|---:|---|
| [Gestão de Contratos e Renovação em Procurement](loop-contratos-renovacao/SKILL.md) | 7 | `$loop-contratos-renovacao` |
| [Performance e Desenvolvimento de Fornecedores](loop-performance-fornecedores/SKILL.md) | 7 | `$loop-performance-fornecedores` |
| [Gestão de Stakeholders](loop-gestao-stakeholders/SKILL.md) | 8 | `$loop-gestao-stakeholders` |
| [Gestão de Riscos Empresariais](loop-riscos-empresariais/SKILL.md) | 8 | `$loop-riscos-empresariais` |
| [Análise de Indicadores e Performance](loop-indicadores-performance/SKILL.md) | 8 | `$loop-indicadores-performance` |
| [Mapeamento e Melhoria de Processos](loop-melhoria-processos/SKILL.md) | 12 | `$loop-melhoria-processos` |
| [Análise de Documentos](loop-analise-documentos/SKILL.md) | 10 | `$loop-analise-documentos` |

## Uso e sincronização

Exemplos: “Prepare a renovação deste contrato”, “Crie um plano de riscos para este processo” ou “Mapeie e melhore este fluxo”. Não é necessário citar o nome da skill.

As mesmas skills estão publicadas em `RafaelMarcondes18/claude-config`, pasta `skills/`, e `RafaelMarcondes18/codex-config`, pasta `skills/`. A máquina residencial deve atualizar os dois repositórios pelo mecanismo de sincronização já configurado. Se houver alterações locais, confira-as antes de atualizar; não force sobrescrita. A recepção depende de a máquina estar conectada e executar a sincronização.

Esta pasta contém a biblioteca de referência dos loops. Ela não utiliza `runner.py`, não deve ser passada ao runner como arquivo `.loop.md` e não registra agendamento nem chama APIs pagas. A conclusão de uma etapa é uma entrega analítica, não prova de execução operacional de uma ação recomendada.

Os arquivos `agents/openai.yaml` permitem seleção implícita no Codex. As skills de apoio são opcionais e estão disponíveis nos repositórios de configuração; o roteiro é autossuficiente para consulta nesta biblioteca. Mantenha as três cópias iguais ao revisar. Dados de clientes e resultados das execuções ficam nos projetos isolados, nunca nesta biblioteca genérica.
