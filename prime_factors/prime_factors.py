def prime_generator(n):
    def is_prime(number_to_check):
        for i in range(2, number_to_check - 1):
            if number_to_check % i == 0:
                return False
        return True

    for number in range(2, n + 1):
        if is_prime(number):
            yield number


def prime_factors(number):
    def multiply_array(arr):
        result = 1
        for i in arr:
            result *= i
        return result

    prime_factors_list = []
    prime_number_generator = prime_generator(number)
    actual_prime_number = next(prime_number_generator)
    temp = number
    while multiply_array(prime_factors_list) != number:
        if temp % actual_prime_number == 0:
            prime_factors_list.append(actual_prime_number)
            temp = temp/actual_prime_number
        else:
            actual_prime_number = next(prime_number_generator)

    return prime_factors_list
