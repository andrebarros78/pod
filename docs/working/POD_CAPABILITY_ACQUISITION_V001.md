# POD — AQUISIÇÃO CONTROLADA DE CAPACIDADES — V001

**Identificador:** POD-WORK-CAP-002
**Versão:** 1.0.0
**Status:** REFERENCE_ONLY
**Data:** 2026-09-03
**Aquisição:** POD-CAPABILITY-ACQUISITION-V001

## Resultado

Foram adquiridas e normalizadas **19 capacidades** selecionadas a partir de SkillsMP e LobeHub.

~~~text
FONTES GITHUB PINADAS             = 14
PACOTES LOBEHUB PINADOS POR HASH = 5
CONTEÚDO DONOR COPIADO AO RUNTIME = 0
DEPENDÊNCIA DONOR DE RUNTIME      = 0
CAPACIDADES NORMALIZADAS          = 19
~~~

Os arquivos externos permanecem fora do repositório operacional, em área de aquisição separada. O POD preserva somente proveniência, hashes, comportamento absorvido e contrato nativo.

## Política de licença

- fontes MIT/Apache-2.0: podem ser estudadas e reimplementadas respeitando licença e atribuição quando houver cópia substancial;
- pacotes LobeHub sem licença explícita no pacote baixado: **nenhum conteúdo verbatim é incorporado**; somente comportamento/ideia é normalizado de forma independente;
- catálogo não é dependência e não é autoridade.

## Artefatos

- [Manifesto de fontes](capability-acquisition/POD_CAPABILITY_SOURCE_MANIFEST_V001.json)
- [Catálogo nativo](capability-acquisition/POD_CAPABILITY_CATALOG_V001.md)
- [ADR-011](../adr/ADR-011-CAPABILITY-ENGINE-AQUISICAO-PROGRESSIVA-E-EVOLUCAO-GOVERNADA.md)

## Próximo uso

A implementação física ocorrerá nas fases F6 e F11 do Plano Mestre. Até lá, os requisitos e testes associados permanecem `DEFINED_NOT_IMPLEMENTED` / `PLANNED`.
