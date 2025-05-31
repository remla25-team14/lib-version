from libversion import VersionUtil, __version__
import unittest
import libversion
import re

print("Current version via VersionUtil.get_version():", VersionUtil.get_version())
print("Current version via __version__:", __version__)

class TestVersion(unittest.TestCase):
    def test_version_is_available(self):
        """Test that version is available and follows semantic versioning"""
        version = libversion.__version__
        self.assertIsNotNone(version)
        
        # Extract the base version (X.Y.Z) from development version format
        base_version = re.match(r'(\d+\.\d+\.\d+)', version)
        self.assertIsNotNone(base_version, "Version should start with semantic versioning X.Y.Z")
        
        # Check if base version follows semantic versioning (e.g., 1.2.3)
        parts = base_version.group(1).split('.')
        self.assertEqual(len(parts), 3, "Base version should follow semantic versioning X.Y.Z")
        for part in parts:
            self.assertTrue(part.isdigit(), "Version parts should be numeric")

if __name__ == '__main__':
    unittest.main()