#!/usr/bin/env python3
from pathlib import Path
import json
import sys

ROOT = Path(__file__).resolve().parents[1]
errors = []

required = [
    ROOT / "POD_PROJETO_CONSOLIDADO.md",
    ROOT / "MISSION_STATE.json",
    ROOT / "ADR",
    ROOT / "SCHEMAS",
    ROOT / "RUNBOOKS",
    ROOT / "EVIDENCE",
    ROOT / "RELEASES",
    ROOT / "HISTORY",
]
for path in required:
    if not path.exists():
        errors.append(f"missing: {path.relative_to(ROOT)}")

canonical = ROOT / "POD_PROJETO_CONSOLIDADO.md"
if canonical.exists():
    text = canonical.read_text(encoding="utf-8")
    required_markers = [
        "# POD — Projeto Consolidado (v3.0)",
        "POD_PROJETO_CONSOLIDADO.md  ← fonte normativa única",
        "CORE_STORES_CONTENT=false",
        "CORE_UNSAFE_CODE=0",
        "MODULE_PROVEN → INTEGRATION_PROVEN → MISSION_PROVEN → PRODUCT_PROVEN → SEALED",
    ]
    for marker in required_markers:
        if marker not in text:
            errors.append(f"canonical marker missing: {marker}")

history = ROOT / "HISTORY" / "README.md"
if history.exists() and "NORMATIVE=false" not in history.read_text(encoding="utf-8"):
    errors.append("HISTORY/README.md does not declare NORMATIVE=false")

try:
    state = json.loads((ROOT / "MISSION_STATE.json").read_text(encoding="utf-8"))
    if state.get("repository") != "https://github.com/andrebarros78/pod":
        errors.append("MISSION_STATE repository mismatch")
    if state.get("branch") != "build/pod-foundation-v001":
        errors.append("MISSION_STATE branch mismatch")
except Exception as exc:
    errors.append(f"MISSION_STATE invalid: {exc}")

adr1 = ROOT / "ADR" / "ADR-001-GITHUB-NATIVO-SCM-SOBERANO.md"
adr2 = ROOT / "ADR" / "ADR-002-BRACOS-LOGICOS-ESPECIALISTAS-32.md"
if not adr1.exists():
    errors.append("ADR-001 missing")
if not adr2.exists():
    errors.append("ADR-002 missing")
elif "MAX_LOGICAL_ARMS = 32" not in adr2.read_text(encoding="utf-8"):
    errors.append("ADR-002 does not define 32 logical arms")

if errors:
    print("POD_GOVERNANCE_INVALID")
    for err in errors:
        print(f"- {err}")
    sys.exit(1)
print("POD_GOVERNANCE_VALID")
