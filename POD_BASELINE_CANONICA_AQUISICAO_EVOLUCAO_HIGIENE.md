# POD — BASELINE CANÔNICA DE AQUISIÇÃO, EVOLUÇÃO E HIGIENE

**Versão:** 1.0.0  
**Data-base:** 03/10/2026  
**Horário de instituição documental:** 08h36 — horário de Brasília  
**Status:** BASELINE CANÔNICA DOCUMENTAL PARA AQUISIÇÃO, EVOLUÇÃO E HIGIENE  
**Estado operacional:** documentação criada; aquisição, sanitização, integração e implantação não são presumidas como executadas.  
**Projeto:** POD — Plataforma Orquestradora Durável

---

## 0. OBJETIVO IMUTÁVEL

O POD existe para receber um objetivo humano e assumir a complexidade técnica necessária até produzir resultado funcional, integrado, seguro, recuperável, documentado e comprovado.

Aquisição, arquitetura, componentes, linguagens, frameworks, bibliotecas, modelos, agentes e tecnologias são meios. Nenhuma evolução pode desviar o objetivo do produto.

```text
OBJETIVO HUMANO
→ POD COMPREENDE
→ POD DECIDE
→ POD PLANEJA
→ POD CONSTRÓI / ADQUIRE / ADAPTA
→ POD EXECUTA
→ POD OBSERVA
→ POD TESTA
→ FALHOU? DIAGNOSTICA → CORRIGE → RETESTA
→ POD INTEGRA
→ POD REGRESSIONA
→ POD PRODUZ EVIDÊNCIA
→ POD CRIA CHECKPOINT
→ MISSION_PROVEN
```

---

## 1. PRINCÍPIO REUSE FIRST

O POD não reconstruirá uma capacidade madura quando existir componente comprovadamente melhor, seguro, sustentável e integrável.

A ordem preferencial passa a ser:

```text
PESQUISAR
→ ANALISAR
→ COMPARAR
→ SELECIONAR
→ ADQUIRIR
→ SANITIZAR
→ NORMALIZAR E QUALIFICAR
→ APERFEIÇOAR
→ CONTEXTUALIZAR
→ VALIDAR
→ CONTRATUALIZAR
→ INTEGRAR
→ PROVAR
```

A construção própria será reservada para:

1. contratos específicos do POD;
2. integração entre componentes;
3. soberania, política e identidade do POD;
4. lacunas reais sem solução adequada disponível;
5. adaptações necessárias para satisfazer invariantes POD;
6. capacidades cuja aquisição gere dependência, risco, custo ou complexidade maior que a construção;
7. componentes cuja qualificação demonstre incompatibilidade com o objetivo do POD.

Regra:

> **Não construir por hábito. Não adquirir por moda. Adquirir vantagem real e construir somente o diferencial necessário.**

---

## 2. HIERARQUIA DE DECISÃO PARA EVOLUÇÃO

A evolução do POD seguirá esta prioridade:

```text
PRESERVAR O QUE FUNCIONA
→ CORRIGIR
→ APERFEIÇOAR
→ ADQUIRIR CAPACIDADE MADURA
→ INTEGRAR
→ ENDURECER
→ SUBSTITUIR SOMENTE COM EVIDÊNCIA
→ REESCREVER SOMENTE COMO ÚLTIMO RECURSO
```

Nenhuma mudança estrutural será aceita apenas por novidade tecnológica.

Toda evolução deve demonstrar ganho material em pelo menos um dos seguintes eixos:

- capacidade;
- autonomia;
- resultado;
- estabilidade;
- persistência;
- recuperação;
- segurança;
- simplicidade;
- custo;
- manutenção;
- observabilidade;
- desempenho;
- escalabilidade;
- substituibilidade;
- redução de lock-in.

---

## 3. ZERO DONOR COUPLING — DEFINIÇÃO CORRIGIDA

A regra histórica `ZERO DONOR COUPLING` permanece, mas sua interpretação é normalizada.

Ela significa:

```text
ZERO DONOR SOVEREIGNTY
ZERO LEGACY RUNTIME COUPLING
ZERO LEGACY REPOSITORY COUPLING
ZERO LEGACY PATH COUPLING
ZERO LEGACY CONFIG COUPLING
ZERO LEGACY SERVICE COUPLING
ZERO FORK COUPLING POR PADRÃO
ZERO VAZAMENTO DE TIPOS DO DOADOR PARA CONTRATOS POD
```

Ela **não** significa:

```text
ZERO THIRD-PARTY LIBRARIES
ZERO OPEN-SOURCE DEPENDENCIES
ZERO EXTERNAL COMPONENTS
ZERO REUSE
```

WMCP, LMCP e outros sistemas históricos podem doar conhecimento, algoritmos, testes, contratos, padrões e experiência, mas não podem permanecer como autoridade, runtime obrigatório, serviço obrigatório, namespace, caminho, banco, configuração ou dependência operacional do POD final.

Componentes OSS maduros podem integrar o POD quando:

- são adquiridos de distribuição oficial ou fonte confiável;
- possuem licença compatível;
- passam por sanitização;
- ficam atrás de contratos POD;
- não se tornam fonte soberana de verdade;
- possuem estratégia de atualização, substituição e remoção;
- não obrigam o POD a depender de fork privado sem necessidade demonstrada.

---

## 4. SOBERANIA E COMPONENTES ADQUIRIDOS

O POD possui uma única soberania lógica.

```text
ONE BRAIN
ONE GOVERNOR
ONE PROJECT REGISTRY
ONE MISSION REGISTRY
ONE OPERATIONAL TRUTH
ONE AUTHORIZATION MODEL
ONE GIT POLICY
ONE EVIDENCE / LEDGER MODEL
ONE CONTROL PLANE

N EXECUTION NODES
N OPERATING SYSTEMS
N PROVIDERS
N LIBRARIES
N SPECIALIZED COMPONENTS
```

Componente adquirido é uma capacidade especializada, nunca um segundo governo.

Nenhum componente externo pode:

- possuir a verdade final de missão;
- criar missão soberana por conta própria;
- conceder autorização a si próprio;
- substituir o modelo de autorização POD;
- declarar `MISSION_PROVEN` sozinho;
- escrever diretamente no estado soberano sem contrato;
- promover sua própria telemetria a evidência final sem validação;
- obrigar o POD a adotar seus tipos internos como contratos globais.

---

## 5. PIPELINE CANÔNICO DE AQUISIÇÃO

Toda capacidade externa passa obrigatoriamente pelas sete fases abaixo.

### 5.1 AQUISIÇÃO

Objetivo: obter o componente correto sem contaminar o POD.

Registrar, quando aplicável:

- nome;
- função desejada;
- origem oficial;
- versão;
- licença;
- pacote/imagem/binário;
- hash/assinatura quando disponível;
- dependências;
- motivo da aquisição;
- alternativa interna existente;
- vantagem esperada;
- custo financeiro;
- custo operacional;
- risco de lock-in.

Regras:

- preferir release, pacote ou imagem oficial;
- não criar fork por padrão;
- não copiar repositório inteiro para dentro do POD sem necessidade;
- não incorporar código desconhecido diretamente no núcleo;
- aquisição paga exige autorização humana.

### 5.2 SANITIZAÇÃO

Objetivo: remover ou conter risco antes de integração.

Verificar, proporcionalmente ao risco:

- SBOM;
- vulnerabilidades conhecidas;
- dependências transitivas;
- segredos embutidos;
- telemetria não desejada;
- portas abertas;
- privilégios;
- execução como root/Administrator;
- scripts de instalação;
- hooks;
- atualizadores automáticos;
- persistência própria;
- conexões externas;
- defaults inseguros;
- permissões de filesystem;
- supply chain;
- licença;
- capacidade de atualização e rollback.

Resultado permitido:

```text
SANITIZED
SANITIZED_WITH_RESTRICTIONS
REJECTED
NOT_PROVEN
```

### 5.3 NORMALIZAÇÃO E QUALIFICAÇÃO

Objetivo: transformar uma ferramenta externa em capacidade utilizável pelo POD.

Obrigatório:

- encapsular atrás de interface POD;
- impedir vazamento de tipos internos do fornecedor;
- impedir dependência de path específico;
- impedir dependência de configuração privada do doador;
- definir ownership de estado;
- definir responsabilidade única;
- medir benefício real;
- identificar sobreposição com componentes existentes;
- classificar `MANTER`, `APERFEIÇOAR`, `SUBSTITUIR`, `INCORPORAR_AGORA`, `TESTAR_PRIMEIRO`, `INCORPORAR_DEPOIS` ou `NÃO_INCORPORAR`.

### 5.4 CONTEXTUALIZAÇÃO

Objetivo: declarar onde a capacidade pertence na arquitetura POD.

Para cada componente declarar:

- função;
- módulo proprietário;
- consumidores;
- entradas;
- saídas;
- autoridade permitida;
- autoridade proibida;
- persistência;
- fronteira de segurança;
- comportamento de falha;
- recovery;
- observabilidade;
- impacto se comprometido;
- relação com Cérebro, Governador, ADE, Fabric e Executores.

### 5.5 VALIDAÇÃO

Objetivo: comprovar comportamento real.

Quando aplicável, validar:

- instalação;
- inicialização;
- função principal;
- entrada válida;
- entrada inválida;
- erro esperado;
- restart;
- persistência;
- recovery;
- concorrência;
- idempotência;
- timeout;
- fallback;
- segurança;
- desempenho mínimo;
- regressão;
- comportamento sem rede;
- comportamento quando dependência externa falha.

Existência, build ou processo ativo não equivalem a validação.

### 5.6 CONTRATUALIZAÇÃO

Objetivo: congelar a relação POD ↔ componente.

O contrato deve incluir:

- interface POD;
- schema;
- versão;
- entradas;
- saídas;
- erros;
- ownership de dados;
- política de autorização;
- limites de recurso;
- SLA/SLO quando aplicável;
- política de atualização;
- compatibilidade;
- estratégia de rollback;
- estratégia de substituição;
- estratégia de remoção;
- critérios de aceite;
- evidências exigidas.

### 5.7 INTEGRAÇÃO

Somente componente qualificado entra no fluxo real.

Prova mínima:

```text
INPUT
→ POD CONTRACT
→ ADAPTER
→ COMPONENT
→ RESULT
→ POD VALIDATION
→ EXPECTED OUTCOME
```

Integração somente é considerada comprovada quando o fluxo real, persistência/recovery aplicáveis, segurança e regressão forem aprovados.

---

## 6. SELEÇÃO INICIAL DE COMPONENTES PARA QUALIFICAÇÃO

Esta lista representa **seleção arquitetural inicial para aquisição/qualificação**, não prova de integração.

| Função POD | Seleção inicial | Estado documental |
|---|---|---|
| Memória de longo prazo | Mem0 | `SELECTED_FOR_QUALIFICATION` |
| Memória relacional/temporal | Graphiti | `TEST_FIRST` |
| Cérebro / orquestração agêntica | LangGraph | `SELECTED_FOR_QUALIFICATION` |
| ADE / desenvolvimento autônomo | OpenHands | `SPECIALIZED_PROVIDER_CANDIDATE` |
| Durable execution / workflows | Temporal | `SELECTED_FOR_QUALIFICATION` |
| Authorization / policy engine | Cedar | `SELECTED_FOR_QUALIFICATION` |
| Persistência vetorial | PostgreSQL + pgvector | `SELECTED_FOR_QUALIFICATION` |
| Protocolo externo de tools/capabilities | MCP | `EDGE_PROTOCOL_CANDIDATE` |
| Observabilidade | OpenTelemetry | `SELECTED_FOR_QUALIFICATION` |
| Cofre de segredos | OpenBao | `QUALIFY` |
| Sandbox Linux de alto risco | Firecracker | `QUALIFY` |
| Mensageria adicional | NATS JetStream | `DEFER_UNTIL_NEED_PROVEN` |

Nenhum item acima é considerado adquirido, sanitizado, validado ou integrado apenas por constar nesta tabela.

---

## 7. NORMALIZAÇÃO DOS PRINCIPAIS DOMÍNIOS

### 7.1 Memória

A memória POD permanece logicamente soberana e separada por função.

```text
POD MEMORY
├── OPERACIONAL
├── DOCUMENTAL
├── CONHECIMENTO
├── APRENDIZADO
├── EVIDÊNCIAS
├── CHECKPOINTS
└── HISTÓRICO
```

Ferramentas de memória podem implementar partes dessa capacidade, mas não transformam memória em prova operacional.

Regra:

> **Memória orienta onde procurar. Evidência atual decide o que é verdade.**

### 7.2 Cérebro

O Cérebro:

- compreende intenção;
- raciocina;
- planeja;
- decompõe;
- seleciona estratégias;
- diagnostica;
- replaneja;
- solicita conhecimento;
- interpreta evidências;
- propõe trabalho.

O Cérebro não possui autoridade administrativa irrestrita.

### 7.3 Governador

O Governador permanece a autoridade operacional única para:

- Project Registry;
- Mission Registry;
- Task Graph;
- scheduler global;
- recursos;
- conflitos;
- autorização;
- Git Policy;
- recovery coordination;
- registries;
- leases;
- fencing;
- prioridades;
- estado;
- checkpoints;
- incidentes;
- Evidence/Ledger.

Motores de workflow durável podem executar mecanismos internos, mas não substituem essa soberania.

### 7.4 ADE

O Executor Autônomo de Desenvolvimento e Correção trabalha no software.

Responsabilidades:

```text
INSPECIONAR
→ COMPREENDER
→ PLANEJAR ALTERAÇÃO
→ IMPLEMENTAR
→ EXECUTAR
→ OBSERVAR
→ TESTAR
→ DIAGNOSTICAR
→ CORRIGIR
→ RETESTAR
→ INTEGRAR
→ REGRESSIONAR
→ PRODUZIR EVIDÊNCIA
→ CHECKPOINT
→ PROVAR
```

Coding agents externos podem ser providers especializados do ADE, nunca soberania do POD.

---

## 8. HIGIENE DE ARQUITETURA

É proibido incorporar componente que crie, sem justificativa e contrato explícitos:

- segundo Governador;
- segunda memória soberana concorrente;
- segundo scheduler global concorrente;
- segunda verdade de missão;
- segunda política Git;
- autorização paralela;
- recovery paralelo conflitante;
- duplicação de responsabilidade;
- persistência oculta;
- bypass de Command API;
- bypass de policy gate;
- painel como fonte de verdade;
- executor como autoridade.

Regra de higiene:

```text
MENOS CÓDIGO PRÓPRIO
+ MENOS COMPONENTES REDUNDANTES
+ MAIS SOFTWARE MADURO
+ CONTRATOS POD FORTES
+ SANITIZAÇÃO
+ SUBSTITUIBILIDADE
+ PROVA REAL
= POD MAIS ROBUSTO
```

---

## 9. SEGURANÇA POR AQUISIÇÃO

Componente adquirido não herda confiança.

```text
THIRD_PARTY != TRUSTED
INTERNAL != TRUSTED
SIGNED != SAFE
POPULAR != SAFE
OPEN_SOURCE != SAFE
RUNNING != PROVEN
```

Aplicam-se integralmente:

- Security by Design;
- Security by Default;
- Security by Verification;
- Security by Containment;
- Least Privilege;
- Deny by Default;
- Fail Closed;
- Defense in Depth;
- Assume Breach;
- supply-chain verification;
- segregação de credenciais;
- evidência objetiva.

---

## 10. VERDADE E EVIDÊNCIA

Estados permitidos:

```text
VERIFIED
INFERRED
HYPOTHESIS
NOT_VERIFIED
UNKNOWN
```

Nunca promover automaticamente:

```text
DOCUMENTED → VERIFIED
SELECTED → ACQUIRED
ACQUIRED → SANITIZED
SANITIZED → QUALIFIED
QUALIFIED → INTEGRATED
INTEGRATED → PROVEN
```

Cada transição exige evidência proporcional.

---

## 11. GATE DE ACEITAÇÃO DE COMPONENTE

Um componente só poderá entrar no baseline operacional quando, conforme aplicável:

```text
SOURCE_VERIFIED=PASS
LICENSE_VERIFIED=PASS
SUPPLY_CHAIN_CHECK=PASS
SECURITY_SANITIZATION=PASS
RESPONSIBILITY_BOUNDARY=PASS
POD_CONTRACT=PASS
DATA_OWNERSHIP=PASS
AUTHORIZATION_BOUNDARY=PASS
FAILURE_BEHAVIOR=PASS
RECOVERY_BEHAVIOR=PASS
OBSERVABILITY=PASS
INTEGRATION_TEST=PASS
REGRESSION=PASS
REMOVAL_STRATEGY=PASS
NO_SOVEREIGNTY_LEAK=PASS
```

Gate ausente ou evidência insuficiente:

```text
COMPONENT_STATUS=NOT_PROVEN
INTEGRATION_TO_CANONICAL_BASELINE=BLOCKED
```

---

## 12. GOVERNANÇA DOCUMENTAL

Hierarquia documental recomendada após esta baseline:

```text
POD_DOCUMENTACAO_CONSOLIDADA_CANONICA.md
POD_BASELINE_CANONICA_AQUISICAO_EVOLUCAO_HIGIENE.md
ADR/
SCHEMAS/
CONTRACTS/
RUNBOOKS/
EVIDENCE/
RELEASES/
HISTORY/
```

As normas transversais de Segurança, Verdade/Evidência e Execução permanecem obrigatórias enquanto não forem formalmente absorvidas sem perda pela fonte canônica.

Material histórico permanece em `HISTORY/` com `NORMATIVE=false`.

Mudanças que afetem soberania, segurança, persistência, execução, prova, contratos ou autoridade exigem ADR.

---

## 13. REGRA TERMINAL

```text
COMPONENTE EXISTE
!= COMPONENTE QUALIFICADO

COMPONENTE QUALIFICADO
!= COMPONENTE INTEGRADO

COMPONENTE INTEGRADO
!= CAPACIDADE PROVADA

CAPACIDADE PROVADA
!= PRODUTO PROVADO
```

E:

```text
PESQUISAR O QUE JÁ EXISTE
→ ADQUIRIR O QUE É BOM
→ APERFEIÇOAR O QUE É ÚTIL
→ NORMALIZAR PARA POD
→ PROVAR
→ CONSTRUIR SOMENTE O QUE FALTA
```

**O objetivo do POD prevalece sobre a tecnologia usada para alcançá-lo.**

---

## 14. ESTADO DESTA BASELINE

```text
BASELINE_DOCUMENT_CREATED=VERIFIED
ARCHITECTURAL_RULES_DEFINED=VERIFIED
COMPONENT_SELECTION=DOCUMENTED

ACQUISITION=NOT_EXECUTED
SANITIZATION=NOT_EXECUTED
NORMALIZATION=NOT_EXECUTED
VALIDATION=NOT_EXECUTED
CONTRACTUALIZATION=NOT_EXECUTED
INTEGRATION=NOT_EXECUTED
MISSION_PROVEN=NO
```
