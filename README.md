# POD — Plataforma Orquestradora Durável

O POD é uma Plataforma Orquestradora Durável, soberana e multiprojeto. Recebe objetivos humanos e assume a complexidade técnica necessária até produzir resultados funcionais, integrados, seguros, recuperáveis, documentados e comprovados.

## Raiz canônica

A branch canônica é `main`.

A ordem operacional de leitura é:

1. [`POD_DOCUMENTACAO_CONSOLIDADA_CANONICA.md`](POD_DOCUMENTACAO_CONSOLIDADA_CANONICA.md) — arquitetura consolidada;
2. [`POD_BASELINE_CANONICA_AQUISICAO_EVOLUCAO_HIGIENE.md`](POD_BASELINE_CANONICA_AQUISICAO_EVOLUCAO_HIGIENE.md) — aquisição, evolução e higiene;
3. [`POD_RECONCILIACAO_CANONICA_F1_2026-10-05.md`](POD_RECONCILIACAO_CANONICA_F1_2026-10-05.md) — fechamento F1 e reconciliação concorrente;
4. [`ADR/`](ADR/) — decisões arquiteturais posteriores;
5. [`SCHEMAS/`](SCHEMAS/) e [`CONTRACTS/`](CONTRACTS/) — contratos formais;
6. [`STANDARDS/`](STANDARDS/) — normas transversais;
7. [`RUNBOOKS/`](RUNBOOKS/), [`EVIDENCE/`](EVIDENCE/) e [`RELEASES/`](RELEASES/) — operação, prova e releases;
8. [`HISTORY/`](HISTORY/) — histórico com `NORMATIVE=false`.

Nenhuma branch de trabalho substitui `main` como fonte canônica após promoção e validação.

## Estado atual desta reconciliação

- Fase 0 — `BASELINE_RECONCILED`: comprovada.
- Fase 1 — `CORE_CONTRACTS_DEFINED`: comprovada no escopo contratual/formal anterior.
- Hardening F1 de 05/10/2026: candidato até CI do commit convergente e de `main`.
- Fase 2 — `MVP_PROVEN`: **não iniciada**.
- Runtime do POD, Privacy Kernel, ADE, Execution Fabric e Capability Engine: **não implementados**.

Documento, aquisição de referência, contrato e modelo formal não são prova de runtime.

## Contratos F1 endurecidos

A base versionada contém:

- `SCHEMAS/v1/pod.proto` — contratos F1 originais;
- `SCHEMAS/v1/pod_hardening.proto` — prova, Privacy/Sensitive Data, ADE, fencing e Execution Fabric;
- `SCHEMAS/v1/pod_capability.proto` — Capability Engine;
- JSON Schemas para estado de missão, contratos de módulo, `DataPolicyEnvelope`, `PrivacyDecision`, `ProofVerdict` e `CapabilityVersion`;
- TLA+ para missão, gates de prova, lease/fencing e stale worker.

## Capability acquisition V001

Foram preservados o manifesto e catálogo de 19 referências adquiridas no trabalho concorrente de 05/10. O CI atual revalida estrutura, proveniência declarada e zero donor runtime coupling. A verificação física dos bytes externos permanece evidência histórica; os bytes externos não integram o runtime nem o build.

Isto não muda o estado de aquisição de componentes runtime da Baseline.

## Regra de conclusão

```text
MISSION_GIVEN
→ MISSION_ACCEPTED
→ WORK
→ EVIDENCE
→ ACCEPTANCE
→ REGRESSION
→ CHECKPOINT
→ SECURITY/PRIVACY/RECOVERY GATES
→ FRESH PROOF VERDICT
→ MISSION_PROVEN
```

`MISSION_PROVEN` não pode ser inferido de código escrito, build verde, processo rodando, endpoint disponível, commit, painel ou texto de IA.

## REUSE FIRST

```text
PESQUISAR
→ ANALISAR
→ COMPARAR
→ SELECIONAR
→ ADQUIRIR
→ SANITIZAR
→ NORMALIZAR E QUALIFICAR
→ CONTEXTUALIZAR
→ VALIDAR
→ CONTRATUALIZAR
→ INTEGRAR
→ PROVAR
→ CONSTRUIR SOMENTE O DIFERENCIAL AUSENTE
```

## Validar

```bash
python3 scripts/validate_governance.py
python3 scripts/validate_contracts.py
python3 scripts/validate_capability_acquisition.py
python3 scripts/validate_formal.py
python3 -m unittest discover -s tests -v
```

O GitHub Actions executa os mesmos gates.

## Próxima fase

Somente depois desta reconciliação estar verde e promovida à `main`, uma nova missão pode iniciar a **Fase 2 — fatia vertical mínima**. Esta missão não inicia F2.
