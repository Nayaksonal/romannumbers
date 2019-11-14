from src.roman_convertor_mod import top_level_calc


def test_valid_combination_prior_valid_XL(capsys):
    input_str = 'CXL'
    top_level_calc(input_str)
    captured = capsys.readouterr()
    print(captured.out)
    assert f'numerical value : 140' in captured.out


def test_valid_combination_prior_invalid_XL(capsys):
    input_str = 'IXL'
    top_level_calc(input_str)
    captured = capsys.readouterr()
    assert f'roman input IXL is Invalid' in captured.out


def test_valid_combination_prior_invalid2_XL(capsys):
    input_str = 'XXL'
    top_level_calc(input_str)
    captured = capsys.readouterr()
    assert f'roman input XXL is Invalid' in captured.out


def test_valid_combination_prior_invalid_XC(capsys):
    input_str = 'IXC'
    top_level_calc(input_str)
    captured = capsys.readouterr()
    assert f'roman input IXC is Invalid' in captured.out


def test_valid_combination_prior_valid_XC(capsys):
    input_str = 'DXL'
    top_level_calc(input_str)
    captured = capsys.readouterr()
    assert f'numerical value : 540' in captured.out
