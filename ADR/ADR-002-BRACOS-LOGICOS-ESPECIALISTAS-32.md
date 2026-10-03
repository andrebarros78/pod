# ADR-002 — 32 braços lógicos bilaterais especialistas

**Status:** ACCEPTED  
**Data:** 2026-10-03  
**Autoridade:** decisão explícita do Owner

## Decisão central

A capacidade lógica de execução do POD é organizada em **32 braços lógicos bilaterais**, distribuídos em **8 blocos de 4 canais**. São **31 braços especialistas + 1 coordenador**.

`MAX_LOGICAL_ARMS = 32`

Capacidade lógica não significa obrigação de manter 32 cargas pesadas fisicamente ativas. O Governador reduz ou amplia a concorrência física conforme dependências, isolamento, CPU, RAM, I/O, rede, cotas, custo e risco, sem destruir a identidade lógica dos braços.

## Bloco 1 — sistemas críticos e robustos

- 01 — Alta confiabilidade: Ada / SPARK
- 02 — Segurança de memória: Rust
- 03 — Concorrência e infraestrutura: Go
- 04 — Disponibilidade 24h: Elixir / Erlang

## Bloco 2 — plataformas corporativas e mobile

- 05 — Sistemas corporativos e JVM: Java
- 06 — Ecossistema Microsoft: C#
- 07 — Ecossistema Apple: Swift
- 08 — Android e JVM moderna: Kotlin

## Bloco 3 — aplicações e web

- 09 — IA, automação, dados e backend: Python
- 10 — Web e runtime JS: JavaScript
- 11 — Web com tipagem segura: TypeScript
- 12 — Aplicações dinâmicas: Ruby

## Bloco 4 — baixo nível e desempenho

- 13 — Embarcados e sistemas: C
- 14 — Alto desempenho: C++
- 15 — Baixo nível moderno: Zig
- 16 — Arquitetura de processador: Assembly

## Bloco 5 — engenharia formal

- 17 — Programação funcional e tipos: Haskell / OCaml
- 18 — Prova formal: Rocq/Coq / Lean / Agda / Idris
- 19 — Contratos e concorrência segura: Eiffel / Pony
- 20 — Sistemas verificados e criptografia: ATS / F*

## Bloco 6 — automação e infraestrutura

- 21 — Automação Windows: PowerShell
- 22 — Automação Linux/Unix: Bash / Shell
- 23 — Infraestrutura como código: Terraform / Ansible / Docker
- 24 — Versionamento e pipelines: Git / CI/CD

## Bloco 7 — marcação, dados e contratos

- 25 — Estrutura e estilo de páginas: HTML / CSS
- 26 — Dados e configuração: XML / JSON / YAML
- 27 — Documentação: Markdown / LaTeX
- 28 — Contratos de API: GraphQL / Protobuf / OpenAPI

## Bloco 8 — dados, hardware e controle

- 29 — Bancos de dados: SQL
- 30 — Ciência de dados: R / Julia
- 31 — Hardware: Verilog / VHDL
- 32 — Coordenador: integra, valida e resolve conflitos entre os braços

## Regras de roteamento

1. Especialidade é autoridade técnica primária, não exclusividade rígida.
2. Uma tarefa multidomínio pode ativar vários braços simultaneamente.
3. O braço 32 coordena integração e conflito; não substitui o Governador e não possui soberania própria.
4. Tarefas independentes podem executar em paralelo; conflitos são bloqueados no menor recurso compartilhado possível.
5. O MVP pode iniciar com concorrência física menor, mas contratos e identificadores não devem impedir evolução até os 32 braços.
6. Cada braço deve ser observável por missão, tarefa, estado, dependências, recurso, resultado e evidência.
