# ADR-003 — REUSE FIRST e pipeline soberano de aquisição

**Status:** ACCEPTED
**Data:** 2026-10-03
**Autoridade:** decisão do Owner materializada na nova Baseline canônica

## Contexto

O POD não deve reconstruir por padrão capacidades maduras que já existam em qualidade adequada. Existência, porém, não equivale a qualificação, integração ou prova.

## Decisão

A evolução do POD adota `REUSE FIRST`.

Fluxo obrigatório quando aplicável:

`PESQUISAR → ADQUIRIR QUANDO VANTAJOSO → SANITIZAR → NORMALIZAR → CONTEXTUALIZAR → VALIDAR → CONTRATUALIZAR → INTEGRAR → PROVAR → CONSTRUIR SOMENTE O DIFERENCIAL AUSENTE`

Regras:

1. componente externo não recebe soberania por existir ou estar instalado;
2. aquisição documental não significa aquisição operacional;
3. componente sem gates suficientes permanece `NOT_PROVEN`;
4. integração à Baseline canônica fica bloqueada até qualificação, contrato e prova;
5. dependência de doador não pode tornar-se dependência estrutural do produto final;
6. aquisição com gasto novo continua sujeita a portão humano;
7. rollback, atualização, substituição e remoção devem ser definidos quando aplicáveis.

## Consequência

A Fase 2 e fases posteriores devem demonstrar não apenas construção, mas também substituibilidade e integração comprovada de componentes adquiridos quando usados.
