import json
from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]


class PortfolioContractTests(unittest.TestCase):
    def test_project_evidence_is_complete_and_unique(self):
        value = json.loads((ROOT / "portfolio/projects.json").read_text())
        self.assertEqual(value["schema"], "kairo.portfolio.v1")
        projects = value["projects"]
        self.assertEqual(len(projects), 4)
        self.assertEqual(len({item["repository"] for item in projects}), 4)
        self.assertTrue(all(item["repository"].startswith("https://github.com/") for item in projects))
        self.assertTrue(any("Python" in item["languages"] for item in projects))
        self.assertTrue(all(item["artist_outcome"].endswith(".") for item in projects))

    def test_required_application_documents_exist(self):
        for path in (
            "docs/DEMO_SCRIPT.md", "docs/INSTALLATION.md",
            "docs/NATIVE_VERIFICATION.md", "README.md",
        ):
            self.assertTrue((ROOT / path).is_file(), path)
