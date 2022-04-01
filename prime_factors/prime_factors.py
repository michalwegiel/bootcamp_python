def factors(n):
    yield 2
    i = 1
    while i < n:
        i += 2
        yield i


def prime_factors(number):
    def multiply_array(arr):
        result = 1
        for i in arr:
            result *= i
        return result

    prime_factors_list = []
    factors_gen = factors(number)
    actual_factor = next(factors_gen)
    temp = number
    while multiply_array(prime_factors_list) != number:
        if temp % actual_factor == 0:
            prime_factors_list.append(actual_factor)
            temp = temp/actual_factor
        else:
            actual_factor = next(factors_gen)

    return prime_factors_list


