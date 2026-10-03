# POD contracts v1

- `pod.proto`: contratos de transporte e domínio para Project, Mission, Task, execução, nós, recursos, autorização, evidência, recovery, Git, artefatos, conhecimento, providers e braços lógicos.
- `mission_state.schema.json`: schema do estado persistente da missão de construção.
- `module_contract.schema.json`: contrato obrigatório de módulos conforme B4 da especificação consolidada.

Regra estrutural: conteúdo produzido, logs e evidências volumosas não são carregados no núcleo; contratos usam referências por hash/ponteiro.
