# POD — REGISTRO VIVO DE IDEIAS E MEMÓRIA

**Status:** WORKING / NON-NORMATIVE
**Finalidade:** capturar ideias, princípios, capacidades, riscos, correções e memórias durante a fase de concepção do POD sem alterar automaticamente a arquitetura oficial.

## Regra central

`MEMÓRIA REGISTRADA != REGRA ARQUITETURAL ATIVA`

Nenhuma entrada deste arquivo modifica por si só baseline, contrato, arquitetura, ADR ou implementação.

A arquitetura final será montada posteriormente por revisão integral deste registro, resolução de conflitos, deduplicação e consolidação.

## Tipos de registro

- IDEA
- PRINCIPLE
- CAPABILITY
- RULE_CANDIDATE
- CONSTRAINT
- LESSON_LEARNED
- RISK
- QUESTION
- ARCHITECTURAL_INSIGHT

## Estados

- CAPTURED
- UNDER_REVIEW
- CANDIDATE
- REJECTED
- MERGED
- CONSOLIDATED

## Estrutura de cada memória

```text
ID:
DATA:
TIPO:
STATUS:
NORMATIVO: NÃO

TEXTO ORIGINAL:

INTERPRETAÇÃO TÉCNICA:

MOTIVAÇÃO:

IMPACTO POSSÍVEL:

DEPENDÊNCIAS:

CONFLITOS POSSÍVEIS:

RELAÇÕES COM OUTRAS MEMÓRIAS:

DECISÃO FINAL:

INCORPORADO EM:
```

## Processo de consolidação futura

`CAPTURAR → AGRUPAR → COMPARAR → DETECTAR DUPLICIDADES → DETECTAR CONTRADIÇÕES → RESOLVER → SELECIONAR REGRAS FINAIS → MONTAR ARQUITETURA → VALIDAR PONTA A PONTA → BASELINE`

## Política durante a fase de concepção

1. Registrar cada nova ideia aqui.
2. Preservar o texto original separadamente da interpretação técnica.
3. Não criar novo ADR para cada ideia.
4. Não alterar baseline por memória isolada.
5. Permitir coexistência temporária de ideias conflitantes.
6. Resolver conflitos somente na consolidação do bloco ou da arquitetura final.
7. Preservar histórico de ideias rejeitadas, fundidas ou superadas.
8. Criar ADR somente quando uma decisão estrutural realmente precisar ser formalizada após consolidação.

---

# MEMÓRIAS

