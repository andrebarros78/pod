import json
import unittest
from pathlib import Path
import jsonschema

ROOT = Path(__file__).resolve().parents[1]
SCHEMAS = ROOT / "SCHEMAS" / "v1"

class PrivacyContractTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data_schema = json.loads((SCHEMAS / "data_policy_envelope.schema.json").read_text(encoding="utf-8"))
        cls.decision_schema = json.loads((SCHEMAS / "privacy_decision.schema.json").read_text(encoding="utf-8"))

    def valid_data(self):
        return {"data_id":"dat_1","project_id":"prj_1","classification":"restricted","personal_data":True,"sensitive_personal_data":True,"child_or_adolescent_data":False,"subject_category":"customer","controller_ref":"ctl_1","operator_refs":[],"purpose_refs":["pur_1"],"authority_refs":["auth_1"],"source_ref":"src_1","lineage_ref":"lin_1","retention_policy_ref":"ret_1","allowed_operations":["READ"],"allowed_destinations":["internal"],"allowed_projects":["prj_1"],"external_processing_allowed":False,"international_transfer_policy_ref":None,"logging_policy":"redacted","encryption_required":True,"created_at":"2026-10-05T16:00:00Z","policy_version":"1"}

    def test_personal_data_without_purpose_is_rejected(self):
        instance = self.valid_data(); instance["purpose_refs"] = []
        with self.assertRaises(jsonschema.ValidationError): jsonschema.validate(instance, self.data_schema)

    def test_sensitive_data_without_encryption_requirement_is_rejected(self):
        instance = self.valid_data(); instance["encryption_required"] = False
        with self.assertRaises(jsonschema.ValidationError): jsonschema.validate(instance, self.data_schema)

    def test_privacy_allow_requires_purpose_and_policy_allow_reason(self):
        instance = {"decision_id":"pvd_1","project_id":"prj_1","operation_id":"op_1","data_ids":["dat_1"],"operation":"READ","purpose_id":None,"policy_version":"1","destination_ref":"internal","processor_ref":None,"decision":"allow","reason_codes":["UNKNOWN_PURPOSE"],"minimization_applied":True,"transformation_refs":[],"expires_at":None,"decided_at":"2026-10-05T16:00:00Z","engine_version":"contract-v1"}
        with self.assertRaises(jsonschema.ValidationError): jsonschema.validate(instance, self.decision_schema)

if __name__ == "__main__": unittest.main()
