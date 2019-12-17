from src.number_to_roman import convert_number_roman,  know_highest_value_in_list
import pytest

test_list = [
    ('20', 'XX'),
    ('10', 'X'),
    ('6', 'VI'),
    ('4', 'IV'),
    ('36', 'XXXVI'),
    ('1000', 'M'),
]


@pytest.mark.parametrize("input_value, expected", test_list)
def test_conver_number_to_roman(input_value, expected):
    roman_numeral = convert_number_roman(int(input_value))
    assert roman_numeral == expected


def test_know_highest_value_in_list():
    assert know_highest_value_in_list(20) == '10'


def test_zero():
    assert know_highest_value_in_list(0) == '0'
