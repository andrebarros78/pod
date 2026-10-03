import json
import subprocess
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

class GovernanceTests(unittest.TestCase):
    def test_validator_passes(self):
        p = subprocess.run([sys.executable, str(ROOT/'scripts'/'validate_governance.py')], capture_output=True, text=True)
        self.assertEqual(p.returncode, 0, p.stdout + p.stderr)
        self.assertIn('POD_GOVERNANCE_VALID', p.stdout)

    def test_history_is_non_normative(self):
        self.assertIn('NORMATIVE=false', (ROOT/'HISTORY'/'README.md').read_text(encoding='utf-8'))

    def test_mission_state_points_to_github(self):
        state = json.loads((ROOT/'MISSION_STATE.json').read_text(encoding='utf-8'))
        self.assertEqual(state['repository'], 'https://github.com/andrebarros78/pod')
        self.assertEqual(state['phase'], 0)

    def test_32_arms_are_fixed_logical_capacity(self):
        text = (ROOT/'ADR'/'ADR-002-BRACOS-LOGICOS-ESPECIALISTAS-32.md').read_text(encoding='utf-8')
        self.assertIn('MAX_LOGICAL_ARMS = 32', text)
        for n in range(1, 33):
            self.assertIn(f'{n:02d} —', text)

if __name__ == '__main__':
    unittest.main()
