# POD — PRIVACY/LGPD E SENSITIVE DATA STANDARD — V001

**Status:** ACTIVE  
**Data-base:** 05/10/2026  
**Autoridade:** norma transversal especializada da Baseline canônica POD  
**Origem reconciliada:** `POD_DOCSET_V005_SENSITIVE_DATA_SECURITY_RECONCILIADO`, especialmente `POD_PRIVACY_LGPD_KERNEL_E_PRIVACY_GATE_V002.md`, ADRs de Privacy Gate e Sensitive Data Security.  
**Implementação comprovada:** NÃO  
**Princípio:** `NO_PRIVACY_GATE = NO_DATA_OPERATION`  
**Modo:** `FAIL_CLOSED`

## 0. Finalidade

Este documento absorve na linha canônica atual, sem regredir as decisões posteriores de 13/09 e 03/10, os requisitos de Privacy/LGPD e Sensitive Data do DOCSET V005 anexado pelo Owner.

Ele não substitui a arquitetura soberana, o Governador, o ADE, o Execution Fabric ou a política geral de segurança. Ele especializa qualquer caminho de dados pessoais/sensíveis.

## 1. Invariantes

```text
NO_PRIVACY_GATE = NO_DATA_OPERATION
PRIVACY_GATE_BYPASS = ARCHITECTURAL_VIOLATION
UNKNOWN_PURPOSE = DENY
UNKNOWN_POLICY = DENY
UNKNOWN_DESTINATION = DENY
UNKNOWN_PROCESSOR_FOR_PERSONAL_DATA = DENY
UNAUTHORIZED_CROSS_PROJECT_ACCESS = DENY
EXTERNAL_AI_WITH_UNAPPROVED_PERSONAL_DATA = DENY
LOG_SECRET = DENY
LOG_PERSONAL_DATA_WITHOUT_JUSTIFICATION = DENY
RETENTION_UNDEFINED_FOR_PERSISTED_PERSONAL_DATA = DENY
TRANSFER_MECHANISM_REQUIRED_AND_MISSING = DENY
LLM_APPROVAL != PRIVACY_AUTHORIZATION
PRIVILEGED_EXECUTION != PRIVACY_BYPASS
```

Security Gate e Privacy Gate são independentes e cumulativos.

## 2. Operações cobertas

O Privacy Gate se aplica, conforme relevância, a:

`COLLECT`, `RECEIVE`, `CLASSIFY`, `READ`, `QUERY`, `JOIN`, `COPY`, `MOVE`, `WRITE`, `UPDATE`, `DELETE`, `ANONYMIZE`, `PSEUDONYMIZE`, `TOKENIZE`, `HASH`, `EMBED`, `INDEX`, `CACHE`, `LOG`, `TRACE`, `EXPORT`, `IMPORT`, `TRANSMIT`, `SHARE`, `PROMPT`, `TOOL_CALL`, `BACKUP`, `RESTORE`, `ARCHIVE`, `REPLICATE`, `SYNC`, `MIGRATE`, `TRAIN_OR_FINE_TUNE` e `GENERATE_DERIVED_DATA`.

## 3. DataPolicyEnvelope

Todo dado governado deve poder ser associado a um `DataPolicyEnvelope`, sem duplicar o conteúdo bruto.

Campos mínimos canônicos:

```text
data_id
project_id
classification
personal_data
sensitive_personal_data
child_or_adolescent_data
subject_category
controller_ref
operator_refs
purpose_refs
authority_refs
source_ref
lineage_ref
retention_policy_ref
allowed_operations
allowed_destinations
allowed_projects
external_processing_allowed
international_transfer_policy_ref
logging_policy
encryption_required
created_at
policy_version
```

A forma executável do contrato está em:

- `SCHEMAS/v1/data_policy_envelope.schema.json`;
- `SCHEMAS/v1/pod_hardening.proto`.

## 4. PrivacyDecision

Toda decisão material do gate deve ser auditável e vinculada ao contexto da operação.

Campos mínimos:

```text
decision_id
project_id
operation_id
data_ids
operation
purpose_id
policy_version
destination_ref
processor_ref
decision
reason_codes
minimization_applied
transformation_refs
expires_at
decided_at
engine_version
```

Resultados permitidos:

```text
allow
deny
require_human_legal_input
```

A LLM pode propor classificação ou apontar ausência de informação, mas não inventa fato jurídico, finalidade, base/autorização ou aprovação.

## 5. Minimização e external AI

Antes de transmissão, log, exportação ou contexto enviado a modelo externo:

```text
FULL_OBJECT
→ NECESSITY ANALYSIS
→ MINIMUM AUTHORIZED VIEW
→ PRIVACY GATE
→ OPERATION
```

External AI deve passar pelo mesmo gate e por adapter POD. Modelo/provedor nunca recebe dados pessoais/sensíveis apenas porque possui capacidade técnica de recebê-los.

## 6. Multiprojeto

Dados e políticas são `project_id` scoped por padrão.

```text
CROSS_PROJECT_DATA_ACCESS
→ explicit authorized sharing contract required
→ otherwise DENY
```

## 7. Sensitive Data Product Profile

Ativação:

```text
DATA_CLASSIFICATION = SENSITIVE
OR
PROJECT_RISK_PROFILE.requires_sensitive_data_controls = true
→ ACTIVATE SENSITIVE_DATA_PRODUCT_PROFILE
```

Controles mínimos quando aplicáveis:

```text
ENCRYPTION_AT_REST = REQUIRED
ENCRYPTION_IN_TRANSIT = REQUIRED_WHEN_APPLICABLE
KEY_MATERIAL_SEPARATE_FROM_DATABASE = REQUIRED
KEY_EXPORT = DENY_BY_DEFAULT
ENCRYPTED_BACKUP = REQUIRED
ENCRYPTED_RESTORE_PATH = REQUIRED
PRIVILEGED_HUMAN_MFA = REQUIRED
CRITICAL_KEY_OPERATION_MFA = REQUIRED
AUDIT_OF_PRIVILEGED_ACCESS = REQUIRED
PRIVACY_GATE = REQUIRED
SECURITY_GATE = REQUIRED
```

MFA protege autoridade humana privilegiada, não cada transação automática do runtime. Serviços usam identidade técnica individual e least privilege.

A chave mestra não pode permanecer em tabela, migration, repositório, imagem de build, configuração comum ou log.

## 8. Backup/restore

```text
BACKUP_SENSITIVE_DATA_PLAINTEXT = FORBIDDEN
RESTORE_WITHOUT_AUTHORIZATION = DENY
RESTORE_WITHOUT_PRIVACY_RECONCILIATION = INVALID
```

Backup sensível herda classificação, retenção, Privacy Gate e Security Gate.

## 9. Release gate

```text
SENSITIVE_DATA = TRUE
AND
(
  ENCRYPTION_AT_REST_PROVEN != TRUE
  OR KEY_SEPARATION_PROVEN != TRUE
  OR PRIVILEGED_MFA_PROVEN != TRUE
  OR ENCRYPTED_BACKUP_PROVEN != TRUE
)
→ SENSITIVE_DATA_SECURITY_GATE = FAIL
→ PROJECT_PROVEN = FALSE
```

Configuração declarada não prova controle. O artefato e o ambiente reais devem ser exercitados.

## 10. Testes mínimos herdados do DOCSET V005

Os IDs a seguir são preservados como requisitos de teste para a futura implementação, conforme aplicabilidade:

```text
POD-TST-PRV-001 unknown purpose denies
POD-TST-PRV-002 unknown policy denies
POD-TST-PRV-003 cross-project access denies
POD-TST-PRV-004 external AI receives only minimized authorized context
POD-TST-PRV-005 secret never reaches logs
POD-TST-PRV-006 personal data redaction occurs before persistence in logs
POD-TST-PRV-007 decision cache invalidates on policy change
POD-TST-PRV-008 restore does not resurrect deleted/blocked data
POD-TST-PRV-009 processor profile expiration blocks transmission
POD-TST-PRV-010 transfer without required mechanism denies
POD-TST-PRV-011 privileged executor cannot bypass privacy
POD-TST-PRV-012 worker direct data path is impossible
POD-TST-PRV-013 lineage covers source→transform→destination
POD-TST-PRV-014 derived data preserves classification when still linkable
POD-TST-PRV-015 subject request cannot expose another subject
POD-TST-PRV-016 incident record retention policy is enforced
POD-TST-PRV-017 privacy gate failure fails closed
POD-TST-PRV-018 policy decision evidence is tamper-evident
POD-TST-PRV-019 federation routing respects privacy restrictions
POD-TST-PRV-020 memory promotion blocks unsanitized personal data
POD-TST-PRV-021 sensitive data profile activates automatically
POD-TST-PRV-022 database/storage at-rest encryption is effective
POD-TST-PRV-023 plaintext copy/backup of sensitive store is rejected
POD-TST-PRV-024 privileged human database access without MFA is denied
POD-TST-PRV-025 protected access with valid MFA is audited
POD-TST-PRV-026 database master key is absent from DB/repo/log/config-common
POD-TST-PRV-027 key rotation preserves authorized access and invalidates obsolete path
POD-TST-PRV-028 encrypted backup restore requires authorization and privacy reconciliation
```

Nesta Fase 1 esses testes são **contratos futuros**, não alegação de execução do Privacy Kernel.

## 11. Relação com prova

Quando privacidade for aplicável:

```text
MISSION_PROVEN
requires
PRIVACY_GATE_PASS = TRUE
```

Quando Sensitive Data Product Profile for aplicável:

```text
MISSION_PROVEN
requires
SENSITIVE_DATA_SECURITY_GATE_PASS = TRUE
```

O `ProofVerdict` canônico deve carregar explicitamente aplicabilidade e resultado desses gates.

## 12. Estado atual

```text
PRIVACY_STANDARD_RECONCILED = VERIFIED_DOCUMENTALLY
DATA_POLICY_ENVELOPE_CONTRACT = DEFINED
PRIVACY_DECISION_CONTRACT = DEFINED
SENSITIVE_DATA_SECURITY_CONTRACT = DEFINED

PRIVACY_KERNEL_RUNTIME = NOT_IMPLEMENTED
PRIVACY_GATE_RUNTIME = NOT_IMPLEMENTED
SENSITIVE_DATA_SECURITY_RUNTIME = NOT_IMPLEMENTED
PRIVACY_RUNTIME_PROVEN = NO
```
