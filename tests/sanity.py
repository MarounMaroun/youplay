import unittest

from youplay.youplay import get_links


class BaseTest(unittest.TestCase):

    def test_basic_extraction(self):
        """Verify YouTube HTML page wasn't changed.
        """
        self.assertTrue(get_links('yesterday beatles'))

if __name__ == '__main__':
    unittest.main()
