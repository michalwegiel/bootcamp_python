import unittest
from palindrome import is_palindrome


class TestPalindrome(unittest.TestCase):

    def test_palindrome_true(self):
        scenarios = [
            '',
            ' ',
            'kajak',
            'ala',
            'Ala',
            'ALA',
            'Akta ma w teczce twa matka',
            'I co idioci?',
            'O, mam karabin i barak mamo!',
            'ALA!@#$%^&*()<>,.?/;:'"[]{}",
        ]
        for scenario in scenarios:
            self.assertTrue(is_palindrome(scenario))

    def test_palindrome_false(self):
        scenarios = [
            'balbla',
            'ala ma kota',
            'MIOPQQQdsjhdskjhd',
        ]
        for scenario in scenarios:
            self.assertFalse(is_palindrome(scenario))

    def test_palindrome_negative(self):
        scenarios = [
            4,
            None,
            [],
            {'Ala': 1},
        ]
        for scenario in scenarios:
            with self.assertRaises(ValueError):
                is_palindrome(scenario)


if __name__ == '__main__':
    unittest.main()
