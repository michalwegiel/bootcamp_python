import pytest
from roman_to_int import roman_to_int


def test_roman_to_int():
    scenarios = {"I": 1,
                 "II": 2,
                 "III": 3,
                 "IV": 4,
                 "V": 5,
                 "VI": 6,
                 "VII": 7,
                 "VIII": 8,
                 "IX": 9,
                 "X": 10,
                 }
    for k, v in scenarios.items():
        assert roman_to_int(k) == v
