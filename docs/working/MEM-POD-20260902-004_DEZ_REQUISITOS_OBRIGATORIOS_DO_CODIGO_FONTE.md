# MEM-POD-20260902-004 — DEZ REQUISITOS OBRIGATÓRIOS DO CÓDIGO-FONTE DO POD

**DATA:** 02/09/2026  
**TIPO:** PRINCIPLE / RULE_CANDIDATE / SOURCE_CODE_REQUIREMENT  
**STATUS:** CANDIDATE  
**NORMATIVO:** NÃO — REGISTRO VIVO DURANTE A FASE DE CONCEPÇÃO  
**INTENÇÃO DO PROPRIETÁRIO:** OBRIGATÓRIO NA CONSOLIDAÇÃO FINAL E NA IMPLEMENTAÇÃO DO CÓDIGO-FONTE

## TEXTO ORIGINAL

> Registra, estes 10 pontos tem que fazer parte do codigo fonte de POD.

## REGRA CENTRAL

Os dez pontos abaixo não são apenas características desejáveis de interface ou documentação. A arquitetura final deverá assegurar que cada um seja materializado por código executável, contratos, estados, políticas, testes e evidências suficientes para comprovar seu comportamento.

A implementação concreta poderá distribuir essas responsabilidades entre componentes diferentes. Não é obrigatório criar um módulo com o mesmo nome de cada ponto. É obrigatório que o comportamento correspondente exista, seja testável e seja comprovável.

## 1. MISSÃO DADA → OBRIGAÇÃO DE CONCLUSÃO COMPROVADA

O código-fonte do POD deverá tratar uma missão aceita como compromisso persistente de continuar trabalhando até prova terminal válida.

```text
MISSION_GIVEN
→ MISSION_ACCEPTED
→ EXECUTION
→ VALIDATION
→ MISSION_PROVEN
```

Falha técnica recuperável não encerra a missão. Falha de tentativa, ferramenta, Worker, teste, serviço ou estratégia deve alimentar diagnóstico, recuperação, replano ou nova tentativa.

O estado terminal de sucesso somente poderá ser produzido mediante critérios objetivos, testes e evidências.

## 2. O USUÁRIO NÃO PODE SER TRANSFORMADO EM OPERADOR TÉCNICO DO POD

O código deverá permitir que o POD execute autonomamente ações técnicas rotineiras necessárias à missão dentro das autorizações vigentes, incluindo descoberta de arquivos e ferramentas, uso de terminal, leitura e escrita, execução de comandos, instalação de recursos gratuitos autorizados, diagnóstico, correção, teste, reinício e recuperação.

O runtime não deverá depender de comandos humanos repetitivos como `continue`, `retome`, `tente novamente`, `abra o terminal` ou `onde parou` para prosseguir em trabalho tecnicamente resolvível.

## 3. O POD DEVE RACIOCINAR E DECIDIR COMO ENGENHEIRO

O código deverá possuir contratos e mecanismos para:

- compreender objetivo e contexto;
- decompor trabalho;
- comparar soluções;
- selecionar estratégia;
- diagnosticar causas;
- replanejar;
- avaliar risco técnico;
- escolher ferramentas e caminhos adequados;
- verificar se o resultado atende ao objetivo.

O usuário define prioritariamente o resultado e os limites soberanos. O POD deve resolver tecnicamente como alcançar o resultado.

## 4. NADA ESSENCIAL PODE SER PERDIDO

Missão, comandos aceitos, estado, decisões, checkpoints, resultados confirmados, evidências e progresso relevante devem sobreviver a falhas de processo, Worker, interface, conexão externa e reinicialização da máquina quando tecnicamente possível.

```text
CONVERSA != MISSÃO
CONEXÃO != EXECUÇÃO
PROCESSO != ESTADO
WORKER != MISSÃO
```

A continuidade deve pertencer à identidade durável da missão e ao estado persistente.

## 5. O POD DEVE SE AUTODIAGNOSTICAR, AUTOCONTER E AUTORRECUPERAR

O código deverá detectar e tratar, entre outros:

- serviço vivo sem progresso;
- loop improdutivo;
- Worker obsoleto;
- lease vencido;
- mutação de geração antiga;
- corrupção ou inconsistência de estado;
- restart storm;
- concorrência destrutiva;
- degradação de recursos;
- falhas repetitivas;
- divergência entre resultado declarado e evidência real.

A recuperação deve seguir lógica equivalente a:

```text
DETECTAR
→ CONTER
→ PRESERVAR ESTADO
→ DIAGNOSTICAR
→ RECUPERAR
→ TESTAR
→ VALIDAR
→ RETOMAR
→ EVIDENCIAR
```

## 6. O POD DEVE POSSUIR E USAR CONHECIMENTO TÉCNICO

Conhecimento técnico não poderá ser apenas documentação passiva. O código deverá permitir recuperar, selecionar e aplicar conhecimento relevante à missão.

Quando houver lacuna de conhecimento, o sistema deverá poder identificar a lacuna, buscar conhecimento autorizado, validar, estruturar, incorporar ao contexto apropriado e comprovar sua utilidade antes de depender dele como competência operacional.

Memória operacional, documentação de projeto, conhecimento técnico e políticas deverão permanecer conceitos separados.

## 7. A INTERFACE DEVE SER SIMPLES PARA O USUÁRIO E A COMPLEXIDADE DEVE FICAR INTERNA

Terminal, painel e demais interfaces deverão operar por intenção e objetivo, sem exigir que o usuário conheça PIDs, filas internas, leases, portas, topologia de Workers ou detalhes de infraestrutura para realizar operações comuns.

A complexidade interna pode ser alta; a superfície operacional deve ser simples, objetiva, em português e orientada ao resultado.

## 8. O POD DEVE MOSTRAR A VERDADE OPERACIONAL

O código deverá distinguir explicitamente:

```text
LIVENESS
READINESS
PROGRESS
RESULT
PROOF
```

Não será permitido equivaler `RUNNING` a saudável, Worker vivo a missão avançando, retry a recuperação ou texto de sucesso a prova.

Painel, Terminal e APIs deverão refletir o estado soberano e as evidências reais, incluindo o motivo pelo qual uma missão ainda não atingiu `MISSION_PROVEN`.

## 9. SOBERANIA OPERACIONAL COM SEGURANÇA E CONTENÇÃO

O POD deverá possuir capacidade técnica para terminal, leitura, escrita, processos, serviços, ferramentas e operações administrativas autorizadas, mas essa capacidade deverá ser mediada por identidade, escopo, isolamento, auditoria, rollback, leases/fencing quando aplicável e execução privilegiada controlada.

Segurança deve proteger a missão sem transformar operações técnicas previamente autorizadas em solicitações humanas repetitivas.

Gasto financeiro novo não autorizado permanece como barreira soberana. Dependências externas fisicamente indisponíveis devem suspender somente o ramo dependente quando possível, preservando a missão para retomada.

## 10. PRESERVAR E ABSORVER TODO VALOR TÉCNICO COMPROVADO DAS EXPERIÊNCIAS ANTERIORES

O código-fonte final deverá incorporar, como capacidades nativas do POD, os mecanismos tecnicamente bons e comprovados identificados em sistemas, estudos e experiências anteriores, incluindo quando aplicável:

- persistência durável;
- recovery;
- idempotência;
- leases e fencing;
- health funcional;
- governança de recursos;
- critical path;
- execução paralela controlada;
- Workers aquecidos;
- contexto incremental;
- teste orientado por impacto;
- circuit breakers;
- backpressure;
- checkpoints;
- evidência;
- fault injection;
- mecanismos de defesa e autorrecuperação.

A absorção deverá ocorrer sem dependência de build, runtime, configuração, caminhos, serviços, nomenclaturas ou identidade de sistemas anteriores. O produto final deve possuir somente identidade POD.

## CRITÉRIO DE MATERIALIZAÇÃO NO CÓDIGO

Para cada um dos dez requisitos, a consolidação final deverá apontar no mínimo:

```text
REQUIREMENT_ID
→ CONTRATO / INVARIANTE
→ MÓDULO(S) RESPONSÁVEL(IS)
→ ESTADO / EVENTO RELEVANTE
→ IMPLEMENTAÇÃO
→ TESTE
→ EVIDÊNCIA
→ GATE DE ACEITE
```

Um ponto não será considerado incorporado apenas por estar descrito em documentação.

```text
DOCUMENTADO != IMPLEMENTADO
IMPLEMENTADO != TESTADO
TESTADO != PROVADO
```

## GATE FUTURO CANDIDATO

```text
POD_SOURCE_DNA_PROVEN = PASS
```

O gate somente poderá ser aprovado quando os dez requisitos possuírem implementação efetiva e prova correspondente.

## RELAÇÕES COM OUTRAS MEMÓRIAS

- relaciona-se com a Fundação Neutra do POD e seus invariantes de baixo arrependimento;
- relaciona-se com os componentes conceituais Memória, Governador, Cérebro, Túnel Core e Sistema Imunológico;
- relaciona-se com a absorção integral de capacidades tecnicamente comprovadas, mantendo identidade nativa POD;
- relaciona-se diretamente com `MISSION_PROVEN` como condição terminal comprovada.

## CONFLITOS POSSÍVEIS

A arquitetura final ainda poderá mudar a localização e a distribuição dessas responsabilidades. Essa mudança não poderá eliminar os dez comportamentos obrigatórios registrados aqui.

## DECISÃO FINAL

Decisão do proprietário registrada: **os dez pontos deverão fazer parte do comportamento implementado do código-fonte final do POD**.

A posição arquitetural concreta de cada requisito será definida durante a consolidação final.

## INCORPORADO EM

Ainda não incorporado em arquitetura normativa nem declarado implementado. A implementação deverá ser comprovada posteriormente por código, testes e evidências.