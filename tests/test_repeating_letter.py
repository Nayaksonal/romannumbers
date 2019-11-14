from src.roman_convertor_mod import top_level_calc


def test_repeating_III(capsys):
    input_str = 'III'
    top_level_calc(input_str)
    captured = capsys.readouterr()
    print(captured.out)
    assert f'numerical value for III : 3' in captured.out


def test_valid_VV(capsys):
    input_str = 'VV'
    top_level_calc(input_str)
    captured = capsys.readouterr()
    assert f'roman input VV is Invalid' in captured.out


def test_invalid_for_continous_four_sameletter(capsys):
    input_str = 'IIII'
    top_level_calc(input_str)
    captured = capsys.readouterr()
    assert f'roman input IIII is Invalid' in captured.out


def test_invalid_combination(capsys):
    input_str = 'IM'
    top_level_calc(input_str)
    captured = capsys.readouterr()
    print('trting to invalid combincation')
    print(captured.out)
    assert f'roman input IM is Invalid' in captured.out
