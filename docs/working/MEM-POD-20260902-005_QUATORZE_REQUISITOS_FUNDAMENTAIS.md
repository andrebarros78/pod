# POD — REGISTRO VIVO

## MEM-POD-20260902-005 — QUATORZE REQUISITOS FUNDAMENTAIS

**DATA:** 02/09/2026  
**TIPO:** PRINCIPLE / CAPABILITY / RULE_CANDIDATE / ARCHITECTURAL_INSIGHT  
**STATUS:** CAPTURED  
**NORMATIVO:** NÃO  
**ESCOPO:** Registro Vivo de Ideias e Memória do POD

## TEXTO ORIGINAL

> esqueci de algo Pipo?

Decisão posterior do proprietário:

> registre em Registro Vivo

## INTERPRETAÇÃO TÉCNICA

Os dez requisitos fundamentais já registrados para o comportamento final do POD permanecem válidos como candidatos obrigatórios de materialização no código-fonte. A análise identificou quatro garantias adicionais que completam o conjunto conceitual atual em quatorze requisitos fundamentais.

A regra superior do conjunto é:

```text
POD NÃO TRANSFERE COMPLEXIDADE TÉCNICA PARA O USUÁRIO.
```

A complexidade deve ser absorvida internamente pelo POD por decisão, execução, recuperação, segurança, governança de recursos, conhecimento, testes e evidência, produzindo para o usuário um resultado simples, verdadeiro e comprovado.

## OS 14 REQUISITOS FUNDAMENTAIS

### 1. Missão aceita gera obrigação de conclusão comprovada

```text
MISSION_GIVEN
→ MISSION_ACCEPTED
→ WORK
→ PROOF
→ MISSION_PROVEN
```

Falha técnica recuperável não encerra a missão. A missão aceita deve continuar até conclusão comprovada, cancelamento soberano legítimo ou dependência externa realmente incontornável.

### 2. O usuário não pode virar operador técnico do POD

O POD deve descobrir, executar, diagnosticar, corrigir, testar, reiniciar, recuperar e continuar autonomamente dentro do escopo e das políticas aplicáveis. Não deve transferir ao usuário tarefas técnicas rotineiras que o próprio POD possui capacidade e autoridade para resolver.

### 3. POD deve pensar como engenheiro, não apenas obedecer como executor

O Cérebro e a Engenharia de Construção devem compreender intenção, avaliar alternativas, identificar riscos, decidir tecnicamente, decompor trabalho, escolher estratégia, diagnosticar falhas e replanejar quando necessário.

### 4. Nada essencial pode ser perdido

Missão, estado, decisões, resultados, checkpoints, evidências, histórico e demais informações essenciais devem sobreviver a queda de sessão, navegador, túnel, conexão, Worker, processo, serviço, reinício do sistema e outras interrupções recuperáveis.

### 5. POD deve possuir autodiagnóstico, contenção e autorrecuperação

O POD deve detectar degradação, loop improdutivo, processo vivo sem progresso, Worker obsoleto, corrupção de estado, conflito de autoridade, falha recorrente e demais anomalias relevantes; então conter, diagnosticar, recuperar, validar e retomar.

### 6. Conhecimento técnico deve ser utilizável operacionalmente

Memória e conhecimento técnico devem estar disponíveis para decisão e construção. Quando existir lacuna de conhecimento, o POD deve poder identificar, consultar, aprender/adquirir quando permitido, validar, aplicar e testar o conhecimento necessário.

### 7. Interface simples para o usuário, complexidade absorvida internamente

A operação externa deve ser orientada a objetivo, preferencialmente em linguagem simples. Serviços, filas, processos, portas, PIDs e detalhes internos não devem ser exigidos do usuário para a operação cotidiana.

### 8. Verdade operacional obrigatória

O POD deve distinguir atividade de progresso, processo vivo de serviço funcional, execução de conclusão e declaração de prova. Painel, Terminal, APIs e evidências devem refletir estado real.

```text
RUNNING != HEALTHY
ACTIVITY != PROGRESS
IMPLEMENTED != PROVEN
```

### 9. Soberania operacional com segurança

O POD deve possuir autoridade técnica e capacidades de execução necessárias à missão, incluindo acesso autorizado a terminal, arquivos, processos, serviços, ferramentas e operações administrativas mediadas, preservando identidade, escopo, isolamento, auditoria, fencing, rollback, segurança e limites soberanos.

### 10. Absorção integral do valor técnico comprovado anterior

Capacidades tecnicamente boas e comprovadas provenientes de LMCP, WMCP e outras experiências devem ser inventariadas, comparadas, aperfeiçoadas e absorvidas como capacidades nativas do POD, sem dependência, nomenclatura, caminhos, serviços ou identidade de projeto doador no produto final.

### 11. Autossustentação operacional

O POD deve saber cuidar da própria operação. Deve possuir capacidades para instalar, inicializar, verificar, atualizar de forma controlada, migrar, fazer backup, validar backup, restaurar, reparar e validar a própria saúde sem depender de intervenção técnica humana rotineira.

Autossustentação não significa ignorar políticas de segurança, licenças, autorizações financeiras ou controles obrigatórios.

### 12. Governança adaptativa de recursos e convivência com a máquina

O POD deve administrar CPU, RAM, disco, I/O, filas, concorrência, processos e demais recursos de forma adaptativa. Quando a capacidade estiver reduzida, deve preferir admission control, throttling, redução de paralelismo, reordenação e continuidade segura em vez de saturar ou travar a máquina.

Princípio:

```text
FALTA DE RECURSO RECUPERÁVEL
→ REPLANEJAR CAPACIDADE
→ NÃO ABANDONAR MISSÃO
```

### 13. Rastreabilidade total e reprodutibilidade

Para qualquer resultado relevante, o POD deve conseguir reconstruir tecnicamente:

```text
O QUE DECIDIU
POR QUE DECIDIU
O QUE EXECUTOU
O QUE MUDOU
QUAL TESTE EXECUTOU
QUAL RESULTADO OBSERVOU
QUAL EVIDÊNCIA FOI PRESERVADA
QUAL CHECKPOINT PERMITE RECUPERAÇÃO
```

Rastreabilidade não é apenas log. Deve permitir auditoria, reprodução e recuperação da cadeia de decisão e execução conforme aplicável.

### 14. Degradação inteligente e continuidade parcial

Falha localizada não deve derrubar o sistema inteiro quando houver trabalho independente seguro a executar.

```text
FALHA LOCAL != PARADA GLOBAL
```

Exemplos conceituais:

- perda de internet não interrompe trabalho puramente local;
- perda de um canal externo não interrompe missão já persistida;
- falha de um Worker não derruba Workers independentes;
- indisponibilidade de um provider não bloqueia trabalho que não dependa dele;
- aprovação financeira pendente bloqueia somente o ramo dependente;
- falha de um nó não deve eliminar estado soberano ou trabalhos independentes quando a arquitetura final permitir continuidade.

## GARANTIA TRANSVERSAL DE PROGRESSO REAL

O conjunto dos 14 requisitos incorpora explicitamente a regra:

```text
ATIVIDADE != PROGRESSO
```

Se não houver avanço real mensurável, o POD deve detectar estagnação e reagir:

```text
SEM PROGRESSO REAL
→ DETECTAR
→ DIAGNOSTICAR
→ MUDAR ESTRATÉGIA
→ RECUPERAR
→ TESTAR
→ CONTINUAR
```

O POD não deve permanecer indefinidamente consumindo recursos e aparentando trabalho sem convergência objetiva da missão.

## MATERIALIZAÇÃO NO CÓDIGO-FONTE

Na consolidação final, os 14 requisitos deverão ser rastreáveis até comportamento implementado. A forma física dos módulos ainda não está definida, mas cada requisito deverá possuir, conforme aplicável:

```text
REQUISITO
→ CONTRATO / INVARIANTE
→ RESPONSABILIDADE
→ IMPLEMENTAÇÃO
→ TESTE
→ EVIDÊNCIA
→ GATE
```

A existência de documentação sem comportamento executável não será suficiente para considerar qualquer requisito atendido.

## GATE CANDIDATO

Relaciona-se ao gate já proposto:

```text
POD_SOURCE_DNA_PROVEN = PASS
```

Esse gate somente poderá passar quando os requisitos considerados obrigatórios na arquitetura final estiverem implementados, testados e evidenciados de forma objetiva.

## MOTIVAÇÃO

Completar a definição das propriedades que tornam o POD um construtor soberano confiável, reduzindo o risco de construir um sistema tecnicamente sofisticado que ainda dependa do usuário para operar, manter, diagnosticar, provar, recuperar ou administrar recursos.

## IMPACTO POSSÍVEL

- requisitos do domínio e da máquina de missão;
- Cérebro e Engenharia de Construção;
- Memória e persistência;
- Governador e Resource Governance;
- Sistema Imunológico e recovery;
- Túnel Core e continuidade desconectada;
- Executor Privilegiado;
- Painel e Terminal;
- observabilidade e progress health;
- evidências, checkpoints e auditoria;
- instalação, atualização, backup e disaster recovery;
- testes de resiliência, performance, segurança e aceitação;
- absorção de capacidades comprovadas de projetos doadores.

## DEPENDÊNCIAS

- consolidação futura dos grandes componentes do POD;
- definição de contratos e autoridade entre os componentes;
- matriz final de requisitos e rastreabilidade;
- critérios objetivos de MISSION_PROVEN;
- definição de políticas de segurança, recursos e continuidade.

## CONFLITOS POSSÍVEIS

A responsabilidade física por cada requisito ainda poderá mudar durante a consolidação arquitetural. Em particular, autodiagnóstico, recuperação e health podem envolver Governador e Sistema Imunológico; continuidade pode envolver Túnel Core, Memória e runtime; autossustentação pode envolver bootstrap, update, recovery e Executor Privilegiado.

Essas sobreposições não serão resolvidas nesta memória.

## RELAÇÕES COM OUTRAS MEMÓRIAS

- **MEM-POD-20260902-001:** absorção integral do valor técnico comprovado de LMCP e WMCP.
- **MEM-POD-20260902-002:** componentes conceituais Memória, Governador, Cérebro, Túnel Core e Sistema Imunológico.
- **MEM-POD-20260902-003:** Fundação Neutra / DNA técnico de baixo arrependimento.
- **MEM-POD-20260902-004:** dez requisitos obrigatórios de materialização no código-fonte do POD.

Esta memória complementa MEM-POD-20260902-004 adicionando os requisitos 11 a 14 e consolidando a visão conceitual dos 14 requisitos fundamentais.

## DECISÃO FINAL

PENDENTE DE CONSOLIDAÇÃO DA ARQUITETURA FINAL.

## INCORPORADO EM

Registro Vivo de Ideias e Memória do POD. Ainda não incorporado em arquitetura normativa, baseline ou ADR.
