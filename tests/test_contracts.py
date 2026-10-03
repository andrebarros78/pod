import json
import subprocess
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

class ContractTests(unittest.TestCase):
    def test_contract_validator(self):
        p = subprocess.run([sys.executable, str(ROOT/'scripts'/'validate_contracts.py')], capture_output=True, text=True)
        self.assertEqual(p.returncode, 0, p.stdout + p.stderr)
        self.assertIn('POD_CONTRACTS_VALID', p.stdout)

    def test_proto_contains_all_minimum_contracts(self):
        text=(ROOT/'SCHEMAS'/'v1'/'pod.proto').read_text(encoding='utf-8')
        names=['Project','Mission','Task','TaskGraph','Command','Event','StateTransition','ExecutionRequest','ExecutionLease','ExecutionEvent','ExecutionResult','CapabilityDescriptor','NodeIdentity','NodeHeartbeat','ResourceClaim','AuthorizationGrant','AuthorizationDenial','Checkpoint','EvidenceRecord','Incident','RecoveryAction','GitIntent','ArtifactManifest','KnowledgeRecord','ProviderDescriptor']
        for name in names:
            self.assertIn(f'message {name} ', text)

    def test_arms_contract_supports_32(self):
        text=(ROOT/'SCHEMAS'/'v1'/'pod.proto').read_text(encoding='utf-8')
        self.assertIn('message ArmDescriptor', text)
        self.assertIn('uint32 logical_arm', text)

if __name__ == '__main__':
    unittest.main()
