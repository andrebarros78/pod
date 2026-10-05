#!/usr/bin/env python3
from pathlib import Path
import json
import subprocess
import sys

import jsonschema

ROOT = Path(__file__).resolve().parents[1]
SCHEMAS = ROOT / "SCHEMAS" / "v1"
errors: list[str] = []

SCHEMA_NAMES = [
    "mission_state.schema.json",
    "module_contract.schema.json",
    "data_policy_envelope.schema.json",
    "privacy_decision.schema.json",
    "proof_verdict.schema.json",
    "capability_version.schema.json",
]

schemas: dict[str, dict] = {}
for name in SCHEMA_NAMES:
    path = SCHEMAS / name
    try:
        schema = json.loads(path.read_text(encoding="utf-8"))
        jsonschema.Draft202012Validator.check_schema(schema)
        schemas[name] = schema
    except Exception as exc:
        errors.append(f"{name}: invalid JSON Schema: {exc}")

try:
    mission_schema = schemas["mission_state.schema.json"]
    mission_state = json.loads((ROOT / "MISSION_STATE.json").read_text(encoding="utf-8"))
    jsonschema.validate(mission_state, mission_schema)
except Exception as exc:
    errors.append(f"MISSION_STATE validation failed: {exc}")

proto_out = Path("/tmp/pod-v1-descriptor.pb")
p = subprocess.run([
    "protoc",
    f"--proto_path={SCHEMAS}",
    "--proto_path=/usr/include",
    f"--descriptor_set_out={proto_out}",
    "--include_imports",
    str(SCHEMAS / "pod.proto"),
    str(SCHEMAS / "pod_hardening.proto"),
    str(SCHEMAS / "pod_capability.proto"),
], capture_output=True, text=True)
if p.returncode != 0:
    errors.append("protoc failed: " + (p.stdout + p.stderr).strip())


def must_accept(schema_name: str, instance: dict, label: str) -> None:
    try:
        jsonschema.validate(instance, schemas[schema_name])
    except Exception as exc:
        errors.append(f"{label}: expected ACCEPT, got {exc}")


def must_reject(schema_name: str, instance: dict, label: str) -> None:
    try:
        jsonschema.validate(instance, schemas[schema_name])
    except jsonschema.ValidationError:
        return
    except Exception as exc:
        errors.append(f"{label}: validator error: {exc}")
        return
    errors.append(f"{label}: expected REJECT")


valid_data_policy = {
    "data_id": "dat_1", "project_id": "prj_1", "classification": "restricted",
    "personal_data": True, "sensitive_personal_data": True,
    "child_or_adolescent_data": False, "subject_category": "customer",
    "controller_ref": "ctl_1", "operator_refs": [], "purpose_refs": ["pur_1"],
    "authority_refs": ["auth_1"], "source_ref": "src_1", "lineage_ref": "lin_1",
    "retention_policy_ref": "ret_1", "allowed_operations": ["READ"],
    "allowed_destinations": ["internal_store"], "allowed_projects": ["prj_1"],
    "external_processing_allowed": False, "international_transfer_policy_ref": None,
    "logging_policy": "redacted", "encryption_required": True,
    "created_at": "2026-10-05T16:00:00Z", "policy_version": "1",
}
must_accept("data_policy_envelope.schema.json", valid_data_policy, "valid personal/sensitive data policy")

invalid_personal_without_purpose = dict(valid_data_policy)
invalid_personal_without_purpose["purpose_refs"] = []
must_reject("data_policy_envelope.schema.json", invalid_personal_without_purpose, "personal data without purpose")

invalid_sensitive_without_encryption = dict(valid_data_policy)
invalid_sensitive_without_encryption["encryption_required"] = False
must_reject("data_policy_envelope.schema.json", invalid_sensitive_without_encryption, "sensitive data without encryption requirement")

valid_privacy_allow = {
    "decision_id": "pvd_1", "project_id": "prj_1", "operation_id": "op_1",
    "data_ids": ["dat_1"], "operation": "READ", "purpose_id": "pur_1",
    "policy_version": "1", "destination_ref": "internal_store", "processor_ref": None,
    "decision": "allow", "reason_codes": ["POLICY_ALLOW"], "minimization_applied": True,
    "transformation_refs": [], "expires_at": None, "decided_at": "2026-10-05T16:00:00Z",
    "engine_version": "contract-v1",
}
must_accept("privacy_decision.schema.json", valid_privacy_allow, "valid privacy allow")

invalid_privacy_allow_no_purpose = dict(valid_privacy_allow)
invalid_privacy_allow_no_purpose["purpose_id"] = None
must_reject("privacy_decision.schema.json", invalid_privacy_allow_no_purpose, "privacy allow without purpose")

all_true_gates = {
    "evidence_complete": True, "acceptance_pass": True, "regression_pass": True,
    "checkpoint_present": True, "security_gate_pass": True,
    "privacy_gate_applicable": True, "privacy_gate_pass": True,
    "sensitive_data_security_gate_applicable": True,
    "sensitive_data_security_gate_pass": True, "recovery_pass": True,
    "donor_decoupling_pass": True, "project_isolation_pass": True,
}
valid_proof = {
    "verdict_id": "ver_1", "mission_id": "mis_1", "project_id": "prj_1",
    "outcome": "PASS", "mission_resource_version": "7",
    "acceptance_contract_version": "1", "policy_version": "1",
    "evidence_manifest_ref": "sha256:" + "a" * 64, "failed_gate_codes": [],
    "issued_at": "2026-10-05T16:00:00Z", "valid_until": None, "gates": all_true_gates,
}
must_accept("proof_verdict.schema.json", valid_proof, "valid proof verdict")

for field, label in [
    ("regression_pass", "PASS without regression"),
    ("privacy_gate_pass", "PASS bypassing applicable privacy"),
    ("sensitive_data_security_gate_pass", "PASS bypassing applicable sensitive-data gate"),
]:
    invalid = json.loads(json.dumps(valid_proof))
    invalid["gates"][field] = False
    must_reject("proof_verdict.schema.json", invalid, label)

valid_promoted_capability = {
    "capability_id": "CAP-DBG-001", "version": "1.0.0", "status": "PROMOTED",
    "source_ref": "sha256:" + "c" * 64, "provenance_ref": "prov_1",
    "license_state": "VERIFIED", "risk_class": "MEDIUM", "authority_ceiling": [],
    "trigger_rules": ["debugging task"], "required_context": [],
    "eval_pass": True, "security_pass": True, "regression_pass": True,
    "donor_decoupling_pass": True, "benchmark_ref": "bench_1", "rollback_ref": "cap_prev"
}
must_accept("capability_version.schema.json", valid_promoted_capability, "valid promoted capability")
invalid_promoted = dict(valid_promoted_capability)
invalid_promoted["eval_pass"] = False
must_reject("capability_version.schema.json", invalid_promoted, "promoted capability without eval")

hardening_proto = (SCHEMAS / "pod_hardening.proto").read_text(encoding="utf-8")
required_hardening_messages = [
    "DataPolicyEnvelope", "PrivacyDecision", "SensitiveDataSecurityProfile",
    "ProofGateState", "EvidenceManifest", "ProofVerdict", "ProofConsumption",
    "LeaseAuthorityPresentation", "GovernedExecutionRequest", "RepositoryInspection",
    "ChangePlan", "ChangeSet", "TestRun", "FailureDiagnosis", "CorrectionAttempt",
    "RegressionResult", "ADECheckpoint", "ADEProof", "DispatchEnvelope", "DispatchAck",
    "InboxRecord", "RouteDecision", "CapabilitySnapshot", "ReconciliationRecord",
]
for name in required_hardening_messages:
    if f"message {name} " not in hardening_proto:
        errors.append(f"pod_hardening.proto missing message {name}")

capability_proto = (SCHEMAS / "pod_capability.proto").read_text(encoding="utf-8")
for name in ["CapabilityVersion", "CapabilityEvaluation", "CapabilityPromotionDecision", "CapabilityLoadRequest"]:
    if f"message {name} " not in capability_proto:
        errors.append(f"pod_capability.proto missing message {name}")

if errors:
    print("POD_CONTRACTS_INVALID")
    for err in errors:
        print("- " + err)
    sys.exit(1)
print("POD_CONTRACTS_VALID")
