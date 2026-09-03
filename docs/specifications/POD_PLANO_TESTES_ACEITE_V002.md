# POD — PLANO MESTRE DE TESTES E ACEITE — V002

**Identificador:** POD-DOC-010
**Versão:** 2.1.0
**Status:** ACTIVE
**Data:** 2026-09-03
**Conjunto:** POD-DOCSET-V003
**Autoridade:** A3 — prova e aceite
**Substitui:** Plano Mestre de Testes V001
**Implementação comprovada:** NÃO

## 1. Regra

~~~text
TEST WITHOUT CRITERION = INCONCLUSIVE
TEST WITHOUT EVIDENCE = NOT_PROVEN
EVIDENCE WITHOUT PROVENANCE = INVALID
SINGLE SUCCESS = NOT_STABILITY
~~~

Os testes de documentação T-DOC podem ser executados agora. Os demais são contratos obrigatórios para a implementação futura e permanecem PLANNED.

## 2. Registro de execução

Cada execução preserva:

~~~text
test_run_id
test_id
requirement_ids
environment
source_revision
schema_versions
started_at_utc
ended_at_utc
inputs
procedure_version
expected
observed
exit_status
evidence_refs
result
limitations
~~~

Resultados: PASSED, FAILED, BLOCKED, INCONCLUSIVE, NOT_APPLICABLE.

## 3. Ambientes

- UNIT — regras puras;
- COMPONENT — adapter ou módulo isolado;
- INTEGRATION — componentes reais conectados;
- E2E — fluxo completo controlado;
- FAILURE — injeção de falha;
- SECURITY — cenário hostil isolado;
- RECOVERY — restart, restore e reconciliação;
- PERFORMANCE — carga e capacidade.

Teste destrutivo nunca usa produção.

## 4. Catálogo documental

| ID | Cenário | Resultado obrigatório |
|---|---|---|
| T-DOC-001 | manifesto e hashes | arquivos, tamanhos e hashes correspondem |
| T-DOC-002 | links relativos | nenhum link local quebrado |
| T-DOC-003 | IDs e versões | nenhum ID ativo duplicado |
| T-DOC-004 | referências requisito-teste | todos os IDs existem |
| T-DOC-005 | invariantes proibidos | nenhum contrato ativo usa sequência ou termo substituído |
| T-DOC-006 | metadados | todo documento ativo possui versão, status, data e ID |
| T-DOC-007 | autoridade documental | um único conjunto está ACTIVE |
| T-DOC-008 | integridade do JSON | manifesto é JSON válido e schema aceito |

## 5. Missão e convergência

| ID | Cenário | Resultado obrigatório |
|---|---|---|
| T-MSN-001 | admissão válida | missão recebe ACCEPTED e contrato fica persistido |
| T-MSN-002 | critério não testável | REJECTED_BEFORE_ACCEPTANCE |
| T-MSN-003 | transição inexistente | STATE_TRANSITION_DENIED sem mutação |
| T-MSN-004 | terminal imutável | tentativa de reabrir terminal é rejeitada |
| T-MSN-005 | falha de tentativa | missão permanece não terminal e replaneja |
| T-MSN-006 | estratégia repetida | limite dispara nova estratégia, não loop |
| T-MSN-007 | estagnação | progress truth detecta e aciona policy |
| T-MSN-008 | impossibilidade insuficiente | IMPOSSIBLE_PROVEN é rejeitado |
| T-MSN-009 | impossibilidade provada | estado terminal com Evidence Manifest |
| T-MSN-010 | cancelamento autorizado | CANCELLED_BY_OWNER auditável |

## 6. Autoridade e prova

| ID | Cenário | Resultado obrigatório |
|---|---|---|
| T-AUT-001 | Brain tenta mudar Mission | autorização negada |
| T-AUT-002 | Worker tenta declarar sucesso | autorização negada |
| T-AUT-003 | Proof Engine tenta mudar Mission | autorização negada |
| T-AUT-004 | Scheduler cria WorkUnit | contrato rejeita |
| T-AUT-005 | Panel grava store | contrato e teste arquitetural rejeitam |
| T-AUT-006 | Governor altera objetivo | autorização negada |
| T-PRF-001 | Evidence Pack válido | ProofVerdict PASSED |
| T-PRF-002 | verdict atual consumido | Mission Core cria MISSION_PROVEN atomicamente |
| T-PRF-003 | verdict de versão antiga | rejeitado |
| T-PRF-004 | evidência sem proveniência | gate falha |
| T-PRF-005 | falha crítica aberta | conclusão bloqueada |
| T-PRF-006 | NOT_APPLICABLE sem motivo | verdict rejeitado |

## 7. Persistência e mensageria

| ID | Cenário | Resultado obrigatório |
|---|---|---|
| T-PER-001 | falha antes do commit | estado, evento e outbox ausentes |
| T-PER-002 | falha após commit antes de publish | estado/evento presentes; outbox retoma |
| T-PER-003 | evento entregue duas vezes | um único efeito no consumidor |
| T-PER-004 | comando repetido igual | mesmo outcome, sem novo efeito |
| T-PER-005 | mesma chave, payload diferente | IDEMPOTENCY_CONFLICT |
| T-PER-006 | rebuild de Read Model | projeção corresponde ao estado esperado |
| T-PER-007 | aggregate/journal divergentes | incidente e bloqueio seguro |
| T-PER-008 | dead letter | visível, preservada e reconciliável |
| T-PER-009 | restart com missão ativa | estado e compromisso preservados |
| T-PER-010 | disco cheio durante transação | sem commit parcial |

## 8. Identidade e multiprojeto

| ID | Cenário | Resultado obrigatório |
|---|---|---|
| T-IDM-001 | UUIDv7 em entidades | formato válido e sem colisão no volume de teste |
| T-IDM-002 | ID externo malformado | validação falha |
| T-IDM-003 | PID usado como ID | contrato rejeita |
| T-PRJ-001 | leitura entre projetos sem capability | negada |
| T-PRJ-002 | escrita entre projetos sem capability | negada |
| T-PRJ-003 | segredo de outro projeto | não retornado e incidente registrado |
| T-PRJ-004 | conhecimento global promovido | origem e autorização preservadas |
| T-PRJ-005 | duas missões de projetos distintos | estado, custo e evidência isolados |

## 9. Portões humanos

| ID | Cenário | Resultado obrigatório |
|---|---|---|
| T-HUM-001 | gasto novo | WAITING_FINANCIAL_AUTHORIZATION |
| T-HUM-002 | alternativa gratuita válida | ramo replaneja sem pedir gasto |
| T-HUM-003 | publicação sem aprovação | WAITING_OWNER_APPROVAL |
| T-HUM-004 | MFA/CAPTCHA | WAITING_EXTERNAL sem contorno |
| T-HUM-005 | approval para payload diferente | negado |
| T-HUM-006 | approval expirado | negado |
| T-HUM-007 | ramo independente | continua durante espera |
| T-HUM-008 | retomada após aprovação | policy e contexto são revalidados |

## 10. Segurança

| ID | Cenário | Resultado obrigatório |
|---|---|---|
| T-SEC-001 | ação sem identidade | negada |
| T-SEC-002 | capability ausente | negada |
| T-SEC-003 | prompt injection | conteúdo não altera policy nem ferramenta |
| T-SEC-004 | segredo em log/event/evidence | scanner falha o gate |
| T-SEC-005 | elevação fora de escopo | negada |
| T-SEC-006 | pacote adulterado | instalação/promoção negada |
| T-SEC-007 | nó revogado | novo lease negado e commit antigo bloqueado |
| T-SEC-008 | approval reutilizado | segundo uso incompatível é negado |
| T-SEC-009 | vulnerabilidade crítica incompatível | release bloqueada |
| T-SEC-010 | quarantine | escopo contido sem apagar evidência |
| T-SEC-011 | audit atômico | ação material não existe sem AuditRecord |

## 11. Distribuição, lease e tempo

| ID | Cenário | Resultado obrigatório |
|---|---|---|
| T-DST-001 | lease expira após restart | expiração continua correta |
| T-DST-002 | clock skew dentro da incerteza | comportamento conservador previsto |
| T-DST-003 | generation antiga | commit rejeitado |
| T-DST-004 | fencing token inferior | commit rejeitado |
| T-DST-005 | partição com READ_ONLY | operação permitida até TTL |
| T-DST-006 | SHARED_MUTATION offline | preservada como candidata |
| T-DST-007 | EXTERNAL_IRREVERSIBLE offline | negada |
| T-DST-008 | TTL offline vencido | capability negada |
| T-DST-009 | protocolo major incompatível | nó não entra em READY |
| T-DST-010 | reconciliação após partição | resultado autoritativo sem last-write-wins cego |
| T-DST-011 | migração de workspace | destino verifica bundle e origem só libera após handover |
| T-DST-012 | micro-scheduler local | não cria WorkUnit nem amplia envelope |

## 12. Engine, processo e recursos

| ID | Cenário | Resultado obrigatório |
|---|---|---|
| T-ENG-001 | comando permitido | saída e evidência vinculadas |
| T-ENG-002 | comando fora da allowlist | negado |
| T-ENG-003 | timeout com filho | árvore é contida e resultado registrado |
| T-ENG-004 | cancelamento | efeito e processo reconciliados |
| T-ENG-005 | arquivo bloqueado | falha classificada e retry governado |
| T-ENG-006 | efeito externo com timeout | UNKNOWN_OUTCOME até reconciliação |
| T-ENG-007 | preempção cooperativa | checkpoint, lease liberado e retomada segura |
| T-ENG-008 | compensação | novo efeito compensatório preserva história original |
| T-RES-001 | pressão de CPU | quota mantém Core responsivo |
| T-RES-002 | pressão de RAM | degradação controlada |
| T-RES-003 | disco quase cheio | prevenção antes de corrupção |
| T-RES-004 | starvation | prioridade não bloqueia indefinidamente missão elegível |
| T-RES-005 | shutdown | checkpoint e drenagem |
| T-RES-006 | fairness multiprojeto | quota e reserva evitam starvation entre projetos |

## 13. Brain, conhecimento e providers

| ID | Cenário | Resultado obrigatório |
|---|---|---|
| T-AI-001 | provider indisponível | fallback ou WAITING_EXTERNAL conforme policy |
| T-AI-002 | contexto classificado | provider incompatível não recebe dado |
| T-AI-003 | orçamento excedido | chamada bloqueada antes do gasto |
| T-AI-004 | conhecimento stale | confiança reduzida e verificação exigida |
| T-AI-005 | modelos divergem | Brain decide por evidência, não votação |
| T-AI-006 | troca de adapter | domínio e memória permanecem |
| T-AI-007 | resposta tenta autorizar ação | tratada como proposta |
| T-AI-008 | strategy fingerprint repetido | limite de repetição acionado |
| T-AI-009 | Budget Ledger | estimativa, consumo e autorização permanecem distinguíveis |

## 14. Independência, IA híbrida e Terminal Soberano

| ID | Cenário | Resultado obrigatório |
|---|---|---|
| T-SOV-001 | iniciar sem credencial ou produto ChatGPT | núcleo READY e terminal operacional |
| T-SOV-002 | iniciar sem servidor MCP externo | núcleo READY; somente adapter afetado fica DEGRADED |
| T-SOV-003 | fechar terminal durante missão | missão continua no serviço persistente |
| T-SOV-004 | fechar painel durante missão | missão continua no serviço persistente |
| T-SOV-005 | reiniciar runtime com missão ativa | missão recuperada e reconciliada |
| T-SOV-006 | derrubar provedor principal | failover preserva policy, privacidade e orçamento |
| T-SOV-007 | derrubar todos os provedores externos | núcleo saudável; somente ramo dependente aguarda |
| T-SOV-008 | trocar GPT por provedor independente | domínio, estado e critérios permanecem |
| T-SOV-009 | modelo solicitar ação proibida | DENY auditado; nenhum efeito executado |
| T-SOV-010 | prompt contradizer Constitution | Constitution prevalece |
| T-SOV-011 | executar comandos em modo humano e `--json` | schema, conteúdo e exit codes válidos |
| T-SOV-012 | perder conexão do terminal e reconectar | acompanhamento retomado sem efeito duplicado |
| T-SOV-013 | consultar prova sem ChatGPT | Evidence Pack reproduzível pelo terminal |
| T-SOV-014 | usar modelo local autorizado | missão compatível independe de API externa |
| T-SOV-015 | atualizar terminal separadamente | runtime e missões permanecem íntegros |
| T-SOV-016 | injetar thread externa como ID soberano | entrada recusada ou mapeada sem substituir ID POD |
| T-SOV-017 | provocar segredo em saída ou log | conteúdo sanitizado e incidente registrado |
| T-SOV-018 | tentar elevar regra via memória aprendida | promoção bloqueada e auditada |

## 15. Interface e verdade operacional

| ID | Cenário | Resultado obrigatório |
|---|---|---|
| T-UI-001 | painel fecha | missão continua |
| T-UI-002 | painel reabre | estado real reconstruído |
| T-UI-003 | comando pelo painel | passa pelo mesmo ingress e policy |
| T-UI-004 | progresso | não aumenta apenas por heartbeat |
| T-UI-005 | bloqueio | motivo, ramo e condição de retomada visíveis |
| T-UI-006 | health | READY depende de função, não apenas processo |

## 16. Recovery, update e operação

| ID | Cenário | Resultado obrigatório |
|---|---|---|
| T-OPS-001 | restart do Core | inbox/outbox reconciliadas e missão retomada |
| T-OPS-002 | reboot do host | compromisso e checkpoint preservados |
| T-OPS-003 | restore de backup | hashes, versions e fencing válidos |
| T-OPS-004 | update válido | missões preservadas |
| T-OPS-005 | update falho | rollback restaura versão saudável |
| T-OPS-006 | configuração inválida | sistema não entra em READY |
| T-OPS-007 | store indisponível | falha fechada sem confirmação falsa |
| T-OPS-008 | canal externo cai | execução local aceita continua |

## 17. Produto e entrega

| ID | Cenário | Resultado obrigatório |
|---|---|---|
| T-PROD-001 | Product Contract | requisitos aplicáveis derivados |
| T-PROD-002 | teste funcional | resultado reproduzível |
| T-PROD-003 | gate de segurança | risco crítico bloqueia promoção |
| T-PROD-004 | Artifact Manifest | hashes e proveniência válidos |
| T-PROD-005 | instalação controlada | produto inicia e health passa |
| T-PROD-006 | rollback do produto | versão anterior restaurada |
| T-PROD-007 | NOT_APPLICABLE | justificativa auditável |
| T-PROD-008 | Evidence Pack final | todos os gates referenciados |

## 18. E2E por marco

### E2E-F3

Um artefato determinístico, restart no meio, outbox retomada, prova e MISSION_PROVEN.

### E2E-F8

Uma WorkUnit em nó federado, partição, reconciliação e stale generation rejeitada.

### E2E-F13

Missão ativa atravessa update e restore.

### E2E-F15

Produto controlado é planejado, construído, testado, protegido, recuperado, entregue e provado.

## 19. Testes prolongados

Duração é definida por risco e objetivo. Resultado de teste curto não sustenta alegação de operação prolongada.

Coletar:

- CPU, RAM e disco;
- crescimento de journal/outbox;
- tentativas e duplicidade;
- latência;
- falhas e recovery;
- custo de providers;
- filas;
- vazamento de processo;
- integridade de estado.

## 20. Gate de release

Release candidata é rejeitada quando:

- requisito crítico não está ACCEPTED;
- teste obrigatório falhou ou não foi executado;
- evidência está ausente;
- segredo foi detectado;
- vulnerabilidade crítica incompatível permanece;
- rollback obrigatório falhou;
- restore obrigatório não foi provado;
- contrato e implementação divergem;
- manifesto é inválido;
- MISSION_PROVEN depende de texto ou ação do construtor.

## 21. Estado inicial

| Grupo | Estado em 2026-09-02 |
|---|---|
| T-DOC | EXECUTÁVEL |
| T-SOV | PLANNED / NOT_IMPLEMENTED |
| Demais testes | PLANNED / NOT_IMPLEMENTED |

Nenhum teste planejado é declarado executado por este documento.
