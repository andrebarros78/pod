# Modelagem formal

`PODCore.tla` modela a transição mínima de missão e a autoridade de escrita por lease/generation/fencing antes do MVP.

O modelo verifica, no mínimo:

- `MISSION_PROVEN` implica validação anterior;
- generation e fencing token evoluem juntos;
- tentativas de escrita com token obsoleto são negadas;
- existe no máximo um lease holder lógico por vez neste modelo mínimo.

## Ferramenta reproduzível

- TLA+ tools: `v1.7.4`
- `tla2tools.jar` SHA-256: `936a262061c914694dfd669a543be24573c45d5aa0ff20a8b96b23d01e050e88`
- Validação: `python3 scripts/validate_formal.py`

O JAR é baixado para `/tmp`, verificado por hash e não é versionado no repositório.
