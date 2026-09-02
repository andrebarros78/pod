# ADR-008 — Multiprojeto, federação e supersessão da topologia anterior

**Identificador:** POD-ADR-008
**Versão:** 1.0.0
**Status:** ACCEPTED
**Data:** 2026-09-02
**Conjunto:** POD-DOCSET-V003
**Decisão de produto:** André Barros
**Autoridade técnica:** Pipo
**Substitui:** uma instalação por projeto, quantidade fixa de serviços, Windows/SQLite como invariantes e Provider Manager soberano

## Contexto

O DOCSET V002 definia uma POD MAQ por projeto, topologia permanente, Windows, SQLite e Provider Manager separado como elementos da arquitetura. A reconsolidação posterior aprovou multiprojeto, federação, multi-OS e provedores subordinados ao Brain/Policy.

## Problema

Duas arquiteturas incompatíveis permaneciam formalmente utilizáveis. Um implementador poderia construir a topologia antiga e ainda alegar conformidade documental.

## Decisão

1. uma instalação POD pode operar múltiplos projetos;
2. project_id é obrigatório em todo estado, evento, comando, evidência, artefato, custo e segredo com escopo de projeto;
3. arquitetura lógica não define número fixo de processos ou serviços;
4. implantação começa como monólito modular local-first;
5. componentes podem ser extraídos quando testes justificarem isolamento;
6. sistema operacional, banco, mensageria e fornecedor são decisões de stack por ADR;
7. Provider Capability Registry e Provider Router pertencem à camada cognitiva, subordinados a Policy Router;
8. federação adiciona capacidade, sem criar autoridades soberanas concorrentes;
9. um projeto não acessa outro sem capability explícita e auditada;
10. isolamento é validado antes de ampliar concorrência.

## Alternativas consideradas

### Uma instalação por projeto

Rejeitada como invariante: duplica infraestrutura e impede visão multiprojeto. Pode continuar como modo de implantação de isolamento máximo.

### Microserviços fixos desde o início

Rejeitada: eleva custo operacional antes de necessidade comprovada.

### Um único projeto global sem fronteira

Rejeitada: mistura segredo, estado, custo e conhecimento.

### Provider Manager soberano independente

Rejeitada: cria autoridade cognitiva concorrente.

## Consequências

- todo contrato inclui ownership_scope;
- configuração física pode escolher um projeto por instalação sem mudar o domínio;
- migração de projeto deve preservar identidade e proveniência;
- testes de isolamento tornam-se críticos;
- stack permanece aberta até benchmark.

## Migração

- marcar DOCSET V002 como superseded;
- adotar POD-DOCSET-V003;
- remover requisitos uma POD MAQ por projeto e sete serviços permanentes;
- criar matriz V002;
- testar um único projeto primeiro, mantendo schema multiprojeto.

## Rollback

Modo de implantação single-project continua possível por policy. Voltar ao modelo de domínio single-project exige novo ADR e migração, pois remove capacidade e isolamento explícito.

## Segurança

Shared global data exige classificação e capability. Segredos são project-scoped por padrão. Cross-project read ou write gera audit record.

## Compatibilidade

Documentos históricos são incompatíveis e não orientam implementação. Não existe runtime oficial para migrar.

## Evidência

- conflito confirmado entre DOCSET V002 e reconsolidação V001;
- modelo consolidado em POD-DOC-002, POD-DOC-004 e POD-DOC-005;
- testes T-PRJ-001 a T-PRJ-005.

## Condição de revisão

Revisar se medição demonstrar que multiprojeto aumenta risco ou custo sem benefício. A revisão pode recomendar modo de implantação isolado, não remover project_id do domínio.

## Documentos relacionados

- POD-DOC-002;
- POD-DOC-004;
- POD-DOC-005;
- POD-DOC-006;
- POD-DOC-009.
