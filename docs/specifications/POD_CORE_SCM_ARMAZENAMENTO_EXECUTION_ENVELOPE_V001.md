# POD — ESPECIFICAÇÃO DE CORE, SCM, ARMAZENAMENTO E EXECUTION ENVELOPE — V001

**Identificador:** POD-DOC-013
**Versão:** 1.0.0
**Status:** ACTIVE
**Data:** 2026-09-13
**Conjunto alvo:** POD-DOCSET-V004
**Autoridade:** A2 — especificação normativa
**Decisão:** ADR-010
**Implementação comprovada:** NÃO

## 1. Finalidade

Complementar POD-DOC-006 sem reescrever contratos já estáveis, definindo os novos contratos necessários para Core selado, SCM, classificação de persistência, armazenamento endereçado por conteúdo e Execution Envelope.

## 2. PersistenceClass

Todo registro/arquivo/objeto persistente governado pelo POD declara uma das classes:

~~~text
DURABLE
RECONSTRUCTIBLE
EPHEMERAL
~~~

Campos mínimos de metadado quando aplicável:

~~~text
persistence_class
owner_scope
project_id optional
mission_id optional
created_at_utc
retention_policy_ref
content_hash optional
producer
schema_version
~~~

`RECONSTRUCTIBLE` exige `source_refs` suficientes para reconstrução.
`EPHEMERAL` exige TTL, lifecycle ou regra de encerramento.

## 3. CoreRelease

~~~text
core_release_id
version
package_hash
manifest_ref
schema_compatibility
build_provenance
created_at_utc
verified_at_utc optional
status
~~~

Estados:

~~~text
BUILT
VERIFYING
VERIFIED
ACTIVE
ROLLBACK_READY
REJECTED
SUPERSEDED
REVOKED
~~~

Somente `VERIFIED` ou `ROLLBACK_READY` pode ser promovido para `ACTIVE`.

## 4. ExecutionEnvelope

~~~text
execution_envelope_id
mission_id
project_id
objective_version
policy_version
allowed_capabilities
security_scope
resource_budget_ref
workspace_policy_ref
retention_policy_ref
timeout_policy_ref
rollback_policy_ref
evidence_policy_ref
knowledge_policy_ref
integration_policy_ref
created_at_utc
expires_at_utc optional
version
status
~~~

Estados:

~~~text
CANDIDATE
VALIDATED
ACTIVE
SUSPENDED
SUPERSEDED
EXPIRED
REVOKED
~~~

Nenhum Worker ou Engine amplia capabilities, budget, effect class, integration access ou retention.

## 5. KnowledgeCandidate

~~~text
knowledge_candidate_id
project_id optional
mission_id optional
source_refs
evidence_refs
statement
proposed_scope
proposed_confidence
freshness_basis
producer
created_at_utc
classification
status
reason_codes
~~~

Estados:

~~~text
CANDIDATE
VALIDATING
ADMITTED
REJECTED
DISPUTED
QUARANTINED
SUPERSEDED
~~~

## 6. CanonicalKnowledge

~~~text
knowledge_id
statement
scope
confidence
freshness_status
support_count
independent_sources
evidence_refs
provenance_refs
valid_from
valid_until optional
last_validated_at
supersedes_knowledge_ids
classification
status
ledger_head_ref
created_at_utc
updated_at_utc
~~~

Estados de participação cognitiva:

~~~text
ACTIVE
DISPUTED
SUSPENDED
SUPERSEDED
REVOKED
QUARANTINED
DEPRECATED
~~~

Somente ACTIVE é elegível por padrão para retrieval produtivo.

## 7. KnowledgeLedgerEvent

~~~text
knowledge_event_id
knowledge_id
event_type
previous_status optional
new_status optional
scope_snapshot
confidence_snapshot
freshness_snapshot
evidence_refs
actor_id
reason_codes
occurred_at_utc
payload_hash
~~~

Append-only.

## 8. Confidence

`confidence` expressa força da sustentação. Não é reduzida automaticamente apenas pela passagem do tempo.

Alteração de confidence exige evento de ledger com justificativa e referências.

## 9. Freshness

Valores mínimos:

~~~text
CURRENT
REVALIDATION_DUE
EXPIRED
UNKNOWN
~~~

Política de retrieval pode exigir CURRENT conforme risco da missão.

## 10. KnowledgeScope

Escopo suporta composição:

~~~text
global optional boolean
platform optional string
project_id optional UUIDv7
environment optional string
operating_system optional string
component optional string
version_range optional string
valid_from optional timestamp
valid_until optional timestamp
constraints optional object
~~~

`global=true` exige gate reforçado e evidência compatível com generalização.

## 11. KnowledgeAdmissionDecision

~~~text
admission_decision_id
knowledge_candidate_id
provenance_check
evidence_check
sensitive_filter_check
deduplication_check
contradiction_check
scope_validation
confidence_assignment
decision
reason_codes
knowledge_id optional
created_at_utc
policy_version
~~~

Decision:

~~~text
ADMIT
REJECT
QUARANTINE
DISPUTE
MERGE_AS_REINFORCEMENT
REQUEST_MORE_EVIDENCE
~~~

## 12. RevalidationRequest

~~~text
revalidation_request_id
knowledge_id
trigger_type
trigger_ref optional
risk_class
requested_at_utc
deadline_at_utc optional
status
result_ref optional
~~~

Trigger:

~~~text
TIME
VERSION_CHANGE
API_CHANGE
OS_CHANGE
DEPENDENCY_CHANGE
CONFIG_CHANGE
CONTRADICTION
HIGH_RISK_USE
MANUAL
~~~

## 13. Projeções cognitivas

Projection record mínimo:

~~~text
projection_id
projection_type
source_knowledge_version
source_hash
build_version
built_at_utc
status
~~~

Tipos:

~~~text
VECTOR
LEXICAL
KNOWLEDGE_GRAPH
HOT_CONTEXT
ANALYTICS
READ_MODEL
~~~

Todos são `RECONSTRUCTIBLE`.

## 14. EvidenceObject por conteúdo

Objeto físico:

~~~text
content_hash
size_bytes
media_type
storage_ref
integrity_status
created_at_utc
~~~

Referência lógica continua contendo:

~~~text
evidence_id
project_id
mission_id
classification
retention_policy_ref
provenance
content_hash
~~~

Bytes idênticos podem apontar para o mesmo objeto físico. Metadata de ownership e autorização nunca é deduplicada de forma a fundir escopos.

## 15. Garbage Collection

Um objeto CAS só pode ser removido quando:

~~~text
durable_reference_count == 0
AND legal_hold == false
AND retention_deadline <= now
AND recovery_window_expired == true
AND integrity_reconciliation == PASS
~~~

GC gera evento e auditoria.

## 16. Eventos adicionais

~~~text
core.release_built
core.release_verified
core.release_activated
core.release_rollback
core.integrity_failed

execution_envelope.created
execution_envelope.validated
execution_envelope.suspended
execution_envelope.revoked

knowledge.candidate_created
knowledge.distillation_requested
knowledge.admitted
knowledge.rejected
knowledge.reinforced
knowledge.disputed
knowledge.superseded
knowledge.suspended
knowledge.revoked
knowledge.revalidation_requested
knowledge.revalidated

storage.object_stored
storage.reference_added
storage.reference_removed
storage.object_gc_eligible
storage.object_deleted
storage.integrity_failed
~~~

## 17. Gates obrigatórios

### Core

~~~text
CORE_INTEGRITY
CORE_SIZE_DRIFT
CORE_DIRTY_FILES
PROJECT_FILES_IN_CORE
MISSION_FILES_IN_CORE
REGENERABLE_DATA_IN_CORE
UNEXPECTED_RESIDUE
~~~

### SCM

~~~text
PROVENANCE_PRESENT
EVIDENCE_SUFFICIENT
SENSITIVE_CONTENT_FILTERED
DEDUPLICATION_RESOLVED
CONTRADICTION_RESOLVED_OR_MARKED
SCOPE_VALID
CONFIDENCE_ASSIGNED
FRESHNESS_ASSIGNED
LEDGER_EVENT_PERSISTED
~~~

### Storage

~~~text
HASH_VERIFIED
OWNERSHIP_PRESERVED
RETENTION_APPLIED
GC_REFERENCES_ZERO
~~~

## 18. Métricas

~~~text
SCM_TOTAL_SIZE
SCM_OBJECT_COUNT
SCM_GROWTH_RATE
DUPLICATION_RATIO
STALE_KNOWLEDGE_RATIO
UNVALIDATED_CANDIDATES
REVALIDATION_BACKLOG
CAS_PHYSICAL_BYTES
CAS_LOGICAL_BYTES
CAS_DEDUP_SAVINGS_BYTES
EPHEMERAL_RESIDUE_BYTES
CORE_RELEASE_SIZE
CORE_SIZE_DRIFT
~~~

## 19. Critérios de prova

Esta especificação não é considerada implementada enquanto os testes não demonstrarem:

- candidato sem evidência não é admitido;
- candidato sem escopo não é admitido;
- contradição não destrói versão anterior;
- revogação retira item do retrieval padrão;
- projeções podem ser apagadas e reconstruídas;
- objeto CAS corrompido é detectado;
- GC não remove objeto ainda referenciado;
- Execution Envelope bloqueia ampliação de capability;
- Core retorna a zero resíduo após execução de teste;
- rollback de release preserva estado externo.
