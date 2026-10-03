# ADR-004 — ADE e runtime especializado de agente isolado

**Status:** ACCEPTED
**Data:** 2026-10-03
**Autoridade:** decisão do Owner materializada na documentação consolidada v4

## Contexto

A documentação v4 explicita o ADE — Executor Autônomo de Desenvolvimento e Correção — e revisa a regra anterior que restringia toda orquestração a Rust.

## Decisão

1. O **ADE** passa a existir explicitamente na arquitetura como executor autônomo de engenharia sob autoridade do POD.
2. O ADE não é Governador, não altera soberania e não declara prova.
3. Runtime especializado de agente pode existir em processo isolado fora do núcleo, desde que:
   - não toque diretamente o núcleo;
   - opere por contratos POD;
   - seja substituível;
   - não seja fonte única de verdade ou prova;
   - respeite autorização, segurança, observabilidade e recovery.
4. Rust permanece a direção do núcleo/Governador, Execution Fabric e executores nativos conforme a documentação consolidada.
5. A abertura para runtime especializado não autoriza implementação ou aquisição automática de um produto específico.

## Consequência

Seleção de agente, framework ou componente externo passa pelo pipeline `REUSE FIRST` e pelos gates de aquisição, qualificação e integração antes de entrar no runtime operacional.
