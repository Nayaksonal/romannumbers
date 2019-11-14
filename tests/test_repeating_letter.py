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
