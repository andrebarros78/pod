# POD — ÍNDICE DE DECISÕES ARQUITETURAIS

**Identificador:** POD-DOC-012
**Versão:** 1.1.0
**Status:** ACTIVE
**Data:** 2026-09-03
**Conjunto:** POD-DOCSET-V003
**Autoridade:** A2

## Decisões ativas

| ADR | Estado | Decisão |
|---|---|---|
| [ADR-003](ADR-003-AUTORIDADE-DE-PROVA-E-TRANSICAO-DE-MISSAO.md) | ACCEPTED | Proof Engine avalia; Mission Core transiciona |
| [ADR-004](ADR-004-PERSISTENCIA-ATOMICA-JOURNAL-E-OUTBOX.md) | ACCEPTED | estado, evento e outbox no mesmo commit |
| [ADR-005](ADR-005-PORTOES-HUMANOS-E-DEPENDENCIAS-EXTERNAS.md) | ACCEPTED | três classes de espera sem contorno |
| [ADR-006](ADR-006-LEASE-FENCING-TEMPO-E-DELEGACAO-OFFLINE.md) | ACCEPTED | tempo distribuído e autoridade offline finita |
| [ADR-007](ADR-007-NUCLEO-DE-SEGURANCA-DESDE-A-FUNDACAO.md) | ACCEPTED | núcleo de segurança desde F0 |
| [ADR-008](ADR-008-MULTIPROJETO-FEDERACAO-E-SUPERSESSAO-DA-TOPOLOGIA-ANTERIOR.md) | ACCEPTED | instalação multiprojeto e topologia evolutiva |
| [ADR-009](ADR-009-INDEPENDENCIA-DO-CHATGPT-IA-HIBRIDA-E-TERMINAL-SOBERANO.md) | ACCEPTED | POD independente do ChatGPT, IA híbrida e terminal próprio |

## Decisões históricas

| ADR | Estado | Motivo |
|---|---|---|
| ADR-001 | NOT_PRESENT | identificador histórico não localizado no repositório; não possui autoridade |
| [ADR-002](ADR-002-DNA-OPERACIONAL-MISSION-PROVEN.md) | SUPERSEDED | preservado; escopo corrigido por ADR-003, ADR-005 e ADR-008 |

## Regra

ADR aceito:

- registra decisão, alternativas e consequências;
- não prova implementação;
- não é editado para mudar sua decisão;
- pode receber correção editorial sem mudar sentido;
- é substituído por novo ADR quando a decisão muda;
- só é normativo quando listado neste índice e no manifesto ativo.
