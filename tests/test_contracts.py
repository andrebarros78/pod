import json
import subprocess
import sys
import unittest
from pathlib import Path

import jsonschema

ROOT = Path(__file__).resolve().parents[1]
SCHEMAS = ROOT / "SCHEMAS" / "v1"

class ContractTests(unittest.TestCase):
    def test_contract_validator(self):
        p = subprocess.run([sys.executable, str(ROOT / "scripts" / "validate_contracts.py")], capture_output=True, text=True)
        self.assertEqual(p.returncode, 0, p.stdout + p.stderr)
        self.assertIn("POD_CONTRACTS_VALID", p.stdout)

    def test_original_proto_contains_minimum_contracts(self):
        text = (SCHEMAS / "pod.proto").read_text(encoding="utf-8")
        names = ["Project", "Mission", "Task", "TaskGraph", "Command", "Event", "StateTransition", "ExecutionRequest", "ExecutionLease", "ExecutionEvent", "ExecutionResult", "CapabilityDescriptor", "NodeIdentity", "NodeHeartbeat", "ResourceClaim", "AuthorizationGrant", "AuthorizationDenial", "Checkpoint", "EvidenceRecord", "Incident", "RecoveryAction", "GitIntent", "ArtifactManifest", "KnowledgeRecord", "ProviderDescriptor"]
        for name in names: self.assertIn(f"message {name} ", text)

    def test_hardening_proto_closes_f1_contract_gaps(self):
        text = (SCHEMAS / "pod_hardening.proto").read_text(encoding="utf-8")
        names = ["DataPolicyEnvelope", "PrivacyDecision", "SensitiveDataSecurityProfile", "ProofGateState", "EvidenceManifest", "ProofVerdict", "ProofConsumption", "LeaseAuthorityPresentation", "GovernedExecutionRequest", "RepositoryInspection", "ChangePlan", "ChangeSet", "TestRun", "FailureDiagnosis", "CorrectionAttempt", "RegressionResult", "ADECheckpoint", "ADEProof", "DispatchEnvelope", "DispatchAck", "InboxRecord", "RouteDecision", "CapabilitySnapshot", "ReconciliationRecord"]
        for name in names: self.assertIn(f"message {name} ", text)

    def test_arms_contract_supports_32(self):
        text = (SCHEMAS / "pod.proto").read_text(encoding="utf-8")
        self.assertIn("message ArmDescriptor", text)
        self.assertIn("uint32 logical_arm", text)

    def test_proof_pass_requires_regression(self):
        schema = json.loads((SCHEMAS / "proof_verdict.schema.json").read_text(encoding="utf-8"))
        instance = {"verdict_id":"ver_x","mission_id":"mis_x","project_id":"prj_x","outcome":"PASS","mission_resource_version":"1","acceptance_contract_version":"1","policy_version":"1","evidence_manifest_ref":"sha256:"+"b"*64,"failed_gate_codes":[],"issued_at":"2026-10-05T16:00:00Z","valid_until":None,"gates":{"evidence_complete":True,"acceptance_pass":True,"regression_pass":False,"checkpoint_present":True,"security_gate_pass":True,"privacy_gate_applicable":False,"privacy_gate_pass":False,"sensitive_data_security_gate_applicable":False,"sensitive_data_security_gate_pass":False,"recovery_pass":True,"donor_decoupling_pass":True,"project_isolation_pass":True}}
        with self.assertRaises(jsonschema.ValidationError): jsonschema.validate(instance, schema)

if __name__ == "__main__": unittest.main()
