#!/usr/bin/env python3
from pathlib import Path
import hashlib
import json
import sys

ROOT = Path(__file__).resolve().parents[1]
errors = []

required = [
    ROOT / "POD_DOCUMENTACAO_CONSOLIDADA_CANONICA.md",
    ROOT / "POD_BASELINE_CANONICA_AQUISICAO_EVOLUCAO_HIGIENE.md",
    ROOT / "MISSION_STATE.json",
    ROOT / "ADR",
    ROOT / "SCHEMAS",
    ROOT / "CONTRACTS",
    ROOT / "STANDARDS",
    ROOT / "RUNBOOKS",
    ROOT / "EVIDENCE",
    ROOT / "RELEASES",
    ROOT / "HISTORY",
]
for path in required:
    if not path.exists():
        errors.append(f"missing: {path.relative_to(ROOT)}")

canonical = ROOT / "POD_DOCUMENTACAO_CONSOLIDADA_CANONICA.md"
if canonical.exists():
    text = canonical.read_text(encoding="utf-8")
    markers = [
        "# POD — DOCUMENTAÇÃO CONSOLIDADA CANÔNICA",
        "**Versão:** 4.0.0-DRAFT-CANONICAL",
        "POD_DOCUMENTACAO_CONSOLIDADA_CANONICA.md",
        "REUSE FIRST",
        "ADE",
        "BASELINE_RECONCILED",
        "CORE_CONTRACTS_DEFINED",
    ]
    for marker in markers:
        if marker not in text:
            errors.append(f"canonical marker missing: {marker}")

baseline = ROOT / "POD_BASELINE_CANONICA_AQUISICAO_EVOLUCAO_HIGIENE.md"
if baseline.exists():
    text = baseline.read_text(encoding="utf-8")
    markers = [
        "# POD — BASELINE CANÔNICA DE AQUISIÇÃO, EVOLUÇÃO E HIGIENE",
        "**Versão:** 1.0.0",
        "BASELINE_DOCUMENT_CREATED=VERIFIED",
        "ACQUISITION=NOT_EXECUTED",
        "MISSION_PROVEN=NO",
    ]
    for marker in markers:
        if marker not in text:
            errors.append(f"baseline marker missing: {marker}")

if (ROOT / "POD_PROJETO_CONSOLIDADO.md").exists():
    errors.append("superseded POD_PROJETO_CONSOLIDADO.md remains active at repository root")

history = ROOT / "HISTORY" / "README.md"
if history.exists() and "NORMATIVE=false" not in history.read_text(encoding="utf-8"):
    errors.append("HISTORY/README.md does not declare NORMATIVE=false")

v3 = ROOT / "HISTORY" / "POD_PROJETO_CONSOLIDADO_v3.0.md"
expected_v3 = "87de4a78972b4cfc85552521086ce12d29b67f54b69b5a0336e187f57b0de921"
if not v3.exists():
    errors.append("historical v3 missing")
elif hashlib.sha256(v3.read_bytes()).hexdigest() != expected_v3:
    errors.append("historical v3 hash mismatch")

for adr in [
    "ADR-001-GITHUB-NATIVO-SCM-SOBERANO.md",
    "ADR-002-BRACOS-LOGICOS-ESPECIALISTAS-32.md",
    "ADR-003-REUSE-FIRST-E-PIPELINE-DE-AQUISICAO.md",
    "ADR-004-ADE-E-RUNTIME-ESPECIALIZADO-ISOLADO.md",
]:
    if not (ROOT / "ADR" / adr).exists():
        errors.append(f"missing ADR: {adr}")

adr2 = ROOT / "ADR" / "ADR-002-BRACOS-LOGICOS-ESPECIALISTAS-32.md"
if adr2.exists() and "MAX_LOGICAL_ARMS = 32" not in adr2.read_text(encoding="utf-8"):
    errors.append("ADR-002 does not define 32 logical arms")

try:
    state = json.loads((ROOT / "MISSION_STATE.json").read_text(encoding="utf-8"))
    if state.get("repository") != "https://github.com/andrebarros78/pod":
        errors.append("MISSION_STATE repository mismatch")
    if state.get("branch") != "build/pod-foundation-v001":
        errors.append("MISSION_STATE branch mismatch")
    if state.get("phase") != 1:
        errors.append("MISSION_STATE must remain at phase 1 during this reconciliation")
    if state.get("phase_target") != "CORE_CONTRACTS_DEFINED":
        errors.append("MISSION_STATE phase target regression")
    if state.get("status") != "PROVEN":
        errors.append("MISSION_STATE phase 1 is not PROVEN")
except Exception as exc:
    errors.append(f"MISSION_STATE invalid: {exc}")

manifest = ROOT / "RELEASES" / "POD_BASELINE_V4_2026-10-03.json"
if not manifest.exists():
    errors.append("baseline release manifest missing")
else:
    try:
        m = json.loads(manifest.read_text(encoding="utf-8"))
        for item in m.get("canonical_files", []):
            p = ROOT / item["path"]
            actual = hashlib.sha256(p.read_bytes()).hexdigest()
            if actual != item["sha256"]:
                errors.append(f"manifest hash mismatch: {item['path']}")
    except Exception as exc:
        errors.append(f"baseline release manifest invalid: {exc}")

if errors:
    print("POD_GOVERNANCE_INVALID")
    for err in errors:
        print(f"- {err}")
    sys.exit(1)
print("POD_GOVERNANCE_VALID")
