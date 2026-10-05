# POD — PLANO MESTRE DE CONSTRUÇÃO — V002

**Identificador:** POD-DOC-009
**Versão:** 2.1.0
**Status:** ACTIVE
**Data:** 2026-09-03
**Conjunto:** POD-DOCSET-V003
**Autoridade:** A3 — sequência executiva
**Substitui:** plano mestre V001
**Implementação comprovada:** NÃO

## 1. Regra de execução

Cada incremento produz:

~~~text
REQUIREMENT
→ IMPLEMENTATION
→ TEST
→ EVIDENCE
→ ACCEPTANCE
→ CHECKPOINT
~~~

Falha de teste retorna ao Loop Engineering. Fase não avança com requisito crítico sem aceite ou proteção formal.

## 2. Gate G0 — prontidão pré-implementação

Antes de escolher stack:

- DOCSET V003 íntegro;
- ADRs 003–008 ativos;
- contratos sem conflito;
- matriz requisito-teste completa;
- plano de testes completo;
- validador documental verde.

Depois de G0:

1. avaliar stack por critérios objetivos;
2. executar benchmark mínimo de persistência, processo, empacotamento e operação;
3. registrar ADR da stack;
4. criar skeleton;
5. iniciar F0.

## 3. Estratégia de entrega

O domínio nasce multiprojeto, federável e multi-provider. A construção física começa pequena:

~~~text
1 PROCESSO PRINCIPAL
1 TRANSACTION STORE
1 PROJETO DE TESTE
1 MISSÃO
1 ENGINE LOCAL
1 ADAPTER COGNITIVO QUANDO NECESSÁRIO
1 FLUXO DE PROVA
~~~

Distribuição, serviços separados e paralelismo entram somente após a fatia local ser comprovada.

## 4. Ordem mestre

~~~text
F0  FUNDAÇÃO, CONTRATOS EXECUTÁVEIS E SECURITY KERNEL
F1  TRANSACTION JOURNAL, MEMORY E MISSION CORE
F2  POLICY, PORTÕES, ESTADOS E PROOF ENGINE
F3  PRIMEIRA FATIA VERTICAL MISSION_PROVEN
F4  ENGINE LOCAL E CONSTRUCTION ENGINEERING
F5  GOVERNOR, SCHEDULER E CONCORRÊNCIA
F6  BRAIN INICIAL E CONHECIMENTO
F7  MULTI-PROVIDER E ECONOMIA COGNITIVA
F8  FEDERAÇÃO E NODE AGENT
F9  ENGINES MULTIPLATAFORMA
F10 SECURITY AVANÇADA E IMMUNE SYSTEM
F11 LEARNING E TRAINING
F12 PRODUCT TESTING, PRODUCT SECURITY E DELIVERY
F13 UPDATE, BACKUP E DISASTER RECOVERY
F14 PERFORMANCE, CARGA, PARTIÇÃO E CHAOS
F15 E2E SOBERANO DO PRÓPRIO POD
~~~

## 5. F0 — Fundação e Security Kernel

### Entregar

- estrutura do repositório;
- ferramenta e versões fixadas;
- modelos de configuração;
- schemas iniciais;
- UUIDv7;
- tipos de Clock;
- failure taxonomy;
- ownership/confidentiality/training/effect scopes;
- Identity, Capability, Policy e SecretRef ports;
- hashing e redaction;
- generation e fencing primitives;
- architecture tests;
- pipeline de qualidade.

### Testar

- domínio não importa infraestrutura;
- IDs válidos e únicos;
- monotonic permanece local;
- segredo de teste é redigido;
- deny by default;
- stale fencing é rejeitado;
- documentos e schemas mantêm rastreabilidade.

### Gate de saída

Todos os requisitos críticos de F0 em ACCEPTED e nenhum segredo no repositório.

## 6. F1 — Transaction Journal, Memory e Mission Core

### Entregar

- Authoritative Transaction Store;
- aggregate versioning;
- Domain Event Journal;
- Inbox/Outbox;
- idempotency;
- audit atômico;
- Project Repository;
- Mission Repository;
- Checkpoint e Evidence mínimos;
- Mission Core com transições básicas;
- bootstrap/recovery.

### Testar

- falha antes e depois de cada passo da transação;
- restart entre commit e publish;
- comando duplicado;
- payload conflitante;
- rebuild de Read Model;
- missão aceita sobrevive a reinício;
- project_id isola dados.

### Gate de saída

Nenhuma janela de estado sem evento/outbox e recovery reproduzível.

## 7. F2 — Policy, portões, estados e Proof Engine

### Entregar

- Admission;
- Mission state machine completa;
- Policy evaluator versionado;
- Capability evaluator;
- três classes de espera;
- EffectIntent;
- EvidenceManifest;
- Proof Gate framework;
- ProofVerdict;
- consumo de verdict pelo Mission Core;
- limites de tentativa, estagnação e replanejamento.

### Testar

- transição inválida;
- verdict obsoleto;
- Brain/Worker/Proof Engine tentando gravar estado;
- aprovação fora do escopo;
- gasto sem aprovação;
- efeito irreversível sem aprovação;
- WAITING_EXTERNAL e retomada;
- repetição de estratégia;
- IMPOSSIBLE_PROVEN com e sem prova suficiente.

### Gate de saída

Somente Mission Core pode criar MISSION_PROVEN ou estado terminal.

## 8. F3 — Primeira fatia vertical

### Missão controlada

Receber um projeto mínimo, produzir um artefato determinístico, validar um critério, reiniciar no meio do fluxo, retomar, gerar Evidence Pack, obter ProofVerdict e transicionar para MISSION_PROVEN.

### Entregar

- Command API própria;
- executável nativo `pod` e Terminal Soberano mínimo;
- serviço persistente separado do processo do terminal;
- Query API;
- Read Model;
- painel funcional simples;
- Engine determinístico de teste;
- Artifact Manifest;
- Evidence Pack;
- health funcional.

### Falhas obrigatórias

- fechar painel;
- fechar terminal durante missão;
- iniciar sem ChatGPT e sem MCP externo;
- repetir comando;
- encerrar processo antes da publicação da outbox;
- reiniciar processo;
- entregar verdict de versão antiga.

### Gate de saída

Uma missão real e reproduzível, criada e comprovada pelo executável `pod`, atinge
MISSION_PROVEN após fechamento do terminal e restart do runtime, sem ChatGPT, sem
MCP externo, sem duplicação e sem bypass.

## 9. F4 — Engine local e Construction Engineering

### Entregar

- WorkUnit DAG;
- plan compiler;
- Engine local;
- sandbox e allowlist;
- timeout/cancel;
- attempt lifecycle;
- coleta de stdout/stderr por referência;
- Artifact Store;
- test/correct loop;
- EffectIntent para efeitos externos.

### Testar

- processo preso;
- cancelamento;
- timeout com processo filho;
- arquivo bloqueado;
- resultado externo ambíguo;
- rollback de alteração;
- Worker não acessa capability ausente.

### Gate de saída

Construção local pequena é segura, recuperável e evidenciada.

## 10. F5 — Governor, Scheduler e concorrência

### Entregar

- priority e quota;
- resource sampling;
- Scheduler;
- lease;
- heartbeat;
- generation/fencing;
- retry/backoff;
- circuit breaker;
- dead-letter e reconcile;
- progress truth.

### Testar

- 1, 2, 4 e maior concorrência suportada;
- Worker morto;
- lease expirado;
- geração obsoleta;
- starvation;
- pressão de CPU/RAM/disco;
- shutdown gracioso.

### Gate de saída

Concorrência aumenta capacidade sem duplicar efeito nem perder estado.

## 11. F6 — Brain inicial e conhecimento

### Entregar

- Brain orchestration;
- context builder;
- Knowledge Store;
- provenance/trust/validity;
- strategy fingerprint;
- planner/replanner;
- uma porta de provider ou motor local substituível.
- modo determinístico/local que preserve o núcleo quando APIs externas faltarem.

### Testar

- conteúdo tenta alterar policy;
- conhecimento stale;
- contexto excede limite;
- estratégia repetida;
- provider indisponível;
- Brain tenta certificar resultado.

### Gate de saída

Brain planeja e replaneja sem adquirir autoridade operacional.

## 12. F7 — Multi-provider

### Entregar

- Provider Capability Registry;
- Policy Router;
- Provider Router;
- adapters;
- no mínimo dois adapters de fornecedores independentes para provar portabilidade;
- health funcional;
- custo e privacidade;
- context portability;
- fallback;
- shadow/challenger opcional.

### Testar

- failover;
- divergência entre modelos;
- orçamento;
- privacy class;
- rate limit;
- adapter incompatível;
- fornecedor indisponível.

### Gate de saída

Troca de fornecedor não altera domínio, policy ou memória soberana.

## 13. F8 — Federação

### Entregar

- Node Registry;
- enrollment;
- identidade;
- version negotiation;
- capability advertisement;
- lease authority;
- secure dispatch;
- partition handling;
- offline delegation;
- reconciliation.

### Testar

- nó falso;
- nó revogado;
- partição;
- clock skew;
- restart de nó;
- stale generation;
- shared mutation offline;
- protocolo incompatível.

### Gate de saída

Federação amplia execução sem criar segunda fonte de verdade.

## 14. F9 — Engines multiplataforma

### Entregar

- ports de filesystem, process, network e privilege;
- adapters por sistema operacional aprovado;
- capability discovery;
- paths e quoting seguros;
- packaging.

### Testar

- suíte de contrato comum;
- permissões;
- sinais e processos filhos;
- diferenças de filesystem;
- instalação limpa;
- rollback.

### Gate de saída

Cada plataforma aprovada cumpre os mesmos contratos.

## 15. F10 — Segurança avançada

### Entregar

- Immune System;
- correlation/detection;
- quarantine;
- revocation orchestration;
- incident playbooks;
- supply-chain gates avançados;
- security dashboard;
- forensics/evidence.

### Testar

- prompt injection;
- credential exposure;
- pacote adulterado;
- nó comprometido;
- privilégio indevido;
- resposta e recuperação.

### Gate de saída

Incidente é detectado, contido, recuperado e auditado.

## 16. F11 — Learning e Training

### Entregar

- Learning Candidate;
- promotion workflow;
- Training Eligibility Gate;
- dataset versionado;
- avaliação e rollback;
- separação conhecimento/policy.

### Testar

- poisoning;
- dado secreto;
- dado não elegível;
- regressão do modelo;
- promoção sem evidência.

### Gate de saída

Aprendizado melhora capacidade sem alterar autoridade ou vazar dados.

## 17. F12 — Product Testing, Security e Delivery

### Entregar

- Product Contract;
- test strategy generator;
- functional/quality/security/recovery gates;
- SBOM e licença quando aplicável;
- Artifact Promotion;
- Delivery Manifest;
- instalação e rollback do produto.

### Gate de saída

Produto só é promovido com conjunto aplicável comprovado.

## 18. F13 — Update, Backup e DR

### Entregar

- backup/restore;
- migração;
- pacote de update;
- side-by-side;
- health gate;
- rollback;
- preservação de missões;
- disaster recovery.

### Gate de saída

Update e desastre simulados não perdem missão, evidência ou possibilidade de rollback.

## 19. F14 — Performance, carga, partição e chaos

Testar limites reais:

- concorrência;
- fila acumulada;
- disco cheio;
- store indisponível;
- provider lento;
- partição de rede;
- churn de nós;
- corrupção detectável;
- recuperação prolongada;
- custo.

Capacidade publicada deve corresponder à medição, não a estimativa.

## 20. F15 — E2E soberano

Missão:

~~~text
RECEBER PRODUTO CONTROLADO
→ ADMITIR
→ PLANEJAR
→ CONSTRUIR
→ TESTAR
→ INJETAR FALHAS
→ RECUPERAR
→ PROTEGER
→ ENTREGAR
→ PROVAR
→ MISSION_PROVEN
~~~

Deve incluir queda do painel, canal, processo, nó e provider, além de reboot seguro e restore.

## 21. Definition of Done por fase

- requisitos aplicáveis atualizados;
- contratos versionados;
- testes focais e regressão verdes;
- falhas obrigatórias injetadas;
- threat review atualizado;
- nenhum segredo exposto;
- evidência persistida;
- checkpoint válido;
- documentação real;
- rollback comprovado quando aplicável;
- nenhuma falha crítica aberta.

## 22. Proibições

- escolher microserviços por desenho lógico;
- adiar segurança necessária;
- aumentar concorrência antes de idempotência/fencing;
- integrar vários providers antes de uma porta estável;
- federar antes de provar nó local;
- marcar requisito ACCEPTED sem evidência;
- confundir F3 com conclusão do produto inteiro;
- aguardar F15 para executar o primeiro E2E.

## 23. Próxima ação após este documento

Com G0 validado, a próxima ação é definir e comprovar a stack física por ADR e benchmark. Nenhum código de produção deve anteceder essa decisão.
