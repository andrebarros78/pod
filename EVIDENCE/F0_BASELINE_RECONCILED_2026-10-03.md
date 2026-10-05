# F0 — Baseline reconciliada

**Resultado:** `BASELINE_RECONCILED`  
**Data:** 2026-10-03  
**Branch:** `build/pod-foundation-v001`

## Evidências

- Repositório canônico acessível: `https://github.com/andrebarros78/pod`.
- Branch de construção criada e publicada no remoto.
- Commit inicial da baseline: `f6321a7`.
- Correção de diretórios não versionados: `1d889f0`.
- Validador local: `POD_GOVERNANCE_VALID`.
- Regressão local: 4 testes, 0 falhas.
- GitHub Actions run `37118657966`: FAILURE esperado que revelou diretórios vazios não versionados pelo Git.
- Causa raiz corrigida com marcadores versionados nos diretórios obrigatórios.
- GitHub Actions run `37118761427`: SUCCESS.
- DOCSET anterior preservado em `HISTORY/DOCSET_V004/` com `NORMATIVE=false`.
- Fonte normativa única atual: `POD_PROJETO_CONSOLIDADO.md`.

## Gate F0

`documentos concorrentes = 0` para a linha atual de construção: PASS por governança do repositório e isolamento do material anterior em HISTORY.
