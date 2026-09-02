# POD — ARQUITETURA TÉCNICA LÓGICA — V002

**Identificador:** POD-DOC-005
**Versão:** 2.0.0
**Status:** ACTIVE
**Data:** 2026-09-02
**Conjunto:** POD-DOCSET-V003
**Autoridade:** A2 — arquitetura técnica
**Substitui:** arquitetura derivada V001 e topologias fixas anteriores

## 1. Objetivo

Definir fronteiras, responsabilidades, fluxos e dependências sem escolher stack física ou quantidade fixa de processos.

## 2. Forma arquitetural

O POD adota monólito modular local-first como ponto de partida físico recomendado, preservando portas que permitem extrair processos quando testes demonstrarem necessidade.

Isso evita transformar cada componente lógico em serviço prematuramente.

## 3. Camadas

### Domain

Contém entidades, valores, estados, transições, invariantes e políticas puras. Não importa banco, rede, UI, modelo ou sistema operacional.

### Application

Contém casos de uso, Mission Core, orquestração, autorização e portas.

### Adapters

Traduz banco, mensageria, provedores, sistema operacional, MCP, API e UI para contratos internos.

### Runtime

Composição, processos, configuração, observabilidade, supervisão e lifecycle.

Regra:

~~~text
DOMAIN → nenhuma camada externa
APPLICATION → DOMAIN
ADAPTERS → APPLICATION + DOMAIN
RUNTIME → composição das anteriores
~~~

## 4. Planos lógicos

### Control Plane

- Command Ingress;
- Admission;
- Mission Core;
- Brain;
- Construction Engineering;
- Governor;
- Scheduler;
- Policy.

### Data Plane

- Engine;
- Worker Runtime;
- Artifact Handling;
- Delivery.

### Memory Plane

- Authoritative Transaction Store;
- Domain Event Journal;
- Outbox/Inbox;
- Evidence Store;
- Checkpoint Store;
- Knowledge Store;
- Read Models.

### Security Plane

- Identity;
- Authentication;
- Authorization;
- Capability;
- Vault Port;
- Audit;
- Immune System;
- Incident Handling.

### Federation Plane

- Node Registry;
- Enrollment;
- Compatibility;
- Lease Authority;
- Dispatch;
- Reconciliation.

### Experience Plane

- Panel;
- Launcher;
- Terminal;
- API;
- Notifications.

Planos são responsabilidades. Não exigem processos separados.

## 5. Componentes e propriedade

| Componente | Entrada | Saída | Autoridade |
|---|---|---|---|
| Command Ingress | comando autenticado | command_id e ACK persistido | nenhuma decisão de produto |
| Admission | contrato de missão | accepted ou rejection | aceitar somente por regras |
| Mission Core | comando/verdict/evento | novo estado atômico | estado da missão |
| Brain | objetivo/contexto/evidência | estratégia e plano candidato | estratégia |
| Construction Engineering | estratégia | WorkUnits e artefatos candidatos | procedimento técnico |
| Governor | demanda e recursos | quotas e prioridade | recursos |
| Scheduler | WorkUnits autorizadas | dispatch | tempo e destino permitidos |
| Engine | envelope | fatos, efeitos e evidências | execução física limitada |
| Proof Engine | critérios e Evidence Pack | ProofVerdict | avaliação de prova |
| Memory | transação | estado/história/outbox | durabilidade |
| Security | identity/scope/action | allow, deny ou require_gate | autorização |
| Federation | WorkUnit e nós | rota/lease/reconcile | roteamento |
| Panel/API | leitura e intenção | projeção/comando | nenhuma mutação direta |

## 6. Fluxo de comando

~~~text
CLIENT
→ AUTHENTICATE
→ COMMAND INGRESS
→ IDEMPOTENCY CHECK
→ POLICY / CAPABILITY
→ ATOMIC COMMAND ACCEPTANCE
→ ACK
→ APPLICATION HANDLER
~~~

ACK confirma aceitação durável, não execução ou resultado.

## 7. Fluxo de mutação

~~~text
LOAD aggregate version
→ VALIDATE command, policy, generation and guards
→ BEGIN local transaction
→ UPDATE aggregate with compare-and-set version
→ APPEND domain event
→ INSERT outbox
→ INSERT idempotency/audit record
→ COMMIT
→ relay outbox at-least-once
→ CONFIRM
~~~

Compare-and-set significa gravar somente se a versão ainda for a esperada.

### Autoridade dos dados

- estado corrente da entidade: linha versionada do aggregate;
- história causal: journal append-only na mesma transação;
- entrega assíncrona: outbox;
- consulta: Read Model reconstruível;
- arquivo grande: Artifact/Evidence Store referenciado por hash;
- barramento: transporte, nunca fonte de verdade.

Se aggregate e journal divergirem, o POD abre incidente de integridade e bloqueia mutações no escopo afetado até reconciliação.

## 8. Fluxo da prova

~~~text
MISSION CORE requests proof evaluation
→ PROOF ENGINE loads exact criteria and policy versions
→ validates Evidence Manifest and mandatory gates
→ emits immutable ProofVerdict
→ MISSION CORE reloads mission version
→ validates verdict freshness and guards
→ atomically records verdict consumption and MISSION_PROVEN
~~~

O ProofVerdict é consumível uma vez para mission_version exata. Alteração posterior da missão invalida verdict anterior.

## 9. Máquina de estados

A tabela normativa está em POD-DOC-006. Toda transição:

- possui comando ou evento causador;
- possui ator;
- possui guardas;
- gera evento;
- incrementa versão;
- é idempotente;
- rejeita generation obsoleta;
- registra reason_code.

Transição inexistente é proibida por padrão.

## 10. Idempotência

Todo comando material possui:

- command_id UUIDv7;
- idempotency_key;
- project_id;
- actor_id;
- action;
- normalized_payload_hash;
- first_seen_at;
- final_outcome_ref.

Mesma chave e mesmo payload devolvem o resultado registrado. Mesma chave com payload diferente gera IDEMPOTENCY_CONFLICT.

## 11. Concorrência

O primeiro runtime pode executar sequencialmente. As primitivas de concorrência existem desde F0:

- optimistic version;
- lease;
- generation;
- fencing_token;
- idempotency;
- cancel token;
- timeout;
- heartbeat quando aplicável.

Concorrência é ampliada apenas após teste de duplicidade, starvation, cancelamento, recovery e capacidade.

## 12. Tempo

### Persistido e distribuído

Usar timestamp UTC com precisão declarada, sequence, authority_epoch e generation.

### Local ao processo

Relógio monotônico serve para medir duração, timeout e backoff enquanto o processo permanece vivo.

Referência monotônica nunca é persistida como instante global nem comparada entre nós.

## 13. Lease e fencing

Lease é emitido por autoridade identificada para um resource_scope.

Commit material exige:

- lease ACTIVE;
- authority_epoch atual;
- generation atual;
- fencing_token igual ou superior ao último aceito;
- prazo válido considerando clock_uncertainty;
- capability compatível.

Uma geração antiga pode enviar evidência, mas não mutar estado compartilhado.

## 14. Federação

Fluxo:

~~~text
DISCOVER
→ ENROLL
→ AUTHENTICATE
→ NEGOTIATE VERSION
→ ADVERTISE CAPABILITY
→ ISSUE LEASE
→ DISPATCH
→ HEARTBEAT
→ RESULT CANDIDATE
→ RECONCILE
→ COMMIT OR REJECT
~~~

Operação local continua durante partição quando possui dependências e delegação válidas.

### Mobilidade de workspace, estado e artefato

Transferência entre nós usa MigrationBundle com:

- project_id e mission_id;
- source_node_id e target_node_id;
- workspace manifest;
- aggregate versions;
- checkpoint válido;
- artefatos e hashes;
- capabilities requeridas;
- generation de origem;
- motivo e policy_version.

Fluxo:

~~~text
FREEZE MUTABLE SCOPE
→ CREATE VALID CHECKPOINT
→ BUILD HASHED MIGRATION BUNDLE
→ TRANSFER
→ VERIFY DESTINATION
→ ISSUE NEW GENERATION
→ ACTIVATE DESTINATION
→ REVOKE SOURCE LEASE
→ CONFIRM HANDOVER
~~~

A origem não apaga dados antes da confirmação. Falha retorna ao checkpoint anterior sem duas gerações capazes de commit.

### Micro-scheduler do nó

Um nó pode ordenar e executar WorkUnits recebidas somente dentro de DelegationEnvelope pré-emitido. Ele não pode:

- criar objetivo ou missão;
- criar WorkUnit fora do conjunto delegado;
- ampliar capability;
- alterar prioridade global;
- renovar autoridade offline;
- confirmar mutação compartilhada sem reconcile;
- declarar MISSION_PROVEN.

## 15. Operação offline

| Effect class | Offline |
|---|---|
| READ_ONLY | permitido por capability finita |
| REVERSIBLE_LOCAL | permitido por capability finita |
| SHARED_MUTATION | somente candidato até reconciliação |
| EXTERNAL_IRREVERSIBLE | proibido |

Delegação offline não se autorrenova. Policy define TTL finito e auditável.

### Fairness multiprojeto

Governor aplica quota, peso, limite e reserva mínima por projeto. Prioridade alta pode preemptar trabalho elegível, mas não causar starvation indefinida de outro projeto sem regra explícita e auditada.

## 16. Segurança

Toda porta de entrada material executa:

~~~text
IDENTITY
→ PROJECT/MISSION OWNERSHIP
→ POLICY VERSION
→ CAPABILITY
→ EFFECT CLASS
→ HUMAN GATE
→ EXECUTION
→ AUDIT
~~~

Safe default é deny.

## 17. Segredos

Segredo é acessado por SecretRef. Componentes recebem somente o valor necessário, durante o tempo necessário, sem registrá-lo em log, evento, evidência, prompt ou Read Model.

O banco físico de segredos será escolhido com a stack. O contrato de Vault existe desde F0.

## 18. IA multi-provider

Provider Adapter normaliza:

- capacidades;
- limites;
- preço e orçamento;
- latência;
- saúde funcional;
- privacidade;
- contexto;
- resposta;
- erro;
- proveniência.

Policy Router filtra antes de Provider Router. Failover não pode mudar classificação, orçamento ou autoridade.

### Economia de execução

Toda decisão material registra estimativa e consumo observado quando mensuráveis:

- compute local;
- armazenamento;
- rede;
- provedor;
- licença ou serviço;
- duração;
- tentativas;
- custo evitado por cache ou reutilização.

Budget Ledger é project-scoped. Estimativa não é cobrança. Novo gasto fora do envelope aciona o portão financeiro antes da execução.

## 19. Conhecimento

Knowledge Store é separado de:

- Policy Store;
- Secret Store;
- Operational State;
- Training Dataset.

Promoção exige proveniência e gate. Conteúdo não confiável pode ser consultado como referência, mas não injeta regra soberana.

## 20. Produto construído

Product Testing e Product Security operam sobre um Product Contract derivado dos requisitos da missão. Gates não aplicáveis exigem justificativa persistida.

## 21. Painel

O painel usa:

- Query API para leitura;
- Command API para intenção;
- Event Stream para atualização;
- Read Models reconstruíveis.

Não acessa tabela soberana diretamente.

## 22. Recuperação

Na inicialização:

~~~text
VALIDATE CONFIG
→ OPEN TRANSACTION STORE
→ VERIFY MIGRATIONS
→ RECONCILE INBOX/OUTBOX
→ EXPIRE INVALID LEASES
→ REBUILD OR VERIFY READ MODELS
→ RESUME NON-TERMINAL MISSIONS
→ REPORT READY
~~~

READY exige saúde funcional mínima, não apenas processo ativo.

## 23. Atualização

Atualização futura deve usar:

- pacote identificado e verificado;
- backup;
- compatibilidade de schema;
- instalação side-by-side quando possível;
- health gate;
- rollback;
- preservação de missões.

## 24. Implantação evolutiva

### Primeiro incremento

Um processo principal, um store transacional, um Engine local e um painel simples podem satisfazer a fatia inicial.

### Extração posterior

Componente só vira processo ou serviço separado quando medição comprovar necessidade de isolamento, escalabilidade, privilégio ou ciclo de vida.

## 25. Restrições de dependência

É proibido:

- Domain importar adapter;
- UI gravar estado;
- Engine ler segredo arbitrário;
- Brain chamar sistema operacional diretamente;
- Scheduler criar WorkUnit;
- Proof Engine mudar Mission;
- Worker confirmar próprio sucesso;
- barramento substituir journal;
- cache substituir fonte oficial;
- nó offline executar efeito irreversível.

## 26. Critérios de aceite arquitetural

- dependências de camada verificadas automaticamente;
- autoridade coberta por testes de contrato;
- mutação atômica comprovada com falha injetada;
- replay/rebuild reproduzível;
- duplicidade sem efeito duplo;
- lease antigo rejeitado;
- ProofVerdict obsoleto rejeitado;
- isolamento multiprojeto comprovado;
- portões testados;
- reinício retoma missão;
- primeira fatia vertical atinge MISSION_PROVEN.
