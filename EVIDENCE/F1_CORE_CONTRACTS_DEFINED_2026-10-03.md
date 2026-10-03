# F1 — Contratos e modelo formal do núcleo

**Resultado:** `CORE_CONTRACTS_DEFINED`  
**Data:** 2026-10-03  
**Branch:** `build/pod-foundation-v001`

## Contratos

- Protobuf v1 compilado com `protoc`: PASS.
- JSON Schema `mission_state.schema.json`: PASS.
- JSON Schema `module_contract.schema.json`: PASS.
- `MISSION_STATE.json` validado contra schema: PASS.
- Contratos mínimos B4 presentes no Protobuf: PASS.
- `ArmDescriptor` incluído para capacidade lógica dos 32 braços especialistas.

## Modelo formal

Ferramenta: TLA+ tools v1.7.4, SHA-256 fixado no repositório.

Resultado TLC:

- 2.573 estados gerados;
- 495 estados distintos;
- profundidade 13;
- 0 estados restantes na fila;
- `No error has been found`;
- `POD_FORMAL_VALID`.

Invariantes verificados no modelo mínimo:

- `MissionProvenRequiresValidation`;
- `FencingMonotonicModel`;
- `StaleWritesAreDenied`;
- `NoTwoLeaseHolders`;
- `TypeOK`.

## Regressão

- Suíte local: 7 testes, 0 falhas.
- GitHub Actions run `37119405072`: SUCCESS.
- Job `integrity`: governança, contratos, TLC e regressão concluídos com sucesso em runner limpo.

## Gate F1

`schemas versionados` = PASS  
`modelo sem violação de invariantes` = PASS
