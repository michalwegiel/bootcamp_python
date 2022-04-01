def prime_generator(n):
    def is_prime(number_to_check):
        for i in range(2, number_to_check - 1):
            if number_to_check % i == 0:
                return False
        return True

    for number in range(1, n + 1):
        if is_prime(number):
            yield number


def prime_factors(number):
    pass
