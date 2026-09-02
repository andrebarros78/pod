# POD — MATRIZ MESTRA DE RASTREABILIDADE E CONFORMIDADE — V002

**Identificador:** POD-DOC-008
**Versão:** 2.0.0
**Status:** ACTIVE
**Data:** 2026-09-02
**Conjunto:** POD-DOCSET-V003
**Autoridade:** A3 — requisitos e conformidade
**Substitui:** matriz V001 de 72 requisitos
**Implementação comprovada:** NÃO

## 1. Finalidade

Ligar requisito, decisão, contrato, fase, teste, evidência e aceite da arquitetura vigente.

~~~text
DEFINED_NOT_IMPLEMENTED
→ IMPLEMENTING
→ IMPLEMENTED_NOT_TESTED
→ TESTED_NOT_EVIDENCED
→ EVIDENCED_NOT_ACCEPTED
→ ACCEPTED
~~~

Nenhum requisito pode saltar diretamente para ACCEPTED.

## 2. Estados

- DEFINED_NOT_IMPLEMENTED;
- IMPLEMENTING;
- IMPLEMENTED_NOT_TESTED;
- TESTED_NOT_EVIDENCED;
- EVIDENCED_NOT_ACCEPTED;
- ACCEPTED;
- BLOCKED;
- DEFERRED;
- NON_COMPLIANT;
- NOT_APPLICABLE.

O DOCSET ativo não prova implementação. Salvo requisitos documentais identificados por REQ-DOC, o estado inicial é DEFINED_NOT_IMPLEMENTED.

## 3. Evidência mínima

Aceite exige:

- source revision;
- test_run_id;
- ambiente;
- resultado observado;
- artefatos ou logs;
- hashes quando aplicável;
- responsável pelo gate;
- ausência de limitação incompatível.

## 4. Documentação e governança

| ID | Requisito e critério de aceite | Fonte | Fase | Teste | Criticidade | Estado |
|---|---|---|---|---|---|---|
| REQ-DOC-001 | Existe um único docset ACTIVE; índice e manifesto concordam | POD-DOC-001 | G0 | T-DOC-001,T-DOC-007 | CRITICAL | ACCEPTED |
| REQ-DOC-002 | Todos os documentos ativos possuem hash, tamanho, ID e versão válidos | POD-DOC-011 | G0 | T-DOC-001,T-DOC-003,T-DOC-006 | CRITICAL | ACCEPTED |
| REQ-DOC-003 | Links relativos e referências internas não estão quebrados | POD-DOC-011 | G0 | T-DOC-002 | HIGH | ACCEPTED |
| REQ-DOC-004 | Requisitos referenciam testes existentes e IDs são únicos | POD-DOC-008 | G0 | T-DOC-003,T-DOC-004 | CRITICAL | ACCEPTED |
| REQ-DOC-005 | Termos e invariantes substituídos não aparecem como regra ativa | POD-DOC-001 | G0 | T-DOC-005 | CRITICAL | ACCEPTED |
| REQ-DOC-006 | ADR estrutural possui contexto, alternativas, decisão, migração, rollback, segurança e evidência | POD-DOC-011 | G0 | T-DOC-006 | HIGH | ACCEPTED |

## 5. Missão e convergência

| ID | Requisito e critério de aceite | Fonte | Fase | Teste | Criticidade | Estado |
|---|---|---|---|---|---|---|
| REQ-MSN-001 | Missão só entra em ACCEPTED com contrato completo e persistido | POD-DOC-006 | F1–F2 | T-MSN-001,T-MSN-002 | CRITICAL | DEFINED_NOT_IMPLEMENTED |
| REQ-MSN-002 | Missão aceita sobrevive a processo, painel, canal e reboot | POD-DOC-003 | F1–F3 | T-PER-009,T-UI-001,T-OPS-001,T-OPS-002 | CRITICAL | DEFINED_NOT_IMPLEMENTED |
| REQ-MSN-003 | Falha recuperável não cria estado terminal | POD-DOC-003 | F2 | T-MSN-005 | CRITICAL | DEFINED_NOT_IMPLEMENTED |
| REQ-MSN-004 | Transições não declaradas são rejeitadas atomicamente | POD-DOC-006 | F2 | T-MSN-003 | CRITICAL | DEFINED_NOT_IMPLEMENTED |
| REQ-MSN-005 | Estado terminal é imutável e correção cria missão sucessora | POD-DOC-006 | F2 | T-MSN-004 | HIGH | DEFINED_NOT_IMPLEMENTED |
| REQ-MSN-006 | Mesma estratégia e estagnação possuem limites obrigatórios | POD-DOC-002 | F2 | T-MSN-006,T-MSN-007 | CRITICAL | DEFINED_NOT_IMPLEMENTED |
| REQ-MSN-007 | IMPOSSIBLE_PROVEN exige prova de esgotamento dos caminhos admissíveis | POD-DOC-006 | F2 | T-MSN-008,T-MSN-009 | CRITICAL | DEFINED_NOT_IMPLEMENTED |
| REQ-MSN-008 | Cancelamento do Owner é específico, autorizado e auditado | POD-DOC-006 | F2 | T-MSN-010 | HIGH | DEFINED_NOT_IMPLEMENTED |

## 6. Autoridade e prova

| ID | Requisito e critério de aceite | Fonte | Fase | Teste | Criticidade | Estado |
|---|---|---|---|---|---|---|
| REQ-AUT-001 | Brain planeja, mas não escreve estado soberano | ADR-003 | F2,F6 | T-AUT-001 | CRITICAL | DEFINED_NOT_IMPLEMENTED |
| REQ-AUT-002 | Worker produz fatos, mas não declara missão concluída | ADR-003 | F2,F4 | T-AUT-002 | CRITICAL | DEFINED_NOT_IMPLEMENTED |
| REQ-AUT-003 | Proof Engine somente emite ProofVerdict | ADR-003 | F2 | T-AUT-003,T-PRF-001 | CRITICAL | DEFINED_NOT_IMPLEMENTED |
| REQ-AUT-004 | Mission Core é o único escritor da Mission | ADR-003 | F1–F2 | T-AUT-001,T-AUT-002,T-AUT-003 | CRITICAL | DEFINED_NOT_IMPLEMENTED |
| REQ-AUT-005 | Scheduler não cria WorkUnit nem amplia capability | POD-DOC-005 | F5 | T-AUT-004 | HIGH | DEFINED_NOT_IMPLEMENTED |
| REQ-AUT-006 | Governor não altera objetivo nem fabrica progresso | POD-DOC-002 | F5 | T-AUT-006,T-UI-004 | HIGH | DEFINED_NOT_IMPLEMENTED |
| REQ-PRF-001 | ProofVerdict vincula missão, critérios, policy e Evidence Manifest exatos | ADR-003 | F2 | T-PRF-001,T-PRF-003 | CRITICAL | DEFINED_NOT_IMPLEMENTED |
| REQ-PRF-002 | MISSION_PROVEN é commit atômico após consumo de verdict válido | ADR-003 | F2–F3 | T-PRF-002 | CRITICAL | DEFINED_NOT_IMPLEMENTED |
| REQ-PRF-003 | Evidência sem proveniência ou hash não satisfaz gate crítico | POD-DOC-006 | F2 | T-PRF-004 | CRITICAL | DEFINED_NOT_IMPLEMENTED |
| REQ-PRF-004 | Falha crítica aberta impede conclusão | POD-DOC-002 | F2 | T-PRF-005 | CRITICAL | DEFINED_NOT_IMPLEMENTED |
| REQ-PRF-005 | NOT_APPLICABLE exige justificativa por gate | POD-DOC-010 | F2,F12 | T-PRF-006,T-PROD-007 | HIGH | DEFINED_NOT_IMPLEMENTED |

## 7. Persistência e dados

| ID | Requisito e critério de aceite | Fonte | Fase | Teste | Criticidade | Estado |
|---|---|---|---|---|---|---|
| REQ-PER-001 | Aggregate, evento, outbox, idempotência e audit usam o mesmo commit | ADR-004 | F1 | T-PER-001,T-PER-002,T-SEC-011 | CRITICAL | DEFINED_NOT_IMPLEMENTED |
| REQ-PER-002 | Confirmação externa ocorre somente após commit | ADR-004 | F1 | T-PER-001,T-PER-002 | CRITICAL | DEFINED_NOT_IMPLEMENTED |
| REQ-PER-003 | Outbox retoma entrega após falha ou restart | ADR-004 | F1 | T-PER-002,T-OPS-001 | CRITICAL | DEFINED_NOT_IMPLEMENTED |
| REQ-PER-004 | Transporte at-least-once não duplica efeito | POD-DOC-006 | F1 | T-PER-003,T-PER-004 | CRITICAL | DEFINED_NOT_IMPLEMENTED |
| REQ-PER-005 | Chave idempotente com payload diferente é conflito | POD-DOC-006 | F1 | T-PER-005 | CRITICAL | DEFINED_NOT_IMPLEMENTED |
| REQ-PER-006 | Read Model pode ser reconstruído do estado/história válidos | ADR-004 | F1,F3 | T-PER-006 | HIGH | DEFINED_NOT_IMPLEMENTED |
| REQ-PER-007 | Divergência aggregate/journal abre incidente e bloqueia escopo | ADR-004 | F1 | T-PER-007 | CRITICAL | DEFINED_NOT_IMPLEMENTED |
| REQ-PER-008 | Dead letter permanece visível e reconciliável | POD-DOC-006 | F1,F5 | T-PER-008 | HIGH | DEFINED_NOT_IMPLEMENTED |
| REQ-PER-009 | Falha de armazenamento não produz commit parcial | ADR-004 | F1 | T-PER-010 | CRITICAL | DEFINED_NOT_IMPLEMENTED |
| REQ-DAT-001 | Entidades soberanas usam UUIDv7 e não reutilizam IDs | POD-DOC-006 | F0 | T-IDM-001,T-IDM-002 | HIGH | DEFINED_NOT_IMPLEMENTED |
| REQ-DAT-002 | PID, hostname, caminho e título não substituem ID | POD-DOC-006 | F0 | T-IDM-003 | HIGH | DEFINED_NOT_IMPLEMENTED |
| REQ-DAT-003 | WorkUnit é a unidade canônica; Task é apenas rótulo | POD-DOC-006 | F0 | T-DOC-005 | HIGH | DEFINED_NOT_IMPLEMENTED |
| REQ-DAT-004 | Ownership, confidentiality, training e effect são campos distintos | POD-DOC-006 | F0 | T-PRJ-001,T-AI-002 | CRITICAL | DEFINED_NOT_IMPLEMENTED |
| REQ-DAT-005 | Eventos são append-only e correção é compensatória | POD-DOC-006 | F1 | T-PER-006,T-PER-007 | HIGH | DEFINED_NOT_IMPLEMENTED |

## 8. Portões humanos

| ID | Requisito e critério de aceite | Fonte | Fase | Teste | Criticidade | Estado |
|---|---|---|---|---|---|---|
| REQ-HUM-001 | Gasto novo não autorizado bloqueia apenas o ramo dependente | ADR-005 | F2 | T-HUM-001,T-HUM-007 | CRITICAL | DEFINED_NOT_IMPLEMENTED |
| REQ-HUM-002 | Alternativa gratuita adequada é tentada antes de solicitar gasto | ADR-005 | F2,F6 | T-HUM-002 | HIGH | DEFINED_NOT_IMPLEMENTED |
| REQ-HUM-003 | Produção, publicação e efeito irreversível exigem Owner Approval | ADR-005 | F2 | T-HUM-003 | CRITICAL | DEFINED_NOT_IMPLEMENTED |
| REQ-HUM-004 | MFA, CAPTCHA e credencial ausente geram WAITING_EXTERNAL sem contorno | ADR-005 | F2 | T-HUM-004 | CRITICAL | DEFINED_NOT_IMPLEMENTED |
| REQ-HUM-005 | Approval é vinculado a ator, ação, escopo, payload e validade | POD-DOC-007 | F2 | T-HUM-005,T-HUM-006 | CRITICAL | DEFINED_NOT_IMPLEMENTED |
| REQ-HUM-006 | Retomada revalida policy, versão, geração e condição | ADR-005 | F2 | T-HUM-008 | HIGH | DEFINED_NOT_IMPLEMENTED |

## 9. Segurança

| ID | Requisito e critério de aceite | Fonte | Fase | Teste | Criticidade | Estado |
|---|---|---|---|---|---|---|
| REQ-SEC-001 | Security Kernel existe desde F0, antes de Engine, IA ou federação | ADR-007 | F0–F2 | T-SEC-001,T-SEC-002 | CRITICAL | DEFINED_NOT_IMPLEMENTED |
| REQ-SEC-002 | Toda ação material autentica identidade e valida capability | POD-DOC-007 | F0–F2 | T-SEC-001,T-SEC-002 | CRITICAL | DEFINED_NOT_IMPLEMENTED |
| REQ-SEC-003 | Policy usa deny by default e versão persistida | POD-DOC-007 | F2 | T-SEC-002 | CRITICAL | DEFINED_NOT_IMPLEMENTED |
| REQ-SEC-004 | Conteúdo e modelo não alteram Policy nem capability | POD-DOC-007 | F6 | T-SEC-003,T-AI-007 | CRITICAL | DEFINED_NOT_IMPLEMENTED |
| REQ-SEC-005 | Segredo não aparece em Git, log, evento, evidence ou prompt | POD-DOC-007 | F0–F15 | T-SEC-004 | CRITICAL | DEFINED_NOT_IMPLEMENTED |
| REQ-SEC-006 | Elevação é isolada, limitada, auditada e não contorna UAC | POD-DOC-007 | F4,F9 | T-SEC-005 | CRITICAL | DEFINED_NOT_IMPLEMENTED |
| REQ-SEC-007 | Pacote adulterado não é instalado ou promovido | POD-DOC-007 | F12–F13 | T-SEC-006 | CRITICAL | DEFINED_NOT_IMPLEMENTED |
| REQ-SEC-008 | Nó revogado não recebe lease nem confirma geração antiga | POD-DOC-007 | F8 | T-SEC-007 | CRITICAL | DEFINED_NOT_IMPLEMENTED |
| REQ-SEC-009 | Approval não pode ser reutilizado fora do contrato | POD-DOC-007 | F2 | T-SEC-008 | CRITICAL | DEFINED_NOT_IMPLEMENTED |
| REQ-SEC-010 | Vulnerabilidade crítica incompatível bloqueia release | POD-DOC-007 | F10,F12 | T-SEC-009 | CRITICAL | DEFINED_NOT_IMPLEMENTED |
| REQ-SEC-011 | Quarentena contém escopo sem apagar história | POD-DOC-007 | F10 | T-SEC-010 | HIGH | DEFINED_NOT_IMPLEMENTED |

## 10. Multiprojeto

| ID | Requisito e critério de aceite | Fonte | Fase | Teste | Criticidade | Estado |
|---|---|---|---|---|---|---|
| REQ-PRJ-001 | Uma instalação suporta múltiplos projetos no domínio | ADR-008 | F0–F1 | T-PRJ-005 | CRITICAL | DEFINED_NOT_IMPLEMENTED |
| REQ-PRJ-002 | Leitura e escrita cross-project exigem capability explícita | POD-DOC-007 | F1–F2 | T-PRJ-001,T-PRJ-002 | CRITICAL | DEFINED_NOT_IMPLEMENTED |
| REQ-PRJ-003 | Segredo é project-scoped por padrão | POD-DOC-007 | F0–F2 | T-PRJ-003 | CRITICAL | DEFINED_NOT_IMPLEMENTED |
| REQ-PRJ-004 | Promoção para GLOBAL preserva origem e autorização | POD-DOC-006 | F6 | T-PRJ-004 | HIGH | DEFINED_NOT_IMPLEMENTED |
| REQ-PRJ-005 | Estado, custo, evidência e artefato são isolados por projeto | ADR-008 | F1–F7 | T-PRJ-005 | CRITICAL | DEFINED_NOT_IMPLEMENTED |

## 11. Federação, lease e tempo

| ID | Requisito e critério de aceite | Fonte | Fase | Teste | Criticidade | Estado |
|---|---|---|---|---|---|---|
| REQ-DST-001 | Referência monotônica nunca é persistida ou comparada entre nós | ADR-006 | F0,F8 | T-DST-001,T-DOC-005 | CRITICAL | DEFINED_NOT_IMPLEMENTED |
| REQ-DST-002 | Lease usa UTC, uncertainty, epoch, generation e fencing | ADR-006 | F5,F8 | T-DST-001,T-DST-002 | CRITICAL | DEFINED_NOT_IMPLEMENTED |
| REQ-DST-003 | Generation ou fencing obsoleto falha no ponto de commit | ADR-006 | F5,F8 | T-DST-003,T-DST-004 | CRITICAL | DEFINED_NOT_IMPLEMENTED |
| REQ-DST-004 | Delegação offline possui TTL finito e não se autorrenova | ADR-006 | F8 | T-DST-005,T-DST-008 | CRITICAL | DEFINED_NOT_IMPLEMENTED |
| REQ-DST-005 | Shared mutation offline permanece candidata até reconcile | ADR-006 | F8 | T-DST-006 | CRITICAL | DEFINED_NOT_IMPLEMENTED |
| REQ-DST-006 | Efeito externo irreversível offline é negado | ADR-006 | F8 | T-DST-007 | CRITICAL | DEFINED_NOT_IMPLEMENTED |
| REQ-DST-007 | Protocolo major incompatível impede READY | POD-DOC-006 | F8 | T-DST-009 | HIGH | DEFINED_NOT_IMPLEMENTED |
| REQ-DST-008 | Reconciliação usa causalidade e autoridade, não LWW cego | ADR-006 | F8 | T-DST-010 | CRITICAL | DEFINED_NOT_IMPLEMENTED |
| REQ-DST-009 | Migração de workspace usa bundle verificado, handover e rollback | POD-DOC-005 | F8 | T-DST-011 | CRITICAL | DEFINED_NOT_IMPLEMENTED |
| REQ-DST-010 | Micro-scheduler opera somente WorkUnits e limites delegados | POD-DOC-006 | F8 | T-DST-012 | CRITICAL | DEFINED_NOT_IMPLEMENTED |

## 12. Execução e recursos

| ID | Requisito e critério de aceite | Fonte | Fase | Teste | Criticidade | Estado |
|---|---|---|---|---|---|---|
| REQ-ENG-001 | Engine executa somente ação permitida pelo envelope | POD-DOC-005 | F4 | T-ENG-001,T-ENG-002 | CRITICAL | DEFINED_NOT_IMPLEMENTED |
| REQ-ENG-002 | Timeout e cancelamento contêm árvore de processos e reconciliam efeito | POD-DOC-009 | F4 | T-ENG-003,T-ENG-004 | CRITICAL | DEFINED_NOT_IMPLEMENTED |
| REQ-ENG-003 | Falha temporária recebe retry governado; permanente não recebe loop | POD-DOC-003 | F4–F5 | T-ENG-005 | HIGH | DEFINED_NOT_IMPLEMENTED |
| REQ-ENG-004 | Efeito externo ambíguo permanece UNKNOWN_OUTCOME até reconcile | POD-DOC-006 | F4 | T-ENG-006 | CRITICAL | DEFINED_NOT_IMPLEMENTED |
| REQ-ENG-005 | Preempção cria safe point, checkpoint e liberação de lease | POD-DOC-006 | F4–F5 | T-ENG-007 | HIGH | DEFINED_NOT_IMPLEMENTED |
| REQ-ENG-006 | Compensação é nova WorkUnit e preserva história original | POD-DOC-006 | F4 | T-ENG-008 | CRITICAL | DEFINED_NOT_IMPLEMENTED |
| REQ-RES-001 | Governor protege responsividade sob pressão de CPU, RAM e disco | POD-DOC-009 | F5 | T-RES-001,T-RES-002,T-RES-003 | HIGH | DEFINED_NOT_IMPLEMENTED |
| REQ-RES-002 | Prioridade não causa starvation indefinida | POD-DOC-009 | F5 | T-RES-004 | HIGH | DEFINED_NOT_IMPLEMENTED |
| REQ-RES-003 | Shutdown drena ou checkpointa trabalho em segurança | POD-DOC-009 | F5 | T-RES-005 | CRITICAL | DEFINED_NOT_IMPLEMENTED |
| REQ-RES-004 | Fairness aplica quota e reserva por projeto | POD-DOC-005 | F5 | T-RES-006 | HIGH | DEFINED_NOT_IMPLEMENTED |

## 13. Brain, conhecimento e providers

| ID | Requisito e critério de aceite | Fonte | Fase | Teste | Criticidade | Estado |
|---|---|---|---|---|---|---|
| REQ-AI-001 | Provider é adapter substituível e não é Brain | POD-DOC-003 | F6–F7 | T-AI-006 | CRITICAL | DEFINED_NOT_IMPLEMENTED |
| REQ-AI-002 | Policy Router filtra privacidade e orçamento antes do Provider Router | POD-DOC-005 | F7 | T-AI-002,T-AI-003 | CRITICAL | DEFINED_NOT_IMPLEMENTED |
| REQ-AI-003 | Indisponibilidade produz fallback seguro ou WAITING_EXTERNAL | POD-DOC-009 | F6–F7 | T-AI-001 | HIGH | DEFINED_NOT_IMPLEMENTED |
| REQ-AI-004 | Conhecimento possui proveniência, confiança e validade | POD-DOC-006 | F6 | T-AI-004 | HIGH | DEFINED_NOT_IMPLEMENTED |
| REQ-AI-005 | Divergência de modelos é arbitrada por evidência, nunca votação cega | POD-DOC-004 | F7 | T-AI-005 | HIGH | DEFINED_NOT_IMPLEMENTED |
| REQ-AI-006 | Output de modelo é proposta e não autorização | POD-DOC-007 | F6 | T-AI-007 | CRITICAL | DEFINED_NOT_IMPLEMENTED |
| REQ-AI-007 | Strategy fingerprint impede repetição improdutiva | POD-DOC-006 | F6 | T-AI-008 | HIGH | DEFINED_NOT_IMPLEMENTED |
| REQ-AI-008 | Budget Ledger separa estimativa, consumo observado e autorização | POD-DOC-006 | F6–F7 | T-AI-009 | HIGH | DEFINED_NOT_IMPLEMENTED |

## 14. Interface e verdade operacional

| ID | Requisito e critério de aceite | Fonte | Fase | Teste | Criticidade | Estado |
|---|---|---|---|---|---|---|
| REQ-UI-001 | Fechar painel não interrompe missão aceita | POD-DOC-004 | F3 | T-UI-001 | CRITICAL | DEFINED_NOT_IMPLEMENTED |
| REQ-UI-002 | Reabrir painel reconstrói estado real | POD-DOC-005 | F3 | T-UI-002 | HIGH | DEFINED_NOT_IMPLEMENTED |
| REQ-UI-003 | Comando de UI usa o mesmo ingress e policy | POD-DOC-005 | F3 | T-UI-003,T-AUT-005 | CRITICAL | DEFINED_NOT_IMPLEMENTED |
| REQ-UI-004 | Progresso não deriva de heartbeat, log ou consumo | POD-DOC-006 | F3,F5 | T-UI-004 | HIGH | DEFINED_NOT_IMPLEMENTED |
| REQ-UI-005 | Interface mostra bloqueio, ramo e condição de retomada | POD-DOC-004 | F3 | T-UI-005 | HIGH | DEFINED_NOT_IMPLEMENTED |
| REQ-UI-006 | READY representa saúde funcional | POD-DOC-005 | F3 | T-UI-006 | HIGH | DEFINED_NOT_IMPLEMENTED |

## 15. Operação e recuperação

| ID | Requisito e critério de aceite | Fonte | Fase | Teste | Criticidade | Estado |
|---|---|---|---|---|---|---|
| REQ-OPS-001 | Startup reconcilia inbox/outbox e retoma missão não terminal | POD-DOC-005 | F1–F3 | T-OPS-001 | CRITICAL | DEFINED_NOT_IMPLEMENTED |
| REQ-OPS-002 | Reboot preserva missão, checkpoint, idempotência e evidência | POD-DOC-009 | F3,F13 | T-OPS-002 | CRITICAL | DEFINED_NOT_IMPLEMENTED |
| REQ-OPS-003 | Restore preserva hashes, versões e fencing | POD-DOC-007 | F13 | T-OPS-003 | CRITICAL | DEFINED_NOT_IMPLEMENTED |
| REQ-OPS-004 | Update preserva missões e possui health gate | POD-DOC-007 | F13 | T-OPS-004 | CRITICAL | DEFINED_NOT_IMPLEMENTED |
| REQ-OPS-005 | Update falho possui rollback comprovado | POD-DOC-007 | F13 | T-OPS-005 | CRITICAL | DEFINED_NOT_IMPLEMENTED |
| REQ-OPS-006 | Configuração inválida ou store indisponível impede READY falso | POD-DOC-005 | F0,F13 | T-OPS-006,T-OPS-007 | CRITICAL | DEFINED_NOT_IMPLEMENTED |
| REQ-OPS-007 | Queda de canal não interrompe execução local já aceita | POD-DOC-003 | F3 | T-OPS-008 | CRITICAL | DEFINED_NOT_IMPLEMENTED |

## 16. Produto e entrega

| ID | Requisito e critério de aceite | Fonte | Fase | Teste | Criticidade | Estado |
|---|---|---|---|---|---|---|
| REQ-DEL-001 | Product Contract deriva requisitos e gates aplicáveis da missão | POD-DOC-004 | F12 | T-PROD-001 | HIGH | DEFINED_NOT_IMPLEMENTED |
| REQ-DEL-002 | Produto possui prova funcional reproduzível | POD-DOC-010 | F12 | T-PROD-002 | CRITICAL | DEFINED_NOT_IMPLEMENTED |
| REQ-DEL-003 | Falha de segurança crítica bloqueia promoção | POD-DOC-007 | F12 | T-PROD-003 | CRITICAL | DEFINED_NOT_IMPLEMENTED |
| REQ-DEL-004 | Artifact Manifest registra conteúdo, hashes e proveniência | POD-DOC-006 | F3,F12 | T-PROD-004 | CRITICAL | DEFINED_NOT_IMPLEMENTED |
| REQ-DEL-005 | Instalação e health do produto são testados | POD-DOC-009 | F12 | T-PROD-005 | HIGH | DEFINED_NOT_IMPLEMENTED |
| REQ-DEL-006 | Produto possui rollback quando aplicável | POD-DOC-009 | F12 | T-PROD-006 | CRITICAL | DEFINED_NOT_IMPLEMENTED |
| REQ-DEL-007 | Evidence Pack final liga todos os gates | POD-DOC-006 | F12,F15 | T-PROD-008 | CRITICAL | DEFINED_NOT_IMPLEMENTED |
| REQ-DEL-008 | E2E soberano constrói, falha, recupera, entrega e prova | POD-DOC-009 | F15 | T-PROD-002,T-PROD-008,T-OPS-002 | CRITICAL | DEFINED_NOT_IMPLEMENTED |

## 17. Resumo inicial

| Estado | Quantidade esperada antes da validação |
|---|---:|
| ACCEPTED | 6 |
| DEFINED_NOT_IMPLEMENTED | 104 |

As quantidades são verificadas automaticamente. Após T-DOC aprovado e evidenciado, somente REQ-DOC pode avançar para ACCEPTED. Os demais permanecem não implementados até prova do runtime.
