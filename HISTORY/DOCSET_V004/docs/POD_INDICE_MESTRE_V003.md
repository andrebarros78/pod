# POD — ÍNDICE MESTRE DE DOCUMENTOS E PRECEDÊNCIA — V003

**Identificador:** POD-DOC-001
**Versão:** 3.1.0
**Status:** ACTIVE
**Data:** 2026-09-03
**Conjunto:** POD-DOCSET-V003
**Autoridade:** A1 — autoridade documental
**Substitui:** POD-DOCSET-V002 e toda baseline anterior do POD

## 1. Finalidade

Este é o ponto de entrada oficial da documentação do POD. Ele elimina a concorrência entre o pacote histórico, a baseline de 02/09/2026 e os documentos posteriores de trabalho.

Somente os arquivos declarados **ACTIVE** neste índice podem orientar a implementação. Documento em **WORKING**, **REFERENCE_ONLY**, **SUPERSEDED** ou fora do manifesto não possui autoridade normativa.

Regra:

~~~text
UM CONJUNTO ATIVO
UMA PRECEDÊNCIA
UMA VERSÃO ATIVA POR ASSUNTO
HISTÓRICO PRESERVADO
INTEGRIDADE REPRODUZÍVEL
~~~

## 2. Estado real do projeto

O DOCSET V003 consolida decisões conceituais e contratos técnicos. Ele não afirma que o software foi implementado.

~~~text
CONCEPÇÃO E CONTRATOS = ACTIVE / NORMATIVE
IMPLEMENTAÇÃO         = NOT_STARTED
REQUISITOS            = DEFINED_NOT_IMPLEMENTED
STACK FÍSICA          = UNDECIDED
MISSION_PROVEN        = NÃO APLICÁVEL À CONSTRUÇÃO AINDA
~~~

## 3. Precedência

Em conflito, prevalece a primeira fonte aplicável:

1. lei, licença, limitação física e decisão legítima do Owner dentro de sua autoridade;
2. este Índice Mestre e o manifesto íntegro;
3. Baseline V003 e DNA Operacional V002;
4. política de segurança e autorizações;
5. ADR ativo que trate especificamente da decisão;
6. arquitetura técnica;
7. contratos de componentes, dados, estados e eventos;
8. requisitos, plano de construção e plano de testes;
9. configuração versionada da implementação;
10. documentos de trabalho e memória, apenas como referência.

Nenhum ADR futuro altera silenciosamente o conjunto ativo. A decisão passa a orientar implementação quando estiver aceita, listada no índice e incluída em manifesto válido.

## 4. Documentos ativos

| Ordem | ID | Documento | Autoridade | Finalidade |
|---:|---|---|---|---|
| 1 | POD-DOC-001 | [Índice Mestre V003](POD_INDICE_MESTRE_V003.md) | A1 | composição e precedência |
| 2 | POD-DOC-002 | [Baseline V003](baselines/POD_BASELINE_V003_2026-09-02.md) | A1 | decisões congeladas |
| 3 | POD-DOC-003 | [DNA Operacional V002](architecture/POD_DNA_OPERACIONAL_V002.md) | A1 | invariantes raiz |
| 4 | POD-DOC-004 | [Projeto Conceitual V002](specifications/POD_PROJETO_CONCEITUAL_V002.md) | A2 | identidade, escopo e funcionamento |
| 5 | POD-DOC-005 | [Arquitetura Técnica V002](architecture/POD_ARQUITETURA_TECNICA_V002.md) | A2 | componentes, planos e fronteiras |
| 6 | POD-DOC-006 | [Contratos, Dados e Estados V002](specifications/POD_CONTRATOS_DADOS_ESTADOS_V002.md) | A2 | autoridade e consistência implementável |
| 7 | POD-DOC-007 | [Segurança e Autorizações V002](specifications/POD_SEGURANCA_AUTORIZACOES_V002.md) | A1 | identidade, políticas e portões |
| 8 | POD-DOC-008 | [Matriz de Rastreabilidade V002](specifications/POD_REQUISITOS_RASTREABILIDADE_V002.md) | A3 | requisitos e cobertura |
| 9 | POD-DOC-009 | [Plano Mestre de Construção V002](specifications/POD_PLANO_MESTRE_CONSTRUCAO_V002.md) | A3 | sequência executiva |
| 10 | POD-DOC-010 | [Plano de Testes e Aceite V002](specifications/POD_PLANO_TESTES_ACEITE_V002.md) | A3 | prova e gates |
| 11 | POD-DOC-011 | [Governança Documental V003](governance/POD_GOVERNANCA_DOCUMENTAL_V003.md) | A2 | mudança, versão e integridade |
| 12 | POD-DOC-012 | [Índice de ADRs](adr/README.md) | A2 | decisões arquiteturais ativas |
| 13 | POD-ADR-003 | [ADR-003](adr/ADR-003-AUTORIDADE-DE-PROVA-E-TRANSICAO-DE-MISSAO.md) | A2 | prova e transição |
| 14 | POD-ADR-004 | [ADR-004](adr/ADR-004-PERSISTENCIA-ATOMICA-JOURNAL-E-OUTBOX.md) | A2 | persistência atômica |
| 15 | POD-ADR-005 | [ADR-005](adr/ADR-005-PORTOES-HUMANOS-E-DEPENDENCIAS-EXTERNAS.md) | A1 | portões humanos |
| 16 | POD-ADR-006 | [ADR-006](adr/ADR-006-LEASE-FENCING-TEMPO-E-DELEGACAO-OFFLINE.md) | A2 | concorrência distribuída |
| 17 | POD-ADR-007 | [ADR-007](adr/ADR-007-NUCLEO-DE-SEGURANCA-DESDE-A-FUNDACAO.md) | A1 | segurança desde F0 |
| 18 | POD-ADR-008 | [ADR-008](adr/ADR-008-MULTIPROJETO-FEDERACAO-E-SUPERSESSAO-DA-TOPOLOGIA-ANTERIOR.md) | A2 | arquitetura vigente |
| 19 | POD-ADR-009 | [ADR-009](adr/ADR-009-INDEPENDENCIA-DO-CHATGPT-IA-HIBRIDA-E-TERMINAL-SOBERANO.md) | A1 | produto próprio, IA híbrida e terminal soberano |

O arquivo [POD_DOCUMENT_MANIFEST_V003.json](POD_DOCUMENT_MANIFEST_V003.json) contém tamanho e SHA-256 de todos os itens acima.

### Cobertura da reconsolidação

| Fechamento conceitual de origem | Fonte normativa V003 |
|---|---|
| 1. matriz de autoridade | POD-DOC-002, POD-DOC-006, ADR-003 |
| 2. Constitution/Policy | POD-DOC-007, ADR-007 |
| 3. conflito decisão/segurança/recursos | POD-DOC-002, POD-DOC-007 |
| 4. ciclo de missão | POD-DOC-006 |
| 5. pausa, drain, cancelamento, preempção e compensação | POD-DOC-006, POD-DOC-009 |
| 6. planejamento, engenharia, scheduling e roteamento | POD-DOC-005, POD-DOC-006 |
| 7. consistência | POD-DOC-006, ADR-004 |
| 8. ordem de eventos e entrega | ADR-004 |
| 9. tempo distribuído | ADR-006 |
| 10. soberania durante partição | ADR-006 |
| 11. mobilidade de workspace, dados e artefatos | POD-DOC-005, POD-DOC-006 |
| 12. ciclo da frota | POD-DOC-006 |
| 13. trust bootstrap do nó | POD-DOC-007 |
| 14. envelope do micro-scheduler | POD-DOC-006 |
| 15. fairness multiprojeto | POD-DOC-005, POD-DOC-009 |
| 16. compartilhamento entre projetos | POD-DOC-007, ADR-008 |
| 17. arquitetura híbrida multi-provider | POD-DOC-004, POD-DOC-005 |
| 18. arbitragem cognitiva | POD-DOC-004, POD-DOC-008 |
| 19. Learning & Training | POD-DOC-004, POD-DOC-009 |
| 20. Product Delivery Contract | POD-DOC-004, POD-DOC-006 |
| 21. self-update | POD-DOC-005, POD-DOC-009 |
| 22. prova independente | POD-DOC-003, ADR-003 |
| 23. progresso real | POD-DOC-006 |
| 24. economia e orçamento | POD-DOC-005, POD-DOC-006, POD-DOC-007 |
| 25. independência do ChatGPT, IA híbrida e terminal próprio | ADR-009 |

## 5. Documentos substituídos

| Artefato | Estado | Substituído por |
|---|---|---|
| POD-DOCSET-V002 fornecido anteriormente | SUPERSEDED | POD-DOCSET-V003 |
| docs/baselines/POD_BASELINE_2026-09-02.md | SUPERSEDED | POD-DOC-002 |
| docs/architecture/POD_DNA_OPERACIONAL_V001.md | SUPERSEDED | POD-DOC-003 |
| docs/adr/ADR-002-DNA-OPERACIONAL-MISSION-PROVEN.md | SUPERSEDED | ADR-003, ADR-005 e ADR-008 |
| Matriz Mestra V001 de 72 requisitos | SUPERSEDED | POD-DOC-008 |
| Contratos e topologia do modelo uma instalação/um projeto | SUPERSEDED | POD-DOC-004, POD-DOC-005 e ADR-008 |

Os artefatos substituídos permanecem no histórico para auditoria. Não podem ser usados para decidir comportamento novo.

## 6. Documentos de trabalho

Todo arquivo em docs/working permanece **REFERENCE_ONLY**. Ele preserva origem, raciocínio e memória, mas não prevalece sobre o DOCSET V003.

Decisão válida encontrada apenas em working deve ser promovida por revisão normativa antes de orientar código.

## 7. Ordem obrigatória de leitura

Para implementar:

~~~text
ÍNDICE
→ BASELINE
→ DNA
→ SEGURANÇA E AUTORIZAÇÕES
→ ADRs
→ ARQUITETURA
→ CONTRATOS
→ REQUISITOS
→ PLANO DE CONSTRUÇÃO
→ PLANO DE TESTES
→ GOVERNANÇA
~~~

## 8. Regra de integridade

O hash do conjunto é reproduzido assim:

1. ordenar documentos por order;
2. para cada documento, calcular SHA-256 sobre os bytes exatos do arquivo;
3. produzir uma linha UTF-8, terminada por LF:

~~~text
<order>\t<document_id>\t<path>\t<size_bytes>\t<sha256_hex>\n
~~~

4. concatenar as linhas sem cabeçalho;
5. calcular SHA-256 sobre a concatenação.

O manifesto não inclui o próprio hash para evitar referência circular.

A evidência da validação do conjunto está preservada em
[POD_DOCSET_V003_VALIDATION.md](evidence/POD_DOCSET_V003_VALIDATION.md). Evidência não
é fonte normativa e não integra o hash do conjunto.

## 9. Gate de ativação

Uma revisão documental somente fica ativa quando:

- todos os documentos obrigatórios estão presentes;
- hashes individuais e hash do conjunto são válidos;
- não há ID duplicado;
- não há dois documentos ativos para o mesmo assunto;
- links relativos são válidos;
- ADRs estão completos;
- matriz e plano de testes usam IDs existentes;
- o validador retorna POD_DOCSET_VALID;
- a mudança está registrada em commit;
- o conjunto recebe tag imutável quando a capacidade do repositório estiver disponível.

## 10. Regra final

Qualquer texto que contradiga este conjunto é histórico, proposta ou defeito documental. O conflito deve falhar de forma visível; nunca deve ser resolvido silenciosamente por um implementador.
