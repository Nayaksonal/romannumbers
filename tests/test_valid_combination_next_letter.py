from src.roman_convertor_mod import calculate_number


def test_valid_combination_valid():
    input_str = 'XLI'
    return_value = calculate_number(input_str)
    assert return_value == 41


def test_valid_combination_next_invalid():
    input_str = 'XLX'
    return_value = calculate_number(input_str)
    assert return_value == 'Invalid'


def test_valid_combination_next_invalid2():
    input_str = 'XLD'
    return_value = calculate_number(input_str)
    assert return_value == 'Invalid'


def test_valid_combination_next_multiple_valid():
    input_str = 'XLIX'
    return_value = calculate_number(input_str)
    assert return_value == 49


def test_valid_combination_next_invalid_XC():
    input_str = 'XCX'
    return_value = calculate_number(input_str)
    assert return_value == 'Invalid'


def test_valid_combination_next_valid_XC():
    input_str = 'XCI'
    return_value = calculate_number(input_str)
    assert return_value == 91
