import pytest
from roman_to_int import roman_to_int


def test_roman_to_int():
    scenarios = {
        "I": 1,
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


def test_roman_to_int_advanced_scenarios():
    scenarios = {
        "XVIII": 18,
        "XXIII": 23,
        "XXXIII": 33,
        "XXXIX": 39,
        "XLI": 41,
        "LXXX": 80,
        "LXXXIX": 89,
        "XCIX": 99,
        "CC": 200,
        "CD": 400,
        "CM": 900,
        "MMMCMXCIX": 3999,
    }
    for k, v in scenarios.items():
        assert roman_to_int(k) == v


def test_roman_to_negative():
    scenarios = [
        1,
        2.4,
        [1, 2],
        {"I": 1},
        None,
        "",
        "IIV",
        "XXXX",
        "MCMC",
        "String",
    ]
    for scenario in scenarios:
        with pytest.raises(ValueError):
            roman_to_int(scenario)
