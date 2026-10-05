# POD — ARQUITETURA TÉCNICA LÓGICA — V003

**Identificador:** POD-DOC-005
**Versão:** 3.0.0
**Status:** ACTIVE
**Data:** 2026-09-13
**Conjunto alvo:** POD-DOCSET-V004
**Autoridade:** A2 — arquitetura técnica
**Substitui:** POD_ARQUITETURA_TECNICA_V002
**Decisão principal:** ADR-010

## 1. Objetivo

Definir a arquitetura reconciliada do POD sem escolher prematuramente stack física ou multiplicar processos. Esta versão preserva o monólito modular local-first como ponto de partida, mas separa normativamente Core, planos lógicos, classes de estado e integrações.

## 2. Forma arquitetural

A unidade inicial recomendada continua sendo um monólito modular com portas explícitas. Componentes somente são extraídos para processos/serviços separados quando testes demonstrarem necessidade de privilégio, isolamento, escalabilidade, disponibilidade ou ciclo de vida independente.

Separação lógica não implica microserviços.

## 3. Core

~~~text
POD CORE
├── Bootstrap
├── POD Identity
├── Fundamental Contracts
└── Governance Kernel
~~~

O Core é pequeno e selado por release.

É proibido armazenar no Core:

- dados de projeto;
- dados de missão;
- evidência;
- checkpoint;
- workspace;
- cache;
- embeddings;
- índices;
- contexto temporário;
- logs operacionais;
- segredos;
- configuração mutável;
- materializações reconstruíveis.

## 4. Planos lógicos reconciliados

### 4.1 Control Plane

- Command Ingress;
- Admission;
- Mission Core;
- Governor;
- Scheduler;
- Supervisor;
- Recovery;
- Policy Engine;
- Capability Registry;
- Resource Governor.

Decide, limita e coordena. Não executa efeito físico arbitrário.

### 4.2 Cognition Plane

- Brain;
- Context Builder;
- SCM Query;
- Memory Distiller;
- Knowledge Admission;
- Contradiction Resolution;
- Revalidation.

Planeja e produz candidatos cognitivos. Não altera estado soberano de missão diretamente.

### 4.3 Execution Plane

- Construction Engineering;
- Mission Runtime;
- Work Core;
- Engine;
- Worker Runtime;
- Windows Engine Adapter;
- Linux Engine Adapter;
- Artifact Handling.

Executa somente dentro de Execution Envelope autorizado.

### 4.4 Data Plane

- Authoritative Transaction Store;
- Domain Event Journal;
- Inbox/Outbox;
- Operational State;
- Canonical Knowledge;
- Knowledge Ledger;
- Evidence Store;
- Checkpoint Store;
- Artifact Store;
- Read Models e projeções reconstruíveis.

Fonte durável e auditável.

### 4.5 Integration Plane

- AI Provider Adapters;
- External API Adapters;
- Protocol Adapters;
- Connectors;
- Webhooks;
- Message/Transport Adapters.

Nenhuma integração externa invade Domain/Core.

### 4.6 Security — controle transversal

- Identity;
- Authentication;
- Authorization;
- Capability;
- Vault Port;
- Audit;
- Immune System;
- Incident Handling.

Segurança atravessa todos os planos; não se torna fonte de objetivo ou prova.

### 4.7 Federation — capacidade transversal

- Node Registry;
- Enrollment;
- Compatibility;
- Lease Authority;
- Dispatch;
- Reconciliation.

Federação distribui capacidade, não soberania não delegada.

### 4.8 Experience Surfaces

- Terminal próprio;
- Panel;
- Launcher;
- API;
- Notifications.

Superfícies não escrevem fonte soberana diretamente.

## 5. Dependências de camada

~~~text
DOMAIN       -> nenhuma camada externa
APPLICATION  -> DOMAIN
ADAPTERS     -> APPLICATION + DOMAIN
RUNTIME      -> composição das anteriores

CORE         -> contratos mínimos
CONTROL      -> contratos internos
COGNITION    -> portas de dados e integração
EXECUTION    -> portas autorizadas
DATA         -> persistência e projeções
INTEGRATION  -> traduz externo para contratos internos
~~~

Dependência reversa de fornecedor para dentro do domínio é proibida.

## 6. Autoridades

| Assunto | Autoridade |
|---|---|
| estado de missão | Mission Core |
| estratégia | Brain |
| procedimento técnico | Construction Engineering |
| recursos e quotas | Governor / Resource Governor |
| despacho | Scheduler |
| execução física | Engine/Worker |
| prova | Proof Engine emite verdict; Mission Core consome |
| política/autorização | Policy/Security |
| conhecimento canônico | SCM Knowledge Admission + ledger |
| dados operacionais | store transacional proprietário |
| integração | adapter sem soberania própria |

## 7. Execution Envelope

Cada missão aceita deve possuir envelope efetivo:

~~~text
mission_id
project_id
objective
constraints
allowed_capabilities
security_scope
resource_budget
workspace_policy
retention_policy
timeout_policy
rollback_policy
evidence_policy
knowledge_policy
integration_policy
~~~

WorkUnit pode restringir, nunca ampliar.

## 8. Classes de estado

### DURABLE

- aggregate soberano;
- journal;
- approvals;
- leases quando vigentes;
- conhecimento canônico e ledger;
- evidência obrigatória;
- checkpoints ainda necessários;
- artefatos promovidos;
- auditoria obrigatória.

### RECONSTRUCTIBLE

- read models;
- embeddings;
- índices vetoriais;
- índices lexicais;
- projeções de Knowledge Graph;
- caches derivados;
- materializações analíticas.

### EPHEMERAL

- temp;
- staging;
- download intermediário;
- scratch;
- workspace descartável;
- buffer de execução.

Regra: nada persiste sem classificação.

## 9. SCM

~~~text
SCM
├── Knowledge Admission
├── Canonical Knowledge
├── Knowledge Ledger
├── Distillation
├── Contradiction Resolution
├── Revalidation
└── Retrieval Interface
~~~

RAG é mecanismo de retrieval. Não é fonte canônica.

~~~text
CANONICAL KNOWLEDGE
→ VECTOR PROJECTION
→ LEXICAL PROJECTION
→ KNOWLEDGE GRAPH PROJECTION
→ HOT CONTEXT CACHE
~~~

Todas as projeções são descartáveis e reconstruíveis.

## 10. Conhecimento

Fluxo de promoção:

~~~text
EXECUTION
→ KNOWLEDGE_CANDIDATE
→ PROVENANCE_CHECK
→ EVIDENCE_CHECK
→ SECRET_AND_SENSITIVE_FILTER
→ DEDUPLICATION
→ CONTRADICTION_CHECK
→ SCOPE_VALIDATION
→ CONFIDENCE_ASSIGNMENT
→ KNOWLEDGE_ADMISSION_GATE
→ CANONICAL_KNOWLEDGE
~~~

Confidence e freshness são dimensões independentes.

Contradição não substitui silenciosamente conhecimento anterior. O ledger preserva a evolução e o escopo.

## 11. Destilação

Ao fechar etapa elegível:

~~~text
PERSIST RESULT
→ PRESERVE REQUIRED EVIDENCE
→ EMIT KNOWLEDGE_DISTILLATION_REQUESTED
→ CONTINUE WHEN INDEPENDENT
~~~

A destilação só bloqueia o próximo passo quando ele depende especificamente do conhecimento em promoção.

## 12. Evidência e artefatos

Evidence/Artifact Store suporta referência por conteúdo:

~~~text
content_ref = sha256:<digest>
~~~

Metadados permanecem project/mission scoped. Bytes idênticos podem ser fisicamente deduplicados sem misturar ownership, autorização ou retenção.

Garbage collection só remove objeto quando nenhuma referência durável válida exigir preservação.

## 13. Fluxo de comando

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

ACK confirma aceite durável, não conclusão.

## 14. Fluxo de mutação

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

## 15. Proof flow

~~~text
MISSION CORE requests proof evaluation
→ PROOF ENGINE loads exact criteria and policy versions
→ validates Evidence Manifest and mandatory gates
→ emits immutable ProofVerdict
→ MISSION CORE reloads mission version
→ validates verdict freshness and guards
→ atomically records verdict consumption and MISSION_PROVEN
~~~

## 16. Multiprojeto

Uma instalação POD opera N projetos isolados por `project_id`.

Isolamento obrigatório:

- estado;
- segredo;
- orçamento;
- evidência;
- workspace;
- conhecimento project-scoped;
- quotas;
- execution envelope;
- políticas.

Compartilhamento exige regra explícita e auditável.

## 17. IA híbrida e independência

Modelo é recurso substituível.

~~~text
PROVIDER != BRAIN
MODEL_OUTPUT != POLICY
MODEL_OUTPUT != AUTHORIZATION
MODEL_OUTPUT != PROOF
~~~

Fluxo:

~~~text
POD COGNITION
→ POLICY ROUTER
→ PROVIDER ROUTER
→ PROVIDER ADAPTER
→ EXTERNAL MODEL/API
~~~

POD pode operar sem ChatGPT, MCP ou fornecedor específico quando capacidades locais/alternativas satisfizerem a missão.

## 18. Federação

Preserva-se o modelo V002 de lease, generation, fencing e reconciliação. Nó remoto recebe autoridade finita e não declara MISSION_PROVEN.

## 19. Segurança

Safe default é deny.

~~~text
IDENTITY
→ SCOPE
→ POLICY
→ CAPABILITY
→ EFFECT CLASS
→ HUMAN GATE
→ EXECUTION
→ AUDIT
~~~

## 20. Atualização e rollback

~~~text
BUILD NEW RELEASE OUTSIDE ACTIVE CORE
→ VERIFY PACKAGE AND MANIFEST
→ VALIDATE SCHEMA COMPATIBILITY
→ START SIDE-BY-SIDE WHEN POSSIBLE
→ HEALTH GATE
→ ATOMICALLY SWITCH ACTIVE RELEASE
→ RECONCILE
→ OBSERVE
~~~

Falha pós-promoção:

~~~text
SWITCH TO LAST VERIFIED RELEASE
→ RECONCILE STATE
→ RESTART REQUIRED COMPONENTS
→ HEALTH GATE
→ OPEN INCIDENT
~~~

Release ativa não é editada in-place.

## 21. Topologia física de referência

Linux, quando adotado:

~~~text
/opt/pod/releases/<version>/
/opt/pod/current -> /opt/pod/releases/<version>

/srv/pod/projects/
/srv/pod/missions/
/srv/pod/memory/
/srv/pod/evidence/
/srv/pod/checkpoints/

/var/cache/pod/
/var/log/pod/
/run/pod/
/archive/pod/
~~~

A topologia Windows deve preservar as mesmas fronteiras lógicas, sem exigir os mesmos caminhos.

## 22. Higiene de encerramento

Toda missão/execução de aceite que possa gerar resíduos deve produzir evidência equivalente a:

~~~text
CORE_INTEGRITY=PASS
CORE_SIZE_DRIFT=PASS
CORE_DIRTY_FILES=0
PROJECT_FILES_IN_CORE=0
MISSION_FILES_IN_CORE=0
CACHE_IN_CORE=0
TEMP_IN_CORE=0
EVIDENCE_IN_CORE=0
UNEXPECTED_RESIDUE=0
KNOWLEDGE_CANDIDATES_REVIEWED=PASS
MANDATORY_EVIDENCE_PRESERVED=PASS
REQUIRED_CHECKPOINT_PRESERVED=PASS
TEMP_RETENTION_APPLIED=PASS
~~~

## 23. Métricas cognitivas e físicas

~~~text
SCM_TOTAL_SIZE
SCM_OBJECT_COUNT
SCM_GROWTH_RATE
DUPLICATION_RATIO
STALE_KNOWLEDGE_RATIO
UNVALIDATED_CANDIDATES
REVALIDATION_BACKLOG
CORE_RELEASE_SIZE
CORE_SIZE_DRIFT
EPHEMERAL_RESIDUE_BYTES
~~~

## 24. Invariantes superiores

~~~text
NOTHING_EXECUTES_WITHOUT_SCOPE = TRUE
NOTHING_PERSISTS_WITHOUT_CLASSIFICATION = TRUE
NOTHING_BECOMES_KNOWLEDGE_WITHOUT_EVIDENCE = TRUE
NOTHING_EXTERNAL_BECOMES_STRUCTURAL_DEPENDENCY = TRUE

CORE_CONTAMINATION = 0
REGENERABLE_DATA_IN_CORE = 0
UNTRACEABLE_KNOWLEDGE = 0
UNSCOPED_KNOWLEDGE = 0
UNREVERSIBLE_KNOWLEDGE = 0
~~~

## 25. Critérios de aceite arquitetural

Além dos critérios V002 preservados:

- release do Core imutável;
- promoção e rollback atômicos comprovados;
- configuração/segredo/estado externos ao Core;
- isolamento físico de projeto e missão;
- classificação de persistência testada;
- projection rebuild sem perda canônica;
- Knowledge Admission Gate testado;
- revogação cognitiva testada;
- revalidação por evento/tempo/risco testada;
- CAS de evidência validado;
- deduplicação sem quebra de ownership;
- higiene final com zero resíduo no Core;
- integração externa substituível por contrato;
- primeira fatia vertical continua exigindo MISSION_PROVEN.
