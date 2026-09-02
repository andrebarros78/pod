# POD — GOVERNANÇA DOCUMENTAL, VERSIONAMENTO E ADR — V003

**Identificador:** POD-DOC-011
**Versão:** 3.0.0
**Status:** ACTIVE
**Data:** 2026-09-02
**Conjunto:** POD-DOCSET-V003
**Autoridade:** A2 — governança
**Substitui:** Governança V001 e regras documentais do DOCSET V002

## 1. Finalidade

Garantir que arquitetura, contratos, requisitos, configuração, implementação, testes e evidências evoluam sem duas fontes ativas ou conclusão falsa.

## 2. Princípios

1. uma fonte ativa por assunto;
2. mudança arquitetural exige ADR;
3. mudança de contrato exige versão;
4. mudança de dados exige migração;
5. mudança normativa atualiza índice e manifesto;
6. versão substituída permanece no histórico;
7. documento não prova implementação;
8. teste não prova aceite sem evidência;
9. configuração crítica possui origem e validação;
10. segredo não entra em Git;
11. release possui revisão, tag, manifesto e rollback;
12. exceção possui escopo e expiração;
13. conflito falha visivelmente;
14. main não recebe mudança normativa direta sem revisão;
15. hashes são reproduzíveis.

## 3. Estados documentais

~~~text
DRAFT
IN_REVIEW
ACTIVE
SUPERSEDED
REVOKED
REFERENCE_ONLY
ARCHIVED
~~~

Somente ACTIVE possui autoridade. SUPERSEDED preserva história. REFERENCE_ONLY pode explicar origem, mas não orientar implementação.

## 4. Autoridade

O Índice Mestre determina a composição do conjunto. A versão maior do arquivo não vence se não estiver ACTIVE no índice e íntegra no manifesto.

Conflito dentro do conjunto ativo é defeito crítico documental.

## 5. Mudança normativa

Fluxo:

~~~text
ISSUE OR AUDIT FINDING
→ IMPACT ANALYSIS
→ ADR WHEN STRUCTURAL
→ UPDATE CANONICAL DOCUMENTS
→ UPDATE REQUIREMENTS AND TESTS
→ GENERATE MANIFEST
→ RUN VALIDATOR
→ REVIEW DIFF
→ COMMIT IN BRANCH
→ PULL REQUEST
→ REQUIRED CHECKS
→ MERGE
→ IMMUTABLE TAG
~~~

## 6. ADR obrigatório

Exige ADR:

- autoridade;
- missão e estados;
- persistência;
- segurança;
- protocolo;
- identidade;
- schema incompatível;
- topologia;
- banco ou mensageria;
- federação;
- stack;
- política de compatibilidade;
- remoção de portão;
- decisão difícil de reverter.

## 7. Conteúdo mínimo de ADR

- Identificador;
- Versão;
- Status;
- Data;
- Contexto;
- Problema;
- Decisão;
- Alternativas;
- Consequências;
- Migração;
- Rollback;
- Segurança;
- Compatibilidade;
- Evidência;
- Condição de revisão;
- Documentos relacionados;
- autoridade técnica;
- decisão de produto quando aplicável.

ADR aceito não é reescrito para mudar a decisão. Nova decisão cria novo ADR e marca o anterior como SUPERSEDED no índice.

## 8. Versionamento

Documentos e schemas usam major.minor.patch.

- major: quebra contrato ou substitui decisão;
- minor: adiciona capacidade compatível;
- patch: corrige sem mudar semântica.

Nome de arquivo pode carregar versão principal. Metadado interno é obrigatório.

## 9. Manifesto

POD_DOCUMENT_MANIFEST_V003.json:

- lista todos os documentos normativos;
- registra ordem, ID, path, versão, status, tamanho e SHA-256;
- registra conjunto substituído;
- registra algoritmo exato do set_hash;
- não inclui a si próprio no conjunto;
- é gerado e verificado pelo mesmo algoritmo versionado.

Serialização do set_hash é definida pelo POD-DOC-001.

## 10. Repositório

### Branches

- main representa a linha integrada;
- mudança usa branch curta;
- branch nasce do HEAD atual;
- mudança não relacionada não é incluída.

### Pull Request

PR normativa contém:

- motivo;
- decisões;
- documentos alterados;
- testes;
- evidência;
- impacto;
- rollback.

### Proteção esperada

Quando suportado pela conta e integração:

- bloquear force push em main;
- exigir pull request;
- exigir docs-integrity;
- impedir exclusão de main;
- exigir resolução de conversa;
- restringir bypass.

Se a proteção ainda não estiver tecnicamente configurada, isso é risco de repositório registrado; o workflow e a política continuam obrigatórios.

## 11. Commit

Commit deve:

- possuir mensagem descritiva;
- representar mudança coerente;
- não misturar segredos;
- passar validação;
- referenciar ADR quando estrutural.

Assinatura é recomendada e se torna obrigatória para release quando a infraestrutura de assinatura estiver configurada.

## 12. Tag e release

Docset ativo recebe tag:

~~~text
pod-docset-v3.0.0
~~~

Tag aponta para o commit integrado e não é movida. Correção posterior cria nova versão.

Release de software usará versão própria e registrará document_set_id.

## 13. Configuração

Configuração possui:

- config schema version;
- origem;
- ambiente;
- owner;
- defaults seguros;
- validação;
- segredo por referência;
- compatibilidade;
- data de ativação;
- rollback.

Configuração inválida impede READY.

## 14. Migração

Toda migração de dados define:

- origem e destino;
- pré-condições;
- backup;
- modo dry-run quando aplicável;
- verificação;
- compatibilidade;
- rollback ou compensação;
- evidência.

Migração não reescreve evento ou evidência histórica para parecer compatível.

## 15. Exceção

Campos:

~~~text
exception_id
requirement_id
scope
reason
risk
compensating_control
owner
technical_owner
approved_at
expires_at
verification
status
~~~

Exceção vencida é NON_COMPLIANT. Requisito crítico não recebe exceção silenciosa.

## 16. Rastreabilidade

Todo requisito possui:

~~~text
requirement
→ source
→ ADR
→ contract
→ phase
→ implementation
→ test
→ evidence
→ acceptance
~~~

Implementação sem requisito exige atualização da matriz ou remoção.

## 17. Gates automatizados

O workflow docs-integrity executa:

- JSON e hashes;
- set_hash;
- presença e metadados;
- links relativos;
- IDs únicos;
- referências de requisitos e testes;
- termos substituídos;
- contagem e estados da matriz;
- segredo por padrões básicos.

Scanner automático não substitui revisão humana ou auditoria.

## 18. Manutenção

Revisar DOCSET quando houver:

- nova decisão arquitetural;
- mudança de autoridade;
- mudança de estado;
- mudança de segurança;
- nova integração;
- stack escolhida;
- contrato executável;
- incidente relevante;
- release;
- requisito substituído.

## 19. Rollback documental

Antes de implementação dependente, reverter o commit ou PR é suficiente.

Após implementação:

- preservar a versão ativa usada pelo runtime;
- criar nova revisão;
- definir compatibilidade e migração;
- nunca mover tag publicada;
- nunca apagar conjunto que sustenta release.

## 20. Critérios de aceite

- um docset ACTIVE;
- manifesto reproduzível;
- nenhuma referência quebrada;
- nenhum ID duplicado;
- nenhum conflito de autoridade;
- ADR completo;
- matriz e testes consistentes;
- workflow verde;
- commit e tag identificáveis;
- histórico preservado.
