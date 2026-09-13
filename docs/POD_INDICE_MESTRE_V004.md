# POD — ÍNDICE MESTRE DE DOCUMENTOS E PRECEDÊNCIA — V004

**Identificador:** POD-DOC-001
**Versão:** 4.0.0
**Status:** ACTIVE
**Data:** 2026-09-13
**Conjunto:** POD-DOCSET-V004
**Autoridade:** A1 — autoridade documental
**Substitui:** POD-DOCSET-V003 como conjunto ativo quando o manifesto V004 validar

## 1. Finalidade

Este índice reconcilia a arquitetura do POD com a decisão de Core selado, SCM soberano, classificação de persistência, Execution Envelope, armazenamento endereçado por conteúdo e Integration Plane, sem regredir multiprojeto, soberania de missão, federação, segurança ou independência de fornecedor.

Regra:

~~~text
UM CONJUNTO ATIVO
UMA PRECEDÊNCIA
UMA VERSÃO ATIVA POR ASSUNTO
HISTÓRICO PRESERVADO
INTEGRIDADE REPRODUZÍVEL
~~~

## 2. Estado real

~~~text
CONCEPÇÃO E CONTRATOS = ACTIVE / NORMATIVE
RECONCILIAÇÃO ARQUITETURAL V004 = ACTIVE / NORMATIVE
IMPLEMENTAÇÃO = NOT_STARTED / NOT_PROVEN
STACK FÍSICA = A DEFINIR POR IMPLEMENTAÇÃO
MISSION_PROVEN DA IMPLEMENTAÇÃO = NÃO
~~~

A reconciliação documental não equivale a implementação.

## 3. Precedência

Em conflito, prevalece a primeira fonte aplicável:

1. lei, licença, limitação física e decisão legítima do Owner;
2. este Índice Mestre e manifesto V004 íntegro;
3. Baseline V003 e DNA Operacional V002, exceto onde ADR-010 e Arquitetura V003 especificarem fronteira mais nova;
4. política de segurança e autorizações;
5. ADR ativo específico;
6. Arquitetura Técnica V003;
7. contratos V002 + Especificação POD-DOC-013;
8. requisitos, plano de construção e plano de testes;
9. configuração versionada da implementação;
10. documentos históricos/working apenas como referência.

## 4. Documentos ativos

| Ordem | ID | Documento | Autoridade | Finalidade |
|---:|---|---|---|---|
| 1 | POD-DOC-001 | [Índice Mestre V004](POD_INDICE_MESTRE_V004.md) | A1 | composição e precedência |
| 2 | POD-DOC-002 | [Baseline V003](baselines/POD_BASELINE_V003_2026-09-02.md) | A1 | decisões anteriores preservadas |
| 3 | POD-DOC-003 | [DNA Operacional V002](architecture/POD_DNA_OPERACIONAL_V002.md) | A1 | invariantes raiz |
| 4 | POD-DOC-004 | [Projeto Conceitual V002](specifications/POD_PROJETO_CONCEITUAL_V002.md) | A2 | identidade, escopo e funcionamento |
| 5 | POD-DOC-005 | [Arquitetura Técnica V003](architecture/POD_ARQUITETURA_TECNICA_V003.md) | A2 | arquitetura reconciliada |
| 6 | POD-DOC-006 | [Contratos, Dados e Estados V002](specifications/POD_CONTRATOS_DADOS_ESTADOS_V002.md) | A2 | contratos existentes |
| 7 | POD-DOC-007 | [Segurança e Autorizações V002](specifications/POD_SEGURANCA_AUTORIZACOES_V002.md) | A1 | segurança, identidade e gates |
| 8 | POD-DOC-008 | [Matriz de Rastreabilidade V002](specifications/POD_REQUISITOS_RASTREABILIDADE_V002.md) | A3 | requisitos existentes |
| 9 | POD-DOC-009 | [Plano Mestre de Construção V002](specifications/POD_PLANO_MESTRE_CONSTRUCAO_V002.md) | A3 | sequência executiva existente |
| 10 | POD-DOC-010 | [Plano de Testes e Aceite V002](specifications/POD_PLANO_TESTES_ACEITE_V002.md) | A3 | prova e gates existentes |
| 11 | POD-DOC-011 | [Governança Documental V003](governance/POD_GOVERNANCA_DOCUMENTAL_V003.md) | A2 | versão e integridade |
| 12 | POD-DOC-012 | [Índice de ADRs](adr/README.md) | A2 | decisões arquiteturais ativas |
| 13 | POD-ADR-003 | [ADR-003](adr/ADR-003-AUTORIDADE-DE-PROVA-E-TRANSICAO-DE-MISSAO.md) | A2 | prova e transição |
| 14 | POD-ADR-004 | [ADR-004](adr/ADR-004-PERSISTENCIA-ATOMICA-JOURNAL-E-OUTBOX.md) | A2 | persistência atômica |
| 15 | POD-ADR-005 | [ADR-005](adr/ADR-005-PORTOES-HUMANOS-E-DEPENDENCIAS-EXTERNAS.md) | A1 | portões humanos |
| 16 | POD-ADR-006 | [ADR-006](adr/ADR-006-LEASE-FENCING-TEMPO-E-DELEGACAO-OFFLINE.md) | A2 | concorrência distribuída |
| 17 | POD-ADR-007 | [ADR-007](adr/ADR-007-NUCLEO-DE-SEGURANCA-DESDE-A-FUNDACAO.md) | A1 | segurança desde F0 |
| 18 | POD-ADR-008 | [ADR-008](adr/ADR-008-MULTIPROJETO-FEDERACAO-E-SUPERSESSAO-DA-TOPOLOGIA-ANTERIOR.md) | A2 | multiprojeto e federação |
| 19 | POD-ADR-009 | [ADR-009](adr/ADR-009-INDEPENDENCIA-DO-CHATGPT-IA-HIBRIDA-E-TERMINAL-SOBERANO.md) | A1 | independência, IA híbrida e terminal |
| 20 | POD-ADR-010 | [ADR-010](adr/ADR-010-CORE-SELADO-SCM-SOBERANO-E-SEPARACAO-DE-ESTADO.md) | A1/A2 | Core selado e SCM soberano |
| 21 | POD-DOC-013 | [Core, SCM, Storage e Execution Envelope V001](specifications/POD_CORE_SCM_ARMAZENAMENTO_EXECUTION_ENVELOPE_V001.md) | A2 | contratos novos da reconciliação |

## 5. Reconciliação normativa

A V004 adota explicitamente:

~~~text
CORE_RELEASE = IMMUTABLE
RUNTIME_STATE = EXTERNAL
PROJECT_STATE = EXTERNAL_TO_CORE
MISSION_STATE = EXTERNAL_TO_CORE

PERSISTENCE_CLASS = DURABLE | RECONSTRUCTIBLE | EPHEMERAL

SCM = SOVEREIGN_COGNITIVE_MEMORY
RAG = RETRIEVAL_MECHANISM
VECTOR_INDEX = RECONSTRUCTIBLE
LEXICAL_INDEX = RECONSTRUCTIBLE
KNOWLEDGE_GRAPH_PROJECTION = RECONSTRUCTIBLE

KNOWLEDGE_ADMISSION_GATE = REQUIRED
KNOWLEDGE_SCOPE = REQUIRED
KNOWLEDGE_PROVENANCE = REQUIRED
CONFIDENCE != FRESHNESS

INTEGRATION_PROVIDER = REPLACEABLE
EXTERNAL_PROVIDER != STRUCTURAL_DEPENDENCY
~~~

## 6. Preservado sem regressão

Continuam normativos:

- uma instalação pode operar N projetos isolados por `project_id`;
- Mission Core é a única autoridade de transição soberana da missão;
- Proof Engine emite verdict e não declara MISSION_PROVEN;
- falha recuperável não equivale a parada;
- segurança é fail-closed;
- lease/generation/fencing governam autoridade distribuída;
- nó federado não recebe soberania ilimitada;
- IA é multi-provider e substituível;
- POD possui terminal próprio e não depende estruturalmente do ChatGPT/MCP;
- evidência, estado e eventos continuam auditáveis.

## 7. Documentos substituídos especificamente

| Artefato | Estado em V004 | Substituído por |
|---|---|---|
| POD_ARQUITETURA_TECNICA_V002.md | SUPERSEDED | POD_ARQUITETURA_TECNICA_V003.md |
| POD-DOCSET-V003 | SUPERSEDED como conjunto ativo | POD-DOCSET-V004 |
| Demais documentos V003 listados na seção 4 | RETAINED | continuam ativos dentro do V004 |

Arquivos históricos não são apagados.

## 8. Gate de implementação da nova arquitetura

Nenhum documento desta revisão prova software implementado.

A implementação deverá demonstrar, no mínimo:

~~~text
CORE_INTEGRITY=PASS
CORE_SIZE_DRIFT=PASS
CORE_DIRTY_FILES=0
PROJECT_FILES_IN_CORE=0
MISSION_FILES_IN_CORE=0
REGENERABLE_DATA_IN_CORE=0
UNEXPECTED_RESIDUE=0

KNOWLEDGE_WITHOUT_EVIDENCE_REJECTED=PASS
KNOWLEDGE_WITHOUT_SCOPE_REJECTED=PASS
KNOWLEDGE_REVOCATION=PASS
PROJECTION_REBUILD=PASS
CAS_HASH_INTEGRITY=PASS
CAS_GC_REFERENCE_SAFETY=PASS
EXECUTION_ENVELOPE_ENFORCEMENT=PASS
CORE_RELEASE_ROLLBACK=PASS
~~~

## 9. Regra de integridade documental

O manifesto V004 usa a mesma regra SHA-256 do V003:

~~~text
<order>\t<document_id>\t<path>\t<size_bytes>\t<sha256_hex>\n
~~~

Linhas são ordenadas por `order`; o manifesto não inclui a si próprio no set hash.

## 10. Regra final

Qualquer implementação nova deve seguir a Arquitetura Técnica V003, ADR-010 e POD-DOC-013 para os assuntos reconciliados. O restante do DOCSET V003 permanece aplicável enquanto não conflitar com essas decisões específicas.
