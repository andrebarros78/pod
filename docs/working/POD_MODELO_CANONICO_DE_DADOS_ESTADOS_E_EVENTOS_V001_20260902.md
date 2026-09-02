# POD — MODELO CANÔNICO DE DADOS, ESTADOS E EVENTOS — V001

**Data:** 02/09/2026  
**Status:** WORKING / NON-NORMATIVE  
**Base:** Projeto Conceitual Reconsolidado + Contratos Conceituais V001  
**Escopo:** entidades lógicas, identidades, estados, eventos, consistência, ordenação e rastreabilidade; sem escolha de banco ou tecnologia física.

---

# 0. PRINCÍPIOS

```text
STATE != PROCESS
COMMAND != EVENT
EVENT != CURRENT STATE
ATTEMPT != MISSION
CONNECTION != EXECUTION
CACHE != SOURCE OF TRUTH
```

Regra de mutação:

```text
VALIDAR
→ PERSISTIR
→ COMMIT
→ EVENTO
→ CONFIRMAR
```

Entrega distribuída:

```text
AT-LEAST-ONCE
+ IDEMPOTENCY
+ DEDUP
+ RECONCILIATION
```

Não se assume `exactly-once` de transporte.

---

# 1. IDENTIDADES SOBERANAS

Entidades mínimas:

```text
pod_id
project_id
mission_id
work_unit_id
task_id
attempt_id
command_id
event_id
checkpoint_id
evidence_id
artifact_id
incident_id
approval_id
node_id
worker_id
lease_id
provider_id
model_id
learning_id
training_id
note_id
correlation_id
```

Regras:

- IDs são imutáveis;
- não são reutilizados;
- PID, hostname, nome de arquivo ou título não substituem identidade soberana;
- toda entidade mutável possui versão/sequence quando aplicável;
- toda execução distribuída relevante possui `generation` e fencing quando houver ownership.

---

# 2. ESCOPOS

Todo ativo lógico recebe escopo explícito:

```text
GLOBAL_POD
PROJECT:<project_id>
MISSION:<mission_id>
NODE_LOCAL:<node_id>
PRIVATE
SECRET
TRAINING_ELIGIBLE
```

Regra:

```text
PROJECT_SCOPE_IS_EXPLICIT = TRUE
```

Nenhuma credencial, conhecimento privado, artefato ou estado atravessa projeto implicitamente.

---

# 3. ENTIDADE PROJECT

Campos conceituais:

```text
project_id
name
status
priority
resource_policy
security_classification
active_policy_version
workspace_manifest_ref
created_at
updated_at
```

Estados candidatos:

```text
ACTIVE
PAUSED
ARCHIVED
SUSPENDED_BY_POLICY
```

Uma instalação POD pode conter múltiplos projetos isolados por `project_id`.

---

# 4. ENTIDADE MISSION

Campos:

```text
mission_id
project_id
objective
constraints
acceptance_criteria
policy_version
priority
budget_policy
status
progress_model
current_strategy_ref
created_at
accepted_at
completed_at
```

Estados:

```text
RECEIVED
ACCEPTED
RUNNING
REPLANNING
RECOVERING
PAUSED
WAITING_EXTERNAL
WAITING_FINANCIAL_AUTHORIZATION
PROVING
MISSION_PROVEN
CANCELLED_BY_OWNER
SUPERSEDED
TERMINATED_BY_POLICY
IMPOSSIBLE_PROVEN
REJECTED_BEFORE_ACCEPTANCE
```

Transição raiz:

```text
RECEIVED
→ ACCEPTED
→ RUNNING
→ PROVING
→ MISSION_PROVEN
```

Estados de espera/recovery não removem compromisso de conclusão.

---

# 5. WORK UNIT / TASK

`work_unit` é unidade planejada do DAG; `task` pode representar sua realização durável no runtime. A consolidação normativa futura pode fundir os nomes, mas a diferença conceitual deve permanecer enquanto útil.

Campos:

```text
work_unit_id/task_id
mission_id
project_id
parent_id
dependencies
required_capabilities
priority
critical_path_weight
resource_envelope
security_class
status
assigned_node_id
current_attempt_id
```

Estados candidatos:

```text
PLANNED
BLOCKED_DEPENDENCY
READY
QUEUED
DISPATCHING
RUNNING
WAITING
READY_FOR_TEST
TESTING
READY_FOR_INTEGRATION
INTEGRATING
SUCCEEDED
FAILED_ATTEMPT_PENDING_RECOVERY
CANCELLED
SUPERSEDED
```

Falha de uma tentativa não implica estado terminal da missão.

---

# 6. ATTEMPT

Campos:

```text
attempt_id
work_unit_id
mission_id
node_id
worker_id
generation
strategy_fingerprint
started_at
ended_at
status
result_ref
failure_fingerprint
checkpoint_ref
```

Estados:

```text
CREATED
DISPATCHED
ACCEPTED
RUNNING
SUCCEEDED
FAILED
TIMED_OUT
PREEMPTED
FENCED
ABORTED
```

Histórico de tentativas é imutável para fins de auditoria; não se apaga falha para simular sucesso.

---

# 7. COMMAND

Campos:

```text
command_id
correlation_id
mission_id
project_id
work_unit_id
attempt_id
node_id
operation
payload_ref
idempotency_key
policy_version
generation
fencing_token
issued_at
expires_at
status
```

Estados:

```text
CREATED
VALIDATED
PERSISTED
DELIVERING
ACCEPTED
RUNNING
DONE
FAILED
EXPIRED
CANCELLED
FENCED
```

```text
ACK != RESULT
```

Um `DONE` local cujo transporte falhou deve ser reconciliado, não reexecutado cegamente.

---

# 8. EVENT

Campos mínimos:

```text
event_id
aggregate_type
aggregate_id
sequence
generation quando aplicável
event_type
occurred_at_utc
recorded_at_utc
correlation_id
causation_id
payload_ref/hash
```

Regras:

- evento é fato imutável;
- `event_id` identifica;
- `sequence` ordena dentro do agregado;
- `generation` protege ownership quando aplicável;
- evento atrasado de geração obsoleta não pode sobrescrever estado vigente.

---

# 9. CHECKPOINT

Campos:

```text
checkpoint_id
mission_id
project_id
work_unit_id opcional
node_id opcional
generation
state_manifest_ref
content_hash
created_at
validation_status
replay_metadata
```

Estados:

```text
CANDIDATE
VALIDATING
VALID
INVALID
SUPERSEDED
RESTORED
```

Checkpoint válido deve ser verificável, versionado e reconciliável.

---

# 10. EVIDENCE

Campos:

```text
evidence_id
mission_id
project_id
work_unit_id
attempt_id
command_id
node_id
generation
evidence_type
content_ref
content_hash
provenance
created_at
classification
redaction_status
```

Tipos conceituais:

```text
COMMAND_OUTPUT
TEST_RESULT
STATE_OBSERVATION
FILE_HASH
ARTIFACT_HASH
SCREEN/UX_PROOF quando aplicável
SECURITY_PROOF
RECOVERY_PROOF
PERFORMANCE_PROOF
AUDIT_TRAIL
```

Evidência deve permitir reconstruir a cadeia causal.

---

# 11. ARTIFACT

Campos:

```text
artifact_id
project_id
mission_id
artifact_type
version
content_hash
manifest_ref
producer_attempt_id
status
promotion_proof_ref
created_at
```

Estados:

```text
CANDIDATE
TESTING
VALIDATED
PROMOTED
REJECTED
SUPERSEDED
```

`last-write-wins` não é permitido para artefato crítico.

---

# 12. LEASE / OWNERSHIP / FENCING

Campos:

```text
lease_id
resource_scope
owner_id
generation
fencing_token
issued_at
expires_monotonic_ref
status
```

Invariantes:

```text
ONE_AUTHORITATIVE_GENERATION_PER_MUTABLE_SCOPE = TRUE
STALE_GENERATION_CANNOT_COMMIT = TRUE
```

Estados:

```text
ACTIVE
EXPIRING
EXPIRED
REVOKED
SUPERSEDED
```

---

# 13. NODE

Campos:

```text
node_id
identity_ref
trust_status
protocol_version
agent_version
capabilities
health
resource_snapshot
connection_state
last_seen
```

Ciclo de vida:

```text
JOIN
→ ENROLL
→ TRUST_CHECK
→ COMPATIBILITY_SYNC
→ READY
→ DRAINING
→ LEAVE
→ REVOKED
```

Estados auxiliares:

```text
OFFLINE
DEGRADED
RECOVERING
UPGRADE_REQUIRED
QUARANTINED
```

```text
DISCOVERED_NODE != TRUSTED_NODE
```

---

# 14. PROVIDER / MODEL CAPABILITY

Provider/model são recursos cognitivos, não autoridade.

Campos conceituais:

```text
provider_id
model_id
version_when_available
capabilities
context_limits
health
latency_profile
cost_profile
privacy/data_policy
quality_profile
status
```

Estados:

```text
AVAILABLE
DEGRADED
RATE_LIMITED
AUTH_INVALID
UNAVAILABLE
DISABLED_BY_POLICY
```

---

# 15. APPROVAL / FINANCIAL AUTHORIZATION

Campos:

```text
approval_id
mission_id
project_id
approval_type
requested_action
scope
cost_estimate quando aplicável
requested_at
expires_at
decision
decided_by
```

Estados:

```text
PENDING
APPROVED
REJECTED
EXPIRED
REVOKED
```

Gasto novo sem `APPROVED` válido permanece em `WAITING_FINANCIAL_AUTHORIZATION`.

---

# 16. INCIDENT

Campos:

```text
incident_id
scope
severity
category
trigger_event_id
status
containment_actions
root_cause_ref
recovery_ref
evidence_refs
opened_at
resolved_at
```

Estados:

```text
OPEN
CONTAINING
INVESTIGATING
RECOVERING
VALIDATING
RESOLVED
ACCEPTED_RISK
```

---

# 17. NOTE / BLOCO DE NOTAS

Formato operacional acordado:

```text
note_id = b6c5cd691f7d52707dd64275a2498e7d97xxxxxx
data
nome
project/part
status
texto_original
context_refs
```

Toda nova nota:

```text
STATUS = PENDÊNCIA
```

Evolução possível:

```text
PENDÊNCIA
→ EM_TRATAMENTO
→ RESOLVIDA
```

ou promoção explícita para task, Registro Vivo ou documentação, preservando o ID e a proveniência.

---

# 18. MODELO DE CONSISTÊNCIA POR CLASSE

## STRONG / SERIALIZED

```text
mission verdict
policy version activation
authorization/financial decision
command acceptance
lease/fencing ownership
artifact promotion
proof verdict
```

## CAUSAL / ORDERED PER AGGREGATE

```text
mission/task/attempt events
checkpoints
results
incident lifecycle
```

## EVENTUAL

```text
Read Models
telemetry
capability cache
aggregated health
panel projections
```

## DERIVED / REBUILDABLE

```text
indexes
embeddings
search projections
caches
analytics
```

## EPHEMERAL

```text
process metrics
transient UI state
non-sovereign runtime observations
```

---

# 19. TEMPO

```text
UTC WALL CLOCK
→ auditoria, correlação humana, persistência de datas

MONOTONIC CLOCK
→ duração, timeout, backoff, heartbeat, lease local

SEQUENCE + GENERATION
→ ordem e autoridade distribuída
```

Relógio de parede nunca decide sozinho ownership distribuído.

---

# 20. EVENTOS CANÔNICOS POR FAMÍLIA

Famílias mínimas:

```text
mission.*
project.*
work_unit.*
attempt.*
command.*
checkpoint.*
evidence.*
artifact.*
lease.*
node.*
provider.*
approval.*
incident.*
learning.*
training.*
note.*
proof.*
security.*
resource.*
```

Exemplos:

```text
mission.accepted
mission.replanning
mission.proving
mission.proven
command.accepted
command.completed
attempt.failed
checkpoint.validated
artifact.promoted
node.quarantined
provider.degraded
approval.approved
incident.resolved
proof.rejected
```

---

# 21. PROGRESSO REAL

Atividade não é progresso.

Progresso deve ser derivado de mudanças objetivas como:

```text
critério satisfeito
dependência fechada
teste obrigatório aprovado
falha eliminada ou risco reduzido
incerteza relevante resolvida
artefato promovido
ramo concluído
proof gate avançado
```

Heartbeat, logs ou retries sozinhos não aumentam progresso.

---

# 22. RECONCILIAÇÃO

Na reconexão ou restart:

```text
IDENTIFICAR ESTADO PERSISTIDO
→ COMPARAR sequence/generation
→ RECONCILIAR inbox/outbox/journal
→ DEDUP command_id/idempotency_key
→ PRESERVAR resultados já produzidos
→ INVALIDAR geração obsoleta
→ RECONSTRUIR Read Models
→ RETOMAR
```

---

# 23. GATES DO MODELO CANÔNICO

```text
ID_IMMUTABILITY_GATE
PERSIST_BEFORE_CONFIRM_GATE
EVENT_SEQUENCE_GATE
STALE_GENERATION_REJECT_GATE
IDEMPOTENCY_GATE
PROJECT_SCOPE_ISOLATION_GATE
EVIDENCE_PROVENANCE_GATE
CHECKPOINT_VALIDITY_GATE
ARTIFACT_PROMOTION_GATE
READ_MODEL_REBUILD_GATE
PROGRESS_TRUTH_GATE
```

---

# 24. PRÓXIMO ARTEFATO

Este modelo alimenta:

`POD_ARQUITETURA_TECNICA_DERIVADA_V001_20260902.md`

A tecnologia física continua deliberadamente aberta.