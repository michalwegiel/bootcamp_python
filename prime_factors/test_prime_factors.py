import unittest
from prime_factors import prime_factors


class TestPrimeFactors(unittest.TestCase):

    def test_prime_factors(self):
        input_values = [7, 2, 6, 8, 1621, 3958159172]
        expected_outputs = [[7], [2], [2, 3], [2, 2, 2], [1621], [2, 2, 11, 2347, 38329]]
        for input_value, expected in zip(input_values, expected_outputs):
            assert expected == prime_factors(input_value)

    def test_prime_factors_negative(self):
        input_values = [4.3, "abcd", -1, [], {}]
        for input_value in input_values:
            with self.assertRaises(ValueError):
                prime_factors(input_value)


if __name__ == '__main__':
    unittest.main()
