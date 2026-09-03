# POD — Plataforma Orquestradora Durável

O POD é um construtor soberano de software. Recebe uma missão, preserva o compromisso assumido, planeja, executa, testa, recupera falhas e somente conclui quando o resultado estiver comprovado.

## Estado atual

- Projeto conceitual e arquitetura lógica: normativos.
- Contratos de autoridade, dados, estados, segurança e prova: normativos.
- Independência do ChatGPT, IA híbrida e Terminal Soberano: decisão normativa.
- Matriz de requisitos e plano de construção: normativos.
- Implementação executável: ainda não iniciada.
- Stack física: ainda não escolhida.

Documento normativo não é prova de implementação. O estado inicial dos requisitos permanece **DEFINED_NOT_IMPLEMENTED**.

## Entrada oficial

Leia primeiro o [Índice Mestre V003](docs/POD_INDICE_MESTRE_V003.md). Ele define:

- o conjunto documental ativo;
- a precedência entre documentos;
- os artefatos substituídos;
- a ordem obrigatória de leitura;
- a forma de verificar integridade.

O manifesto verificável está em [POD_DOCUMENT_MANIFEST_V003.json](docs/POD_DOCUMENT_MANIFEST_V003.json).
A execução da validação está registrada em [POD_DOCSET_V003_VALIDATION.md](docs/evidence/POD_DOCSET_V003_VALIDATION.md).

## Regra de conclusão

~~~text
MISSION_GIVEN
→ MISSION_ACCEPTED
→ WORK
→ PROOF_VERDICT
→ MISSION_PROVEN
~~~

O Proof Engine avalia evidências. O Mission Core é o único componente que altera o estado soberano da missão. Cérebro, Worker, modelo de IA, painel ou texto não podem declarar conclusão.

O executável próprio `pod` será a interface operacional nativa. ChatGPT, MCP e
provedores de IA serão integrações substituíveis; o núcleo não dependerá deles para
preservar estado, aplicar regras ou recuperar missões.

A decisão completa está em [ADR-009 — Independência do ChatGPT, IA híbrida e
Terminal Soberano](docs/adr/ADR-009-INDEPENDENCIA-DO-CHATGPT-IA-HIBRIDA-E-TERMINAL-SOBERANO.md).

## Validar a documentação

No diretório raiz:

~~~bash
python scripts/validate_docs.py
~~~

Resultado esperado:

~~~text
POD_DOCSET_VALID
~~~

## Regra de implementação

A stack física e o skeleton só podem ser definidos quando todos os gates documentais de F0 estiverem aprovados. Toda implementação deverá ligar requisito, decisão, contrato, teste, evidência e aceite.
