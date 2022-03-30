import unittest
from palindrome import is_palindrome


class TestPalindrome(unittest.TestCase):

    def test_palindrome_true(self):
        self.assertTrue(is_palindrome("kajak"))

    def test_palindrome_false(self):
        self.assertFalse(is_palindrome("blabla"))


if __name__ == '__main__':
    unittest.main()
