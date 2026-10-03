# POD — CONTRATOS, DADOS, ESTADOS E EVENTOS — V002

**Identificador:** POD-DOC-006
**Versão:** 2.0.0
**Status:** ACTIVE
**Data:** 2026-09-02
**Conjunto:** POD-DOCSET-V003
**Autoridade:** A2 — contratos normativos
**Substitui:** contratos conceituais V001, modelo canônico V001 e contratos do DOCSET V002
**Implementação comprovada:** NÃO

## 1. Finalidade

Definir autoridade, identidades, entidades, estados, transições, eventos, consistência e protocolos mínimos. Tipos físicos de banco e linguagem serão derivados deste contrato.

## 2. Invariantes

~~~text
NO_COMPETING_SOVEREIGN_AUTHORITIES = TRUE
MISSION_CORE_IS_SOLE_MISSION_STATE_WRITER = TRUE
PROOF_ENGINE_EMITS_VERDICT_ONLY = TRUE
ATOMIC_STATE_EVENT_OUTBOX = TRUE
ACK_IS_NOT_RESULT = TRUE
AT_LEAST_ONCE_TRANSPORT = TRUE
IDEMPOTENCY_REQUIRED = TRUE
STALE_GENERATION_CANNOT_COMMIT = TRUE
READ_MODEL_IS_NOT_SOURCE_OF_TRUTH = TRUE
PROVIDER_IS_NOT_BRAIN = TRUE
KNOWLEDGE_IS_NOT_POLICY = TRUE
TASK_IS_UI_ALIAS_FOR_WORK_UNIT = TRUE
MONOTONIC_TIME_IS_PROCESS_LOCAL = TRUE
PROJECT_SCOPE_IS_EXPLICIT = TRUE
SECRET_IS_NEVER_EVENT_PAYLOAD = TRUE
ACTIVITY_IS_NOT_PROGRESS = TRUE
~~~

## 3. Autoridade

| Assunto | Propõe | Autoriza ou limita | Executa | Persiste | Avalia | Transiciona |
|---|---|---|---|---|---|---|
| missão | Owner/Ingress | Admission/Policy | — | Memory | — | Mission Core |
| estratégia | Brain | Policy/Governor | Construction Engineering | Memory | Proof Engine no resultado | — |
| WorkUnit | Construction Engineering | Policy/Governor | Engine | Memory | testes/evidência | Work Core |
| recursos | Governor | Policy | Scheduler | Memory | observabilidade | Governor |
| ação física | Engine | Policy/Capability/Gate | Engine/Worker | Memory | Evidence/Proof | — |
| prova | Proof Engine | critérios/policy | — | Memory | Proof Engine | Mission Core |
| segurança | Security | Policy | Immune System/Engine | Memory | Security gates | componente proprietário |
| federação | Federation | Policy/Governor | Node Agent | Memory | Reconciler | componente proprietário |

## 4. Identificadores

Todas as entidades globais usam UUIDv7 textual canônico em minúsculas.

Regras:

- imutável;
- nunca reutilizado;
- gerado localmente sem coordenador;
- validado na fronteira;
- PID, hostname, título e caminho não são identidade;
- IDs externos são preservados em campos external_ref, nunca substituem ID soberano.

Entidades:

~~~text
pod_id
project_id
mission_id
work_unit_id
attempt_id
command_id
event_id
message_id
checkpoint_id
evidence_id
artifact_id
proof_verdict_id
approval_id
incident_id
lease_id
node_id
worker_id
provider_id
model_id
knowledge_id
correlation_id
~~~

O termo Task é rótulo de interface. Não existe task_id canônico.

## 5. Dimensões de escopo

### ownership_scope

~~~text
GLOBAL_POD
PROJECT:<project_id>
MISSION:<mission_id>
NODE_LOCAL:<node_id>
~~~

### confidentiality

~~~text
PUBLIC
INTERNAL
CONFIDENTIAL
SECRET
~~~

### training_eligibility

~~~text
DENIED
ALLOWED_WITH_REDACTION
ALLOWED
~~~

### execution_effect

~~~text
READ_ONLY
REVERSIBLE_LOCAL
SHARED_MUTATION
EXTERNAL_IRREVERSIBLE
~~~

### trust_status

~~~text
UNTRUSTED
PROVISIONAL
TRUSTED
DEGRADED
QUARANTINED
REVOKED
~~~

Cada dimensão possui campo separado e política própria.

## 6. Envelope comum

Todo Command, Event e Message material contém:

~~~text
schema_name
schema_version
id
correlation_id
causation_id optional
pod_id
project_id
mission_id optional
actor_id
actor_type
ownership_scope
created_at_utc
producer
producer_version
payload
payload_hash
classification
trace_context
~~~

Campos desconhecidos são rejeitados em comandos críticos e preservados em eventos quando a versão permitir forward compatibility.

## 7. Project

Campos mínimos:

~~~text
project_id
name
status
version
policy_version
resource_policy_ref
budget_policy_ref
security_classification
workspace_manifest_ref
created_at_utc
updated_at_utc
~~~

Estados:

~~~text
ACTIVE
PAUSED
SUSPENDED_BY_POLICY
ARCHIVED
~~~

ARCHIVED é terminal para mutações comuns. Restauração exige comando autorizado e nova versão.

## 8. Mission

Campos mínimos:

~~~text
mission_id
project_id
objective
objective_version
constraints
acceptance_criteria_ref
acceptance_criteria_version
policy_version
priority
resource_envelope_ref
budget_policy_ref
approval_policy_ref
deadline_policy_ref
max_same_strategy_attempts
max_stagnation_cycles
replan_policy_ref
impossibility_proof_policy_ref
status
resume_state optional
current_strategy_ref optional
version
accepted_at_utc optional
terminal_at_utc optional
created_at_utc
updated_at_utc
~~~

### Estados

~~~text
RECEIVED
ACCEPTED
RUNNING
REPLANNING
RECOVERING
PAUSED
WAITING_EXTERNAL
WAITING_FINANCIAL_AUTHORIZATION
WAITING_OWNER_APPROVAL
PROVING
MISSION_PROVEN
CANCELLED_BY_OWNER
SUPERSEDED
TERMINATED_BY_POLICY
IMPOSSIBLE_PROVEN
REJECTED_BEFORE_ACCEPTANCE
~~~

### Estados terminais

~~~text
MISSION_PROVEN
CANCELLED_BY_OWNER
SUPERSEDED
TERMINATED_BY_POLICY
IMPOSSIBLE_PROVEN
REJECTED_BEFORE_ACCEPTANCE
~~~

Terminal é imutável. Correção posterior cria nova missão ligada por supersedes_mission_id.

## 9. Transições de Mission

| Origem | Comando/evento | Destino | Guarda obrigatória |
|---|---|---|---|
| RECEIVED | ADMIT | ACCEPTED | contrato completo, critérios testáveis, policy válida, limites de loop definidos |
| RECEIVED | REJECT | REJECTED_BEFORE_ACCEPTANCE | reason_code e regra de admissão |
| ACCEPTED | START | RUNNING | commit de aceite confirmado |
| RUNNING | REPLAN_REQUIRED | REPLANNING | falha/risco/estagnação registrados |
| REPLANNING | PLAN_ACCEPTED | RUNNING | estratégia diferente ou nova evidência |
| qualquer não terminal após aceite | RECOVERY_REQUIRED | RECOVERING | incidente ou falha recuperável |
| RECOVERING | RECOVERY_PASSED | resume_state | checkpoint e reconciliação válidos |
| RUNNING ou REPLANNING | REQUEST_PROOF | PROVING | critérios executáveis e Evidence Pack fechado |
| PROVING | PROOF_FAILED | REPLANNING | verdict FAILED ou INCONCLUSIVE |
| PROVING | PROOF_PASSED | MISSION_PROVEN | ProofVerdict atual e todos os guards |
| qualquer não terminal após aceite | PAUSE | PAUSED | ator autorizado e resume_state persistido |
| PAUSED | RESUME | resume_state | bloqueio ausente e policy revalidada |
| qualquer não terminal após aceite | EXTERNAL_MISSING | WAITING_EXTERNAL | dependência indispensável comprovada |
| WAITING_EXTERNAL | EXTERNAL_RESTORED | resume_state | conexão/condição revalidada |
| qualquer não terminal após aceite | FINANCIAL_GATE | WAITING_FINANCIAL_AUTHORIZATION | gasto novo não autorizado |
| WAITING_FINANCIAL_AUTHORIZATION | FINANCIAL_DECISION | resume_state | Approval válido ou estratégia gratuita |
| qualquer não terminal após aceite | OWNER_GATE | WAITING_OWNER_APPROVAL | ação protegida pela policy |
| WAITING_OWNER_APPROVAL | OWNER_DECISION | resume_state | Approval válido ou ramo descartado |
| qualquer não terminal após aceite | CANCEL | CANCELLED_BY_OWNER | Owner autorizado |
| qualquer não terminal após aceite | SUPERSEDE | SUPERSEDED | nova missão ligada e ator autorizado |
| qualquer não terminal após aceite | POLICY_TERMINATE | TERMINATED_BY_POLICY | regra, evidência e auditoria |
| RUNNING, REPLANNING ou PROVING | IMPOSSIBILITY_PASSED | IMPOSSIBLE_PROVEN | verdict de esgotamento dos caminhos admissíveis |

Transição não listada é STATE_TRANSITION_DENIED.

## 10. Guardas de MISSION_PROVEN

Todas devem ser verdadeiras:

~~~text
mission.status == PROVING
proof_verdict.verdict == PASSED
proof_verdict.mission_id == mission.mission_id
proof_verdict.mission_version == mission.version
proof_verdict.acceptance_criteria_version == mission.acceptance_criteria_version
proof_verdict.policy_version == mission.policy_version
evidence_manifest.hash == proof_verdict.evidence_manifest_hash
mandatory_gates == PASSED_OR_JUSTIFIED_NOT_APPLICABLE
open_critical_failures == 0
current_generation_is_authoritative == TRUE
~~~

O consumo do verdict e a transição pertencem à mesma transação.

## 11. WorkUnit

Campos:

~~~text
work_unit_id
mission_id
project_id
parent_work_unit_id optional
kind
title
input_refs
expected_output_contract
acceptance_criteria_ref
dependency_ids
required_capabilities
execution_effect
priority
timeout_policy
retry_policy
resource_limits
status
generation
version
created_at_utc
updated_at_utc
~~~

Estados:

~~~text
DEFINED
READY
LEASED
RUNNING
VERIFYING
SUCCEEDED
FAILED_ATTEMPT
BLOCKED
PAUSED
CANCELLED
SUPERSEDED
~~~

SUCCEEDED significa critério da WorkUnit comprovado; não significa missão concluída.

Preempção cooperativa de RUNNING segue:

~~~text
PREEMPT_REQUESTED
→ SAFE_POINT
→ CHECKPOINT
→ RELEASE LEASE
→ PAUSED
~~~

Se o processo não cooperar, a tentativa é contida, marcada LOST ou CANCELLED conforme evidência e recuperada por nova generation.

Compensação é nova WorkUnit de kind COMPENSATION ligada ao efeito original. Ela não apaga evento, tentativa ou evidência anterior.

## 12. Attempt

Campos:

~~~text
attempt_id
work_unit_id
mission_id
node_id
worker_id
generation
fencing_token
strategy_fingerprint
started_at_utc
ended_at_utc optional
status
outcome_ref optional
failure_fingerprint optional
resource_usage_ref
~~~

Estados:

~~~text
CREATED
RUNNING
SUCCEEDED
FAILED
TIMED_OUT
CANCELLED
LOST
RECONCILED
~~~

Tentativa terminal não é reaberta.

## 13. Command e ACK

Command:

~~~text
command_id
idempotency_key
normalized_payload_hash
actor_id
action
target_ref
expected_version optional
generation optional
fencing_token optional
status
accepted_at_utc optional
outcome_ref optional
~~~

Estados:

~~~text
RECEIVED
REJECTED
ACCEPTED
EXECUTING
COMPLETED
FAILED
UNKNOWN_OUTCOME
~~~

ACK:

~~~text
ACK_REJECTED
ACK_ACCEPTED_DURABLE
ACK_DUPLICATE_SAME_PAYLOAD
ACK_CONFLICT_DIFFERENT_PAYLOAD
~~~

ACK_ACCEPTED_DURABLE significa que Command e inbox foram commitados. Não significa COMPLETED.

## 14. Persistência atômica

Registros da mesma mutação:

- aggregate row com version;
- domain_event;
- outbox_message;
- command outcome ou inbox record;
- idempotency record;
- audit record.

São gravados na mesma transação local. O evento só pode ser publicado após commit; a confirmação ao chamador só pode ser enviada após commit.

## 15. DomainEvent

Campos:

~~~text
event_id
event_type
aggregate_type
aggregate_id
aggregate_version
sequence
correlation_id
causation_id
project_id
mission_id optional
actor_id
occurred_at_utc
recorded_at_utc
schema_version
payload
payload_hash
classification
~~~

Eventos são append-only. Correção gera novo evento compensatório; não reescreve história.

Famílias:

~~~text
project.*
mission.*
work_unit.*
attempt.*
command.*
proof.*
approval.*
lease.*
node.*
artifact.*
checkpoint.*
security.*
incident.*
provider.*
knowledge.*
delivery.*
~~~

## 16. Inbox e Outbox

Inbox deduplica comando recebido. Outbox entrega evento ou mensagem.

Campos comuns:

~~~text
message_id
topic
partition_key
payload_ref
payload_hash
status
attempt_count
available_at_utc
lease fields
last_error_code optional
created_at_utc
delivered_at_utc optional
~~~

Estados:

~~~text
PENDING
LEASED
DELIVERED
RETRY_SCHEDULED
DEAD_LETTER
~~~

DEAD_LETTER é estado visível e reconciliável, não descarte.

## 17. Evidence

Campos:

~~~text
evidence_id
project_id
mission_id
work_unit_id optional
attempt_id optional
command_id optional
node_id optional
generation optional
evidence_type
content_ref
content_hash
provenance
producer
producer_version
observed_at_utc
recorded_at_utc
classification
redaction_status
validation_status
~~~

Evidência sem proveniência ou hash não pode satisfazer gate crítico.

## 18. EvidenceManifest

Campos:

~~~text
evidence_manifest_id
mission_id
mission_version
criteria_version
evidence_refs ordered
known_failures
known_limitations
created_at_utc
content_hash
status
~~~

Estados: CANDIDATE, SEALED, INVALIDATED, CONSUMED.

SEALED é imutável. Nova evidência cria novo manifesto.

## 19. ProofVerdict

Definido pelo ADR-003.

Estados:

~~~text
PASSED
FAILED
INCONCLUSIVE
~~~

Não aplicável é resultado de gate individual com justificativa; não é verdict final.

## 20. Checkpoint

Campos:

~~~text
checkpoint_id
project_id
mission_id
work_unit_id optional
aggregate_versions
state_manifest_ref
content_hash
generation
created_at_utc
validation_status
replay_metadata
~~~

Estados:

~~~text
CANDIDATE
VALIDATING
VALID
INVALID
SUPERSEDED
RESTORED
~~~

Restore nunca reduz fencing_token aceito.

## 21. Artifact

Campos:

~~~text
artifact_id
project_id
mission_id
artifact_type
version
content_ref
content_hash
manifest_ref
producer_attempt_id
status
promotion_proof_ref
created_at_utc
~~~

Estados:

~~~text
CANDIDATE
TESTING
VALIDATED
PROMOTED
REJECTED
SUPERSEDED
~~~

PROMOTED exige prova vinculada à versão exata.

## 22. Approval

Campos:

~~~text
approval_id
approval_type
project_id
mission_id
actor_id
action
target_ref
payload_hash
amount_and_currency optional
scope
decision
reason optional
issued_at_utc
expires_at_utc optional
consumed_at_utc optional
status
~~~

Tipos:

~~~text
FINANCIAL
OWNER_SOVEREIGN
RISK_ACCEPTANCE
~~~

Estados:

~~~text
REQUESTED
APPROVED
DENIED
EXPIRED
REVOKED
CONSUMED
~~~

Aprovação é específica e não concede privilégio global.

## 23. Lease

Campos e regras seguem ADR-006.

Estados:

~~~text
ACTIVE
EXPIRING
EXPIRED
REVOKED
SUPERSEDED
~~~

Validação ocorre no commit. Dispatch válido não garante commit futuro.

## 24. Node

Campos:

~~~text
node_id
identity_ref
trust_status
protocol_version
agent_version
capabilities
health_status
resource_snapshot_ref
connection_state
authority_epoch
last_seen_at_utc
version
~~~

Ciclo:

~~~text
DISCOVERED
→ ENROLLING
→ PROVISIONAL
→ READY
→ DRAINING
→ OFFLINE
→ RECOVERING
→ READY
~~~

Desvios: DEGRADED, QUARANTINED, UPGRADE_REQUIRED, REVOKED.

## 25. DelegationEnvelope

Campos:

~~~text
delegation_id
issuer_node_id
target_node_id
project_id
mission_id
work_unit_ids
capability_refs
effect_classes
resource_limits
priority_bounds
authority_epoch
generation
issued_at_utc
expires_at_utc
offline_allowed
max_local_concurrency
status
~~~

O micro-scheduler local pode ordenar somente work_unit_ids do envelope. Não cria nova autoridade, não renova o envelope offline e não muda missão.

## 26. MigrationBundle

Campos:

~~~text
migration_bundle_id
project_id
mission_id
source_node_id
target_node_id
workspace_manifest_ref
aggregate_versions
checkpoint_id
artifact_refs
content_hash
source_generation
target_generation optional
policy_version
status
created_at_utc
verified_at_utc optional
~~~

Estados:

~~~text
CREATED
SEALED
TRANSFERRING
VERIFIED
ACTIVATED
ROLLED_BACK
REJECTED
~~~

Ativação no destino e revogação da origem impedem duas gerações autoritativas. Dados de origem só podem ser removidos após handover confirmado e retenção aplicável.

## 27. BudgetLedger

Campos:

~~~text
budget_entry_id
project_id
mission_id optional
work_unit_id optional
provider_id optional
resource_type
estimate_amount optional
observed_amount optional
unit
currency optional
authorization_ref optional
recorded_at_utc
provenance
~~~

Estimativa e consumo observado são campos distintos. Novo gasto monetário acima do envelope não pode ser registrado como autorizado por inferência.

## 28. Provider e Model

Provider Capability:

~~~text
provider_id
model_id
capability
limits
privacy_class
cost_policy_ref
health_status
context_format_version
adapter_version
last_verified_at_utc
~~~

Saída de modelo inclui provider, model, versão, request_hash, response_hash, uso, custo observado e policy decision.

## 29. Knowledge

Campos:

~~~text
knowledge_id
ownership_scope
confidentiality
training_eligibility
source_ref
source_hash
provenance
confidence_status
valid_from_utc
valid_until_utc optional
content_ref
version
status
~~~

Estados de confiança:

~~~text
UNTRUSTED
PROVISIONAL
VERIFIED
STALE
REVOKED
~~~

## 30. Incident

Campos:

~~~text
incident_id
severity
project_id optional
mission_id optional
detected_at_utc
status
symptom
impact
containment
cause_status
cause
recovery_ref
evidence_refs
closed_at_utc optional
~~~

Estados: OPEN, CONTAINED, INVESTIGATING, RECOVERING, RESOLVED, CLOSED.

## 31. Efeito externo

Banco não torna uma chamada externa atômica. Toda ação externa material usa:

~~~text
PERSIST EFFECT_INTENT with idempotency key
→ authorize/gate
→ execute
→ observe
→ reconcile ambiguous timeout
→ PERSIST outcome
~~~

Timeout produz UNKNOWN_OUTCOME até reconciliação. Nunca dispara repetição cega de efeito irreversível.

## 32. Erros

Categorias mínimas:

~~~text
VALIDATION_ERROR
AUTHENTICATION_FAILED
AUTHORIZATION_DENIED
HUMAN_GATE_REQUIRED
IDEMPOTENCY_CONFLICT
VERSION_CONFLICT
STALE_GENERATION
LEASE_EXPIRED
POLICY_VERSION_MISMATCH
STATE_TRANSITION_DENIED
EXTERNAL_DEPENDENCY_UNAVAILABLE
TIMEOUT
UNKNOWN_OUTCOME
INTEGRITY_VIOLATION
RESOURCE_EXHAUSTED
INTERNAL_ERROR
~~~

Cada erro declara retryable verdadeiro ou falso. Credencial inválida, permissão negada, dado inválido e conflito permanente não recebem retry automático.

## 33. Versionamento

- schemas seguem major.minor;
- major quebra compatibilidade;
- minor adiciona campo opcional ou valor negociável;
- produtor e consumidor declaram versões;
- federação recusa major incompatível;
- eventos históricos mantêm schema_version original;
- migração nunca reescreve evidência original.

## 34. Retenção e exclusão

Policy define retenção por classe. Exclusão:

- exige autorização;
- produz tombstone e audit record;
- respeita obrigação legal;
- não deixa segredo em backup sem política;
- não apaga cadeia necessária a ProofVerdict ainda válido.

## 35. Progresso

ProgressEvent precisa apontar ao menos um:

- acceptance criterion satisfeito;
- dependência fechada;
- teste aprovado;
- falha eliminada;
- risco reduzido;
- artefato promovido;
- incerteza relevante resolvida;
- gate avançado.

Heartbeat, log e tentativa não aumentam progresso por si.

## 36. Critérios de aceite

Este contrato somente pode ser considerado implementado quando:

- schemas executáveis correspondem às entidades;
- transições inválidas falham;
- mutação atômica passa por falhas injetadas;
- outbox recupera após restart;
- comando duplicado não duplica efeito;
- ProofVerdict obsoleto falha;
- stale generation falha no commit;
- isolamento multiprojeto passa;
- monotonic não é persistido;
- portões são distinguíveis;
- Read Model é reconstruído;
- Event/State integrity gate passa.
