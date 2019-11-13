from src.roman_convertor_mod import calculate_number


def test_valid_combination_prior_valid_XL():
    input_str = 'CXL'
    return_value = calculate_number(input_str)
    assert return_value == 140


def test_valid_combination_prior_invalid_XL():
    input_str = 'IXL'
    return_value = calculate_number(input_str)
    assert return_value == 'Invalid'


def test_valid_combination_prior_invalid2_XL():
    input_str = 'XXL'
    return_value = calculate_number(input_str)
    assert return_value == 'Invalid'


def test_valid_combination_prior_invalid_XC():
    input_str = 'IXC'
    return_value = calculate_number(input_str)
    assert return_value == 'Invalid'


def test_valid_combination_prior_valid_XC():
    input_str = 'DXL'
    return_value = calculate_number(input_str)
    assert return_value == 540
