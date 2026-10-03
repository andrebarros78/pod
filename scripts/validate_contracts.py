#!/usr/bin/env python3
from pathlib import Path
import json
import subprocess
import sys

import jsonschema

ROOT = Path(__file__).resolve().parents[1]
SCHEMAS = ROOT / "SCHEMAS" / "v1"
errors = []

for name in ["mission_state.schema.json", "module_contract.schema.json"]:
    path = SCHEMAS / name
    try:
        schema = json.loads(path.read_text(encoding="utf-8"))
        jsonschema.Draft202012Validator.check_schema(schema)
    except Exception as exc:
        errors.append(f"{name}: invalid JSON Schema: {exc}")

try:
    mission_schema = json.loads((SCHEMAS / "mission_state.schema.json").read_text(encoding="utf-8"))
    mission_state = json.loads((ROOT / "MISSION_STATE.json").read_text(encoding="utf-8"))
    jsonschema.validate(mission_state, mission_schema)
except Exception as exc:
    errors.append(f"MISSION_STATE validation failed: {exc}")

proto = SCHEMAS / "pod.proto"
out = Path("/tmp/pod-v1-descriptor.pb")
p = subprocess.run([
    "protoc",
    f"--proto_path={SCHEMAS}",
    "--proto_path=/usr/include",
    f"--descriptor_set_out={out}",
    "--include_imports",
    str(proto),
], capture_output=True, text=True)
if p.returncode != 0:
    errors.append("protoc failed: " + (p.stdout + p.stderr).strip())

if errors:
    print("POD_CONTRACTS_INVALID")
    for err in errors:
        print("- " + err)
    sys.exit(1)
print("POD_CONTRACTS_VALID")
