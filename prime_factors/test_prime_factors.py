import unittest
from prime_factors import prime_generator, prime_factors


class TestPrimeGenerator(unittest.TestCase):

    def test_prime_generator(self):
        prime_numbers = [1, 2, 3, 5, 7, 11, 13, 17, 19, 23]
        outputs = [[i for i in prime_generator(23)], [i for i in prime_generator(26)]]
        assert prime_numbers == outputs[0]
        assert prime_numbers == outputs[1]



class TestPrimeFactors(unittest.TestCase):

    def test_prime_factors(self):
        assert True


if __name__ == '__main__':
    unittest.main()
