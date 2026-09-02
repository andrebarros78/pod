# POD — BASELINE ARQUITETURAL V003

**Identificador:** POD-DOC-002
**Versão:** 3.0.0
**Status:** ACTIVE
**Data:** 2026-09-02
**Conjunto:** POD-DOCSET-V003
**Autoridade:** A1 — baseline soberana
**Substitui:** POD-2026-09-02 e POD-DOCSET-V002
**Implementação comprovada:** NÃO

## 1. Identidade

POD é a **Plataforma Orquestradora Durável**, concebida como construtor soberano de software.

Recebe uma missão, valida se pode aceitá-la, preserva o compromisso assumido, planeja, constrói, executa, testa, corrige, recupera, audita e somente conclui quando existe prova suficiente e válida.

POD não é:

- chatbot;
- sessão de IA;
- modelo de linguagem;
- fila isolada;
- painel;
- simples executor de comandos;
- produto dependente de conexão contínua com fornecedor externo.

## 2. Estado desta baseline

Esta baseline congela o **projeto conceitual e os contratos lógicos**. Não congela linguagem, banco, framework, barramento, número de processos ou fornecedor.

~~~text
CONCEITO       = ACTIVE
CONTRATOS      = ACTIVE
ARQUITETURA    = ACTIVE
IMPLEMENTAÇÃO  = NOT_STARTED
STACK          = UNDECIDED
~~~

## 3. Invariantes soberanos

1. missão só é aceita após contrato e admissão válidos;
2. missão aceita cria obrigação durável de buscar conclusão;
3. falha recuperável não encerra missão;
4. progresso deriva de mudança verificável, não de atividade;
5. conclusão positiva exige MISSION_PROVEN;
6. Cérebro não executa nem certifica sozinho;
7. Proof Engine avalia prova, mas não altera estado;
8. Mission Core é o único escritor do estado soberano da missão;
9. Policy e segurança podem negar ou conter ação;
10. Governor controla recursos, não redefine objetivo;
11. painel, terminal e API usam os mesmos contratos do Core;
12. confirmação externa só ocorre após persistência atômica;
13. geração obsoleta não pode confirmar mutação compartilhada;
14. transporte opera em at-least-once com idempotência e reconciliação;
15. modelos, CLIs, ferramentas e provedores são capacidades substituíveis;
16. uma instalação pode operar vários projetos isolados;
17. federação distribui execução sem criar soberanias concorrentes;
18. segredo não é conhecimento nem contexto de modelo;
19. documento não prova implementação;
20. código não substitui requisito, teste e evidência.

## 4. Ciclo da missão

~~~text
MISSION_GIVEN
→ RECEIVED
→ ADMISSION
→ MISSION_ACCEPTED
→ RUNNING
→ PROVING
→ PROOF_VERDICT_PASSED
→ MISSION_PROVEN
~~~

Desvios recuperáveis:

~~~text
RUNNING
↔ REPLANNING
↔ RECOVERING
↔ PAUSED
↔ WAITING_EXTERNAL
↔ WAITING_FINANCIAL_AUTHORIZATION
↔ WAITING_OWNER_APPROVAL
~~~

Estados terminais não positivos:

- REJECTED_BEFORE_ACCEPTANCE;
- CANCELLED_BY_OWNER;
- SUPERSEDED;
- TERMINATED_BY_POLICY;
- IMPOSSIBLE_PROVEN.

Nenhuma falha de tentativa, ferramenta, Worker, teste, serviço ou estratégia é terminal por si só.

## 5. Contrato de admissão e convergência

Toda missão aceita deve possuir:

- objective imutável ou versionado;
- acceptance_criteria testáveis;
- constraints;
- policy_version;
- ownership_scope;
- resource_envelope;
- budget_policy;
- approval_policy;
- deadline_policy;
- max_same_strategy_attempts;
- max_stagnation_cycles;
- replan_policy;
- impossibility_proof_policy.

Ausência de prazo pode ser válida. Ausência de limite contra repetição cega não é válida.

Exaurir uma estratégia dispara replanejamento. Exaurir todos os caminhos admissíveis sob as restrições pode produzir candidato a IMPOSSIBLE_PROVEN; o Proof Engine deve comprovar o esgotamento antes da transição terminal.

## 6. Autoridade

| Domínio | Autoridade | Limite |
|---|---|---|
| objetivo, restrições de negócio e orçamento | Owner | não escolhe resultado técnico falso |
| regras soberanas | Constitution/Policy | versionadas e auditáveis |
| estratégia e replanejamento | Brain | não executa, autoriza ou certifica |
| construção técnica | Construction Engineering | atua dentro do plano e da política |
| recursos e prioridade | Governor | não altera objetivo nem prova |
| despacho | Scheduler | não cria trabalho ou autoridade |
| execução | Engine/Worker | produz resultado candidato e evidência |
| prova | Proof Engine | emite verdict, não muda missão |
| estado da missão | Mission Core | transiciona somente com guardas válidas |
| segurança ativa | Security/Immune System | pode negar, conter e quarentenar |
| persistência | Memory | preserva estado, história e evidência |
| roteamento federado | Federation | escolhe destino autorizado |

## 7. Regra de MISSION_PROVEN

MISSION_PROVEN exige, conforme aplicabilidade:

- objetivo alcançado;
- critérios de aceite satisfeitos;
- resultado funcional;
- testes obrigatórios aprovados;
- regressão aprovada;
- segurança aplicável aprovada;
- recuperação aplicável aprovada;
- evidências com proveniência;
- artefatos identificados por hash;
- estado reconciliado;
- checkpoint final válido;
- ausência de falha crítica incompatível;
- ProofVerdict PASSED para a versão exata da missão;
- transição atômica executada pelo Mission Core.

~~~text
WORKER_DONE              != MISSION_PROVEN
PROCESS_RUNNING          != MISSION_PROVEN
MODEL_SAYS_SUCCESS       != MISSION_PROVEN
CODE_CREATED             != MISSION_PROVEN
TEST_ISOLATED_PASSED     != MISSION_PROVEN
PROOF_VERDICT_WITHOUT_COMMIT != MISSION_PROVEN
~~~

## 8. Persistência

Toda mutação material usa uma única fronteira transacional local:

~~~text
VALIDATE
→ BEGIN
→ WRITE aggregate_state_and_version
→ APPEND immutable_domain_event
→ WRITE outbox_message
→ WRITE idempotency_and_audit_record
→ COMMIT
→ PUBLISH
→ CONFIRM
~~~

Estado atual e histórico não são gravações independentes: pertencem ao mesmo commit. O barramento é transporte, nunca fonte de verdade.

Falha antes do commit não produz confirmação. Falha após o commit é recuperada pela outbox sem repetir o efeito de domínio.

## 9. Identidade, tempo e concorrência

- identificadores soberanos usam UUIDv7;
- Task não é entidade concorrente: o nome canônico é WorkUnit;
- UTC persistido representa instante;
- relógio monotônico mede duração somente dentro do mesmo processo vivo;
- lease persistido usa issued_at_utc, expires_at_utc, authority_epoch, generation e fencing_token;
- toda validação distribuída considera incerteza de relógio;
- geração antiga pode preservar resultado como candidato, mas não confirmar estado compartilhado.

## 10. Escopos independentes

Cada ativo declara dimensões distintas:

- ownership_scope: GLOBAL_POD, PROJECT, MISSION ou NODE_LOCAL;
- confidentiality: PUBLIC, INTERNAL, CONFIDENTIAL ou SECRET;
- training_eligibility: DENIED, ALLOWED_WITH_REDACTION ou ALLOWED;
- execution_effect: READ_ONLY, REVERSIBLE_LOCAL, SHARED_MUTATION ou EXTERNAL_IRREVERSIBLE.

Essas dimensões não podem ser comprimidas em um único campo scope.

## 11. Segurança desde a fundação

F0–F2 devem conter o núcleo mínimo:

- identidade;
- autenticação das fronteiras existentes;
- autorização por capability e escopo;
- policy_version;
- isolamento de projeto;
- redaction;
- referência segura a segredos;
- auditoria imutável;
- safe defaults;
- idempotência e fencing;
- portões humanos.

O Sistema Imunológico avançado continua em fase posterior, mas nenhum componente nasce sem o núcleo de segurança.

## 12. Portões e dependências

### Aprovação financeira

Gasto, assinatura, licença, API paga, contratação ou obrigação financeira não autorizada geram WAITING_FINANCIAL_AUTHORIZATION.

### Aprovação soberana do Owner

Produção não autorizada, exposição pública, ação externa irreversível, mudança destrutiva, aumento de privilégio, decisão jurídica/comercial ou alteração do objetivo geram WAITING_OWNER_APPROVAL.

### Dependência externa

Credencial ausente, MFA, CAPTCHA, ação física, hardware ou conexão indispensável indisponível geram WAITING_EXTERNAL.

O POD nunca contorna portão. Apenas o ramo dependente aguarda; ramos seguros e independentes continuam.

## 13. Multiprojeto e federação

Uma instalação POD pode operar múltiplos projetos. Cada comando, evento, estado, evidência, segredo, artefato e custo deve carregar project_id e cumprir isolamento.

A federação:

- não cria outro Cérebro soberano;
- não cria outro Mission Core para a mesma autoridade de missão;
- usa identidade de nó, capability, lease, generation e fencing;
- aceita operação offline somente dentro de delegação pré-emitida e finita;
- reconcilia por causalidade, versão e autoridade, nunca por last-write-wins cego.

## 14. Ferramentas, IA e conhecimento

- Provider Router fica atrás de Policy Router;
- nenhum fornecedor é o Cérebro;
- contexto é portável e controlado pelo POD;
- saída de modelo é proposta, não autorização;
- conhecimento possui proveniência, confiança, validade e classificação;
- conteúdo externo não substitui Constitution/Policy;
- segredo nunca é enviado a modelo sem contrato explícito e autorização.

## 15. Painel e verdade operacional

Painel, Launcher, Terminal e APIs:

- consultam Read Models reconstruíveis;
- enviam comandos ao mesmo ingress;
- não gravam diretamente no banco;
- mostram bloqueio, fase, progresso real e evidência;
- não convertem fechamento da interface em encerramento da missão.

## 16. Construção incremental

A primeira prova vertical deve ocorrer cedo com:

- um projeto;
- uma missão;
- um nó local;
- um Engine determinístico;
- persistência atômica;
- um critério de aceite;
- um ProofVerdict;
- uma transição MISSION_PROVEN;
- reinício e retomada comprovados.

O domínio nasce multiprojeto e federável; a complexidade física é adicionada somente após a fatia local estar comprovada.

## 17. ZERO DONOR COUPLING

Capacidades de projetos anteriores podem ser estudadas e reimplementadas, mas:

- código não é copiado sem análise de licença e adequação;
- runtime, caminhos, serviços, bancos e identidades doadores não viram dependência;
- comportamento absorvido recebe contrato e teste próprios;
- nenhuma falha histórica é importada como requisito.

## 18. Gate para iniciar implementação

Antes de escolher a stack ou iniciar F0:

- DOCSET V003 íntegro;
- ADRs ativos completos;
- autoridade sem conflito;
- máquina de estados e guardas definidas;
- persistência atômica definida;
- matriz requisito-teste completa;
- plano reordenado;
- núcleo de segurança em F0–F2;
- validador documental aprovado.

## 19. Baseline

Esta baseline é a autoridade conceitual ativa do POD.

**Baseline:** POD-DOCSET-V003
**Posição:** READY_FOR_STACK_DECISION somente após todos os gates documentais passarem.
**Implementação:** não iniciada.
