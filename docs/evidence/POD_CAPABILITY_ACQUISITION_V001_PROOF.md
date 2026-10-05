# POD — PROVA DA AQUISIÇÃO CONTROLADA DE CAPACIDADES — V001

**Identificador:** POD-EVID-CAP-001
**Versão:** 1.1.0
**Status:** EVIDENCE_ONLY
**Data:** 2026-10-05 13:16 BRT
**Aquisição:** POD-CAPABILITY-ACQUISITION-V001
**Branch de selagem:** `pod-capability-acquisition-v001`

## 1. Escopo provado

Esta evidência sela a aquisição controlada das capacidades selecionadas a partir de SkillsMP e LobeHub e verifica que as fontes foram preservadas com proveniência e hashes, sem introduzir dependência de runtime nos projetos doadores.

## 2. Resultado da prova física das fontes

Comando executado:

~~~text
C:\Python313\python.exe scripts\validate_capability_acquisition.py --source-root C:\New Projet\POD-ACQUISITION-SOURCES
~~~

Resultado observado:

~~~text
POD_CAPABILITY_ACQUISITION_VALID
sources=19
github_pinned=14
marketplace_pinned=5
donor_runtime_coupling=0
external_sources_verified=true
~~~

Critérios comprovados:

- 19 capacidades registradas;
- 14 fontes GitHub pinadas por commit e hash;
- 5 pacotes LobeHub pinados por hash;
- fontes externas verificadas fisicamente contra o manifesto;
- nenhum conteúdo LobeHub sem licença explícita foi copiado verbatim para o runtime;
- `donor_runtime_coupling=0`.

O detalhamento por capability, repositório/pacote, commit, licença e SHA-256 está em `docs/working/capability-acquisition/POD_CAPABILITY_SOURCE_MANIFEST_V001.json`.

## 3. Integridade do docset

O manifesto canônico foi regenerado após a última alteração documental, eliminando a divergência residual de hashes detectada durante a selagem.

Resultado observado após regeneração:

~~~text
POD_DOCSET_VALID
document_set_id=POD-DOCSET-V003
documents=20
requirements=137
set_hash=sha256:59fc974c267714b081ca10f9c2be8d5c7e9166e89d21be5d7417a4b9e8c1d9b5
~~~

## 4. Capacidades normalizadas

A aquisição inclui capacidades POD-native para:

- criação, eval e versionamento de capabilities;
- debugging sistemático por causa-raiz;
- verificação fresca antes de conclusão;
- ledger durável para Workers;
- revisão independente de código;
- TDD;
- isolamento com Git worktrees;
- memória híbrida;
- continuação autônoma;
- workflow com quality gates;
- execução paralela governada;
- teste real em navegador/DevTools;
- automação por navegador;
- dispatch por domínio independente;
- performance/load/stress;
- execução de projeto com checkpoints;
- análise de logs e traces;
- evolução governada de capabilities;
- autoauditoria de segurança.

## 5. Invariantes preservados

~~~text
CAPABILITY_ENGINE_IS_POD_NATIVE = TRUE
EXTERNAL_SKILL_IS_REFERENCE_INPUT_ONLY = TRUE
PROGRESSIVE_CAPABILITY_LOADING = TRUE
CAPABILITY_PROMOTION_REQUIRES_EVAL = TRUE
CAPABILITY_CANNOT_EXPAND_AUTHORITY = TRUE
DONOR_RUNTIME_COUPLING = ZERO
SELF_EVOLUTION_WRITES_CANDIDATE_ONLY = TRUE
UNLICENSED_SOURCE_CONTENT_NOT_COPIED = TRUE
~~~

## 6. Critério de conclusão desta aquisição

A aquisição documental e de conhecimento é considerada comprovada quando, no mesmo estado versionado:

1. a prova física das 19 fontes passa;
2. o docset retorna `POD_DOCSET_VALID`;
3. a suíte de regressão passa integralmente;
4. `git diff --check` não encontra erro estrutural;
5. o commit é publicado no repositório oficial;
6. `main` contém o commit de selagem sem carregar alterações posteriores não pertencentes ao escopo.

A implementação runtime das capacidades permanece sujeita às fases F6/F11 e aos requisitos `REQ-CAP-*`; esta evidência não declara esses requisitos como implementados.

## 7. Reconciliação com o DOCSET V004 — 2026-10-05

A publicação foi retomada sobre o `main` remoto real, que continha o DOCSET V004 e uma decisão arquitetural `ADR-010` posterior à aquisição local. Para eliminar colisão de identidade sem apagar a decisão remota:

- `ADR-010` permanece reservado a Core selado, SCM soberano e separação de estado;
- a decisão de Capability Engine foi reconciliada como `ADR-011`;
- requisitos `REQ-CAP-*`, índices, validadores e arquitetura atual foram atualizados para o novo identificador;
- o Capability Engine passou a fazer parte do DOCSET V004 ativo;
- nenhuma fonte doadora ganhou autoridade ou dependência de runtime.

Provas observadas no mesmo worktree reconciliado:

~~~text
POD_DOCSET_VALID
V003_COMPAT_EXIT=0
set_hash=sha256:59fc974c267714b081ca10f9c2be8d5c7e9166e89d21be5d7417a4b9e8c1d9b5

POD_DOCSET_V004_VALID
V004_EXIT=0

POD_CAPABILITY_ACQUISITION_VALID
sources=19
github_pinned=14
marketplace_pinned=5
donor_runtime_coupling=0
external_sources_verified=true

UNIT TESTS: 11/11 PASS
DIFF CHECK: PASS
~~~

A aquisição somente pode ser declarada `MISSION_PROVEN` após o commit reconciliado ser publicado no `main` remoto e relido pelo canal GitHub.
