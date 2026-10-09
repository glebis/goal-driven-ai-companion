"""Dependency-free package and cross-skill integration checks."""
import json
from pathlib import Path
import re
import unittest

ROOT = Path(__file__).resolve().parents[1]
SKILLS = {'companion', 'lab-context', 'lab-homework', 'lab-review', 'lab-setup'}

class PackageTest(unittest.TestCase):
    def test_manifest(self):
        manifest = json.loads((ROOT / '.claude-plugin/plugin.json').read_text())
        self.assertEqual(manifest['name'], 'goal-driven-ai')
        self.assertEqual(manifest['license'], 'MIT')

    def test_all_skills_and_local_references(self):
        self.assertEqual({p.name for p in (ROOT / 'skills').iterdir() if p.is_dir()}, SKILLS)
        for path in (ROOT / 'skills').rglob('*.md'):
            text = path.read_text()
            for target in re.findall(r'\]\(([^)]+)\)', text):
                if '://' not in target and not target.startswith('#'):
                    self.assertTrue((path.parent / target.split('#')[0]).exists(), f'{path}: {target}')
        for name in SKILLS:
            text = (ROOT / 'skills' / name / 'SKILL.md').read_text()
            self.assertIn(f'name: {name}', text)
            self.assertNotIn('Default: English', text)
            self.assertNotIn('~/claude-lab-vault/', text)

    def test_coaching_routes_share_context(self):
        companion = (ROOT / 'skills/companion/SKILL.md').read_text()
        for name in SKILLS - {'companion'}:
            self.assertIn(f'../{name}/SKILL.md', companion)
            body = (ROOT / 'skills' / name / 'SKILL.md').read_text()
            self.assertIn('../companion/references/persistence.md', body)
            self.assertIn('Saving is optional', body)

    def test_installer_includes_course_skills(self):
        readme = (ROOT / 'README.md').read_text()
        self.assertIn('--agent codex -g -y', readme)
        self.assertNotIn('--skill companion', readme)

if __name__ == '__main__':
    unittest.main()
