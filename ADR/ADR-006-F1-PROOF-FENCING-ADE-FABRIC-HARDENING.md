# ADR-006 — Endurecimento F1: prova, fencing, ADE e Execution Fabric

**Status:** ACCEPTED  
**Data:** 2026-10-05  
**Autoridade:** reconciliação código ↔ documentação solicitada pelo Owner

## Contexto

A auditoria de 05/10 encontrou quatro diferenças entre a semântica documentada e os contratos/provas F1:

1. `MISSION_PROVEN` estava modelado formalmente por uma condição de validação simples demais;
2. o modelo de lease/fencing não representava explicitamente token retido por worker antigo;
3. ADE estava arquiteturalmente definido, mas sem contratos F1 próprios;
4. Execution Fabric tinha peças básicas, mas faltavam contratos explícitos de dispatch/ACK/inbox/routing/reconciliation.

## Decisão

### Prova

`MISSION_PROVEN` exige no modelo F1:

```text
evidence_complete
acceptance_pass
regression_pass
checkpoint_present
security_gate_pass
recovery_pass
donor_decoupling_pass
project_isolation_pass
privacy_gate_pass when applicable
sensitive_data_security_gate_pass when applicable
fresh_proof_verdict
```

### Fencing

Cada worker pode reter o token que recebeu. Escrita autorizada exige simultaneamente:

```text
current_lease_holder == worker
worker_presented_token == current_fencing_token
```

Token antigo não pode alterar `resourceVersion`.

### ADE

Ficam definidos contratos explícitos para inspeção, plano, changeset, teste, diagnóstico, tentativa de correção, regressão, checkpoint e `ADEProof`.

### Execution Fabric

Ficam definidos contratos explícitos para `DispatchEnvelope`, `DispatchAck`, `InboxRecord`, `RouteDecision`, `CapabilitySnapshot` e `ReconciliationRecord`.

## Consequências

F1 passa a expressar de forma verificável os invariantes que a documentação já exigia, sem alegar que o runtime existe.

## Migração

Os contratos são aditivos em `SCHEMAS/v1/pod_hardening.proto`; o modelo TLA+ é endurecido sem alterar a fase do projeto.

## Rollback

Somente por ADR posterior com prova equivalente ou superior.

## Segurança

Fencing, Privacy Gate, Security Gate e escopo de autorização permanecem fail closed.

## Compatibilidade

`pod.proto` permanece preservado. Consumidores atuais podem continuar compilando o contrato original; novos consumidores podem importar o hardening.

## Evidência

- compilação dos dois `.proto`;
- validação dos JSON Schemas;
- testes negativos de ProofVerdict e DataPolicyEnvelope;
- TLC sem violação dos invariantes.

## Condição de revisão

Revisar ao implementar a primeira fatia vertical da Fase 2.

## Documentos relacionados

- `formal/PODCore.tla`
- `formal/PODCore.cfg`
- `SCHEMAS/v1/pod_hardening.proto`
- `SCHEMAS/v1/proof_verdict.schema.json`
