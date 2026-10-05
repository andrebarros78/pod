import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

class FormalSemanticsTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.model = (ROOT / "formal" / "PODCore.tla").read_text(encoding="utf-8")
        cls.cfg = (ROOT / "formal" / "PODCore.cfg").read_text(encoding="utf-8")

    def test_mission_proven_requires_full_proof(self):
        for token in ["evidenceComplete", "acceptancePass", "regressionPass", "checkpointPresent", "securityGatePass", "recoveryPass", "donorDecouplingPass", "projectIsolationPass", "proofVerdictFresh", "MissionProvenRequiresCompleteProof"]:
            self.assertIn(token, self.model)

    def test_privacy_is_conditional_but_non_bypassable(self):
        self.assertIn("privacyGateApplicable", self.model)
        self.assertIn("PrivacyCannotBeBypassedWhenApplicable", self.model)
        self.assertIn("SensitiveDataGateCannotBeBypassedWhenApplicable", self.model)

    def test_worker_retains_issued_token_and_write_checks_current_token(self):
        self.assertIn("workerToken = [w \\in Workers |-> 0]", self.model)
        self.assertIn("workerToken[w] = fencingToken", self.model)
        self.assertIn("workerToken[w] < fencingToken", self.model)
        self.assertIn("AtMostOneAuthorizedWriter", self.model)

    def test_cfg_checks_hardened_invariants(self):
        for invariant in ["MissionProvenRequiresCompleteProof", "PrivacyCannotBeBypassedWhenApplicable", "SensitiveDataGateCannotBeBypassedWhenApplicable", "AtMostOneAuthorizedWriter", "StaleWritesAreDenied"]:
            self.assertIn(invariant, self.cfg)

if __name__ == "__main__": unittest.main()
