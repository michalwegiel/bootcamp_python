from typing import Dict


def roman_to_int(roman: str) -> int:
    """
    :param roman: str
    :return: int
    Tests:
    >>> roman_to_int("I")
    1
    >>> roman_to_int("XI")
    11
    >>> roman_to_int("L")
    50
    >>> roman_to_int("")
    ValueError: Input value must be string and valid roman number
    >>> roman_to_int("IIII")
    ValueError: Input value must be string and valid roman number
    """
    symbols: Dict[str, int] = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000,
    }
    value: int = 0
    previous: int = 0

    for i in roman:
        current = symbols[i]
        if current > previous:
            value = value + current - 2 * previous
        else:
            value += current
        previous = current

    return value
