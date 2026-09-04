"""Validate both host catalogs without fetching or installing plugins."""
import json
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parent.parent


class TestMarketplace(unittest.TestCase):
    def test_codex_catalog_preserves_plugin_identity_and_source(self):
        claude = json.loads((ROOT / ".claude-plugin/marketplace.json").read_text())
        codex = json.loads((ROOT / ".agents/plugins/marketplace.json").read_text())
        self.assertEqual(codex["name"], claude["name"])
        self.assertEqual([(p["name"], p["source"]) for p in codex["plugins"]],
                         [(p["name"], p["source"]) for p in claude["plugins"]])
        for plugin in codex["plugins"]:
            self.assertEqual(plugin["policy"]["installation"], "AVAILABLE")
            self.assertEqual(plugin["policy"]["authentication"], "ON_INSTALL")
            self.assertEqual(plugin["category"], "Productivity")

    def test_claude_catalog_keeps_the_retired_plugin_migration(self):
        claude = json.loads((ROOT / ".claude-plugin/marketplace.json").read_text())
        self.assertEqual(claude["renames"], {"exactory-verifier": "exactory"})
        self.assertEqual([p["name"] for p in claude["plugins"]], ["exactory"])


if __name__ == "__main__":
    unittest.main()
