from .context import src
import unittest

class AudioTests(unittest.TestCase):
    def test_files_in_directory(self):
        expected = ''
        result = src.files_in_directory('/data')
        self.assertEqual(expected, result)

if __name__=='__main__':
    unittest.main()
