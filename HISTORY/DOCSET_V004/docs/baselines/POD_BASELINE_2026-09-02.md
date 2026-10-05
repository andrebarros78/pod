# POD — BASELINE ARQUITETURAL 02/09/2026

**Identificador:** POD-2026-09-02
**Tipo:** BASELINE_TAG_RECORD
**Status:** SUPERSEDED
**Data:** 2026-09-02
**Produto:** POD — Plataforma Orquestradora Durável
**Substituído por:** POD_BASELINE_V003_2026-09-02.md
**Uso:** histórico e rastreabilidade; não orienta implementação nova

---

## 1. Identidade

POD é um sistema soberano de construção de software. Recebe um objetivo/projeto, interpreta, planeja, constrói, executa, testa, corrige, integra, audita, valida e somente conclui quando o resultado estiver comprovado.

POD não é um chatbot, um simples executor de comandos, uma fila isolada ou uma sessão dependente de conexão externa.

---

## 2. Pilares

1. Autonomia
2. Persistência
3. Constância
4. Loop Engineering

A autonomia opera dentro de políticas explícitas. A persistência impede perda de estado. A constância impede abandono por falha recuperável. O Loop Engineering mantém avanço verificável até a conclusão.

---

## 3. Regra de conclusão

Nenhum processo, serviço, Worker, comando ou teste isolado é prova de conclusão.

MISSION_PROVEN exige, conforme aplicável:

- resultado funcional;
- critérios de aceite satisfeitos;
- testes reais aprovados;
- regressão aprovada;
- evidências persistidas;
- estado final reconciliado;
- checkpoint final;
- ausência de falhas críticas abertas.

---

## 4. Arquitetura soberana

A arquitetura lógica do POD é composta por:

- Cérebro;
- Coração;
- Memória;
- Engenharia de Construção;
- Federação;
- motores de execução;
- interfaces operacionais;
- segurança, recuperação e observabilidade transversais.

Princípio:

`1 CÉREBRO + 1 CORAÇÃO + 1 MEMÓRIA + 1 FEDERAÇÃO + MOTORES DE EXECUÇÃO = POD`

---

## 5. Cérebro

Responsável por:

- compreender intenção e objetivo;
- interpretar projeto e contexto;
- raciocinar e planejar;
- decompor e priorizar trabalho;
- selecionar conhecimento necessário;
- avaliar resultados e evidências;
- replanejar diante de falhas;
- decidir tecnicamente dentro da política;
- determinar quando a missão atingiu prova suficiente.

O Cérebro não executa diretamente ações físicas do sistema operacional.

---

## 6. Engenharia de Construção POD

A Engenharia de Construção é nativa do POD e transforma decisões do Cérebro em construção técnica executável e verificável.

Ela não depende estruturalmente de agente, CLI, produto ou fornecedor externo de programação.

Princípios:

- simplicidade arquitetural;
- contexto sob demanda;
- exploração progressiva do projeto;
- máquina de estados explícita;
- ação pequena e verificável;
- tool loop fechado;
- falha como informação;
- testes contínuos;
- segurança contextual;
- paralelismo isolado;
- regressão obrigatória;
- conclusão por evidência.

Fluxo-base:

`OBJETIVO → CLASSIFICAR → SELECIONAR CONTEXTO → INSPECIONAR → PLANEJAR → EXECUTAR → OBSERVAR → TESTAR → DIAGNOSTICAR/CORRIGIR → REGREDIR → EVIDENCIAR → CHECKPOINT → CONTINUAR → MISSION_PROVEN`

---

## 7. Limites claros de módulo

Cada módulo deve possuir:

- uma responsabilidade principal;
- contrato explícito de entrada;
- contrato explícito de saída;
- autoridade delimitada;
- estado observável;
- testes próprios.

Nenhum módulo pode assumir silenciosamente autoridade pertencente a outro.

---

## 8. Coração

O Coração governa a continuidade operacional e inclui responsabilidades como:

- Governor;
- Scheduler;
- Supervisor;
- Watchdog;
- Recovery;
- Resource Manager;
- prioridades;
- leases;
- fencing;
- retries;
- backoff;
- circuit breakers;
- health/readiness;
- reconciliação;
- incidentes.

Princípio crítico: atividade não é resultado.

`Worker vivo != missão avançando`

`Serviço Running != sistema saudável`

`Retry ocorrendo != recuperação comprovada`

---

## 9. Memória soberana

POD possui uma memória lógica soberana, organizada em planos:

- documental;
- operacional;
- conhecimento;
- evidências;
- checkpoints;
- histórico;
- aprendizado.

Regra de mutação soberana:

`VALIDAR → PERSISTIR → COMMIT → REGISTRAR EVENTO → CONFIRMAR`

Nenhuma operação mutável deve confirmar sucesso antes da persistência soberana.

---

## 10. Biblioteca de Conhecimento POD

A Biblioteca de Conhecimento é o repositório técnico permanente usado pelo Cérebro e pela Engenharia de Construção.

Exemplos de domínios:

- Engenharia de Software;
- Segurança Cibernética;
- Arquitetura de Software;
- Windows;
- Linux;
- Redes;
- Bancos de Dados;
- DevOps;
- Testes;
- Observabilidade;
- Recuperação de Sistemas.

Separação obrigatória:

`BIBLIOTECA DE CONHECIMENTO = ensina o POD`

`DOCUMENTAÇÃO DO PROJETO = explica um projeto`

`POLÍTICA/CONSTITUIÇÃO = determina o que o POD pode e deve fazer`

Conhecimento comum não possui autoridade para substituir políticas soberanas.

---

## 11. Ingestão de conhecimento

Pipeline:

`RECEBER → VALIDAR → ANALISAR SEGURANÇA → CLASSIFICAR → DEFINIR ESCOPO → SHA-256 → VERSIONAR → INDEXAR → TESTAR RECUPERAÇÃO/CONSULTA → ATIVAR`

Estados previstos:

- IMPORTED;
- VALIDATING;
- ACTIVE;
- QUARANTINED;
- SUPERSEDED;
- REVOKED.

O conteúdo canônico deve permanecer versionado; índices e embeddings, quando existirem, são derivados reconstruíveis e nunca a fonte soberana.

---

## 12. Multiprojeto

Uma instalação POD pode operar múltiplos projetos.

A separação acontece por identidade e cápsula de projeto, especialmente `project_id`.

Cada projeto isola, conforme aplicável:

- documentos;
- estado;
- tarefas;
- dependências;
- workspace;
- checkpoints;
- evidências;
- artefatos;
- permissões e referências de credenciais;
- limites e quotas.

Serviços centrais podem ser compartilhados sem compartilhar o estado lógico de projetos.

---

## 13. Terminal POD

O Terminal é a interface operacional primária do POD e existe antes da dependência de um painel web completo.

Funções mínimas:

- status;
- projetos;
- projeto atual;
- missões e tarefas;
- motores e nós;
- cofre;
- Biblioteca de Conhecimento;
- evidências;
- incidentes;
- diagnóstico;
- recuperação;
- ajuda.

O Terminal não acessa banco, Vault, processos críticos ou Workers diretamente. Toda mutação passa pela Command/API/IPC interna e pelas políticas do Core.

---

## 14. Painel

O Painel é interface de visualização, acompanhamento, consulta e intervenção por exceção.

Princípios:

- não é fonte da verdade;
- não escreve diretamente no banco operacional;
- não acessa segredo em texto claro;
- não executa ferramentas diretamente;
- fechar o painel não interrompe a POD;
- comandos passam pelo Core.

---

## 15. Vault e segredos

Segredos devem:

- ser inseridos sem eco;
- não entrar em histórico de terminal;
- não aparecer em logs;
- não aparecer em evidências;
- não ficar em configuração comum;
- não ser exibidos integralmente no painel;
- ser usados por referência controlada.

O Core e os módulos recebem referência/identidade do segredo, nunca dependem da exposição do valor em texto claro.

---

## 16. Elevação administrativa

O Core não permanece elevado.

Operações administrativas passam por um Executor Privilegiado POD com:

- identidade;
- escopo;
- política;
- ACL;
- task_id/correlation_id;
- auditoria;
- resultado;
- rollback quando aplicável.

Não desabilitar nem contornar proteções do sistema operacional para obter autonomia.

---

## 17. Federação

A Federação fornece identidade, descoberta, capacidades, roteamento e reconciliação entre nós.

Cada nó possui, no mínimo:

- node_id;
- nome lógico;
- identidade criptográfica quando aplicável;
- sistema operacional;
- capabilities;
- estado;
- recursos;
- conectividade;
- health/readiness.

O operador deve poder direcionar execução por nome lógico, sem precisar conhecer IP, PID ou caminho interno.

---

## 18. Motores de execução

Os motores nativos são organizados por plataforma/capacidade, incluindo inicialmente:

- POD Windows Engine;
- POD Linux Engine.

Runtime local mínimo:

- identity;
- capability registry;
- local queue;
- cache;
- executor;
- journal;
- checkpoint;
- local watchdog;
- reconnect/reconcile.

Se desconectado, o motor pode concluir trabalho previamente autorizado quando seguro, persistir resultado e reconciliar na reconexão. Não inventa nova missão soberana.

---

## 19. Conectividade externa

Canais externos são adaptadores e não fazem parte da soberania de execução.

Princípios:

- conexão não é execução;
- tarefa aceita e persistida continua localmente;
- canais externos não controlam Workers diretamente;
- canais diferentes convergem para o mesmo Command Ingress;
- idempotência impede duplicação;
- falha de canal não deve apagar missão.

---

## 20. Persistência e mensageria

A arquitetura deve suportar:

- Command Inbox durável;
- idempotência;
- eventos imutáveis;
- State Store;
- Outbox transacional;
- ACK;
- retries;
- backoff;
- dead-letter quando necessário;
- leases;
- fencing tokens;
- checkpoints;
- deduplicação;
- reconciliação.

---

## 21. Recuperação

Regra:

`FALHA NÃO SIGNIFICA ABANDONO`

Fluxo:

`DETECTAR → CONTER → PRESERVAR ESTADO → DIAGNOSTICAR → RECUPERAR → VALIDAR → RETOMAR → AUDITAR`

A recuperação deve usar restart budget, backoff, circuit breaker e evidência. Reinício infinito é proibido.

---

## 22. Segurança

Princípio:

`AUTONOMIA + IDENTIDADE + ESCOPO + POLÍTICA + ISOLAMENTO + AUDITORIA + ROLLBACK = OPERAÇÃO SEGURA`

Nenhuma entidade é confiável apenas por estar na mesma máquina. Identidade válida também não implica autoridade global.

---

## 23. Humano por exceção

Ações técnicas rotineiras, reversíveis e dentro de escopo autorizado podem prosseguir autonomamente.

Portões humanos permanecem para situações como:

- gasto novo;
- criação de conta externa;
- credencial;
- MFA/CAPTCHA;
- produção quando não previamente autorizada;
- exposição pública;
- ação externa irreversível;
- decisão jurídica/comercial;
- ação física.

Um portão bloqueia somente o ramo afetado; trabalhos independentes continuam.

---

## 24. Ferramentas e fornecedores

Ferramentas são capacidades substituíveis, nunca soberania.

A arquitetura do POD não pode depender estruturalmente de um fornecedor, agente, CLI ou modelo específico.

Adapters e portas devem permitir substituição sem alterar domínio e regras soberanas.

---

## 25. ZERO DONOR COUPLING

Regra absoluta para absorção de tecnologia pré-existente:

Todo ativo proveniente de projeto anterior deve ser convertido em capacidade nativa do POD.

O produto final não pode conter vínculo de build, runtime, configuração, dados, serviço, nomenclatura, caminho, importação ou operação com projeto doador.

Gate mínimo:

- DONOR_RUNTIME_DEPENDENCIES = 0
- DONOR_CODE_IMPORTS = 0
- DONOR_PATH_REFERENCES = 0
- DONOR_CONFIG_REFERENCES = 0
- DONOR_SERVICE_DEPENDENCIES = 0

A rastreabilidade histórica de migração, quando necessária, deve ficar fora do runtime/build e não pode criar dependência.

---

## 26. Processo de absorção de capacidades existentes

Fluxo:

`INVENTARIAR → ENTENDER → EXTRAIR CAPACIDADE → COMPARAR → NORMALIZAR → REMOVER ACOPLAMENTO → INTEGRAR → TESTAR → REGREDIR → ACEITAR`

Princípio adicional:

`PRESERVAR → COMPARAR → FUNDIR → APERFEIÇOAR → TESTAR → REGREDIR → MIGRAR → COMPROVAR`

Nenhuma capacidade comprovada deve ser descartada antes de substituição equivalente ou superior ser provada.

---

## 27. Estrutura lógica inicial

A organização conceitual inicial do código é:

```text
src/pod/
├── brain/
├── construction/
├── governor/
├── memory/
├── knowledge/
├── federation/
├── engines/
│   ├── windows/
│   └── linux/
├── terminal/
├── gateway/
├── security/
├── recovery/
└── observability/
```

A árvore física poderá evoluir por ADR, preservando os limites de responsabilidade.

---

## 28. Governança

Mudança arquitetural relevante exige ADR.

Documentação, contrato, implementação, testes e evidências devem permanecer rastreáveis.

Código não substitui documento normativo; documento normativo não substitui teste real.

---

## 29. Regras proibitivas consolidadas

Não implementar:

- múltiplos cérebros soberanos concorrentes;
- múltiplos governadores globais concorrentes;
- múltiplas memórias soberanas concorrentes;
- múltiplos schedulers globais sem delimitação;
- Worker definindo unilateralmente conclusão de missão;
- painel ou terminal como bypass do Core;
- serviço `Running` como prova de saúde funcional;
- conexão externa como condição de continuidade;
- carregamento integral desnecessário da Biblioteca de Conhecimento;
- dependência estrutural de ferramenta/fornecedor externo de construção;
- acoplamento a projetos anteriores;
- MISSION_PROVEN sem evidência.

---

## 30. Baseline

Este documento congela as decisões conceituais e arquiteturais aceitas até 02/09/2026 para orientar a próxima fase de especificação e implementação.

Alterações posteriores exigem registro explícito e, quando estruturais, ADR.

**Baseline:** `POD-2026-09-02`

**Estado:** CONSOLIDATED
