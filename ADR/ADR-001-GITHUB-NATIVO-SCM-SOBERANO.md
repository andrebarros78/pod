# ADR-001 — GitHub nativo e SCM soberano do POD

**Status:** ACCEPTED  
**Data:** 2026-10-03  
**Autoridade:** decisão explícita do Owner  
**Repositório canônico:** `https://github.com/andrebarros78/pod`

## Contexto

O POD precisa nascer com uma fonte canônica, durável, auditável e independente da memória de conversas ou de máquinas individuais.

## Decisão

O GitHub é o SCM nativo do POD.

1. O repositório `andrebarros78/pod` é a origem canônica do código e dos artefatos versionados de engenharia.
2. `main` representa a linha integrada; construção ocorre em branches e integra por revisão/merge controlado.
3. Pull requests, checks, tags e releases fazem parte do mecanismo de integração e rastreabilidade.
4. O Governador define a política soberana de Git; executores não escolhem autonomamente branch, merge, force-push, tag ou rollback.
5. Estado operacional de missão não é delegado ao GitHub. `MISSION_STATE.json` é um artefato persistente de continuidade da construção, mas o futuro runtime do POD manterá seu estado operacional próprio conforme a especificação.
6. GitHub não é autoridade sobre `MISSION_PROVEN`; é infraestrutura de SCM e evidência de integração.
7. Alterações destrutivas de histórico são proibidas por padrão. Force-push exige decisão explícita e verificação do remoto.
8. Nenhum sistema doador é dependência estrutural do repositório ou do runtime final.

## Consequências

- Toda construção passa a ter commit identificável e remoto GitHub correspondente.
- CI do GitHub valida a governança e, progressivamente, contratos, Rust, testes, segurança e integração.
- O POD pode ser reconstruído a partir do repositório e de dependências declaradas, sem depender da conversa atual.
