import unittest
from src.osint_checks import is_email, is_domain
from src.search import web_search

class TestOSINT(unittest.TestCase):
    def test_is_email(self):
        self.assertTrue(is_email("test@example.com"))
        self.assertFalse(is_email("not_an_email"))

    def test_is_domain(self):
        self.assertTrue(is_domain("example.com"))
        self.assertFalse(is_domain("invalid domain"))

    def test_web_search(self):
        results = web_search("test", max_results=2)
        self.assertGreater(len(results), 0)
        self.assertIn("title", results[0])

if __name__ == "__main__":
    unittest.main()
