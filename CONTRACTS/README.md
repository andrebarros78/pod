# Contratos POD

A Fase 1 separa contrato de implementação.

Contratos versionados executáveis:

- `SCHEMAS/v1/pod.proto` — baseline v1;
- `SCHEMAS/v1/pod_hardening.proto` — prova, privacy, ADE, fencing e Execution Fabric;
- `SCHEMAS/v1/pod_capability.proto` — Capability Engine, avaliação e promoção;
- `SCHEMAS/v1/mission_state.schema.json`;
- `SCHEMAS/v1/module_contract.schema.json`;
- `SCHEMAS/v1/data_policy_envelope.schema.json`;
- `SCHEMAS/v1/privacy_decision.schema.json`;
- `SCHEMAS/v1/proof_verdict.schema.json`;
- `SCHEMAS/v1/capability_version.schema.json`.

A existência, compilação e model checking desses contratos não significam que Governador, ADE, Execution Fabric, Privacy Kernel ou Capability Engine estejam implementados em runtime.
