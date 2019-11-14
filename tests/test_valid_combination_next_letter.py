from src.roman_convertor_mod import top_level_calc


def test_valid_combination_valid(capsys):
    input_str = 'XLI'
    top_level_calc(input_str)
    captured = capsys.readouterr()
    print(captured.out)
    assert f'numerical value : 41' in captured.out


def test_valid_combination_next_invalid(capsys):
    input_str = 'XLX'
    top_level_calc(input_str)
    captured = capsys.readouterr()
    print(captured.out)
    assert f'roman input XLX is Invalid' in captured.out


def test_valid_combination_next_invalid2(capsys):
    input_str = 'XLD'
    top_level_calc(input_str)
    captured = capsys.readouterr()
    # print(captured.out)
    assert f'roman input XLD is Invalid' in captured.out


def test_valid_combination_next_multiple_valid(capsys):
    input_str = 'XLIX'
    top_level_calc(input_str)
    captured = capsys.readouterr()
    print(captured.out)
    assert f'numerical value : 49' in captured.out


def test_valid_combination_next_invalid_XC(capsys):
    input_str = 'XCX'
    top_level_calc(input_str)
    captured = capsys.readouterr()
    assert f'roman input XCX is Invalid' in captured.out


def test_valid_combination_next_valid_XC(capsys):
    input_str = 'XCI'
    top_level_calc(input_str)
    captured = capsys.readouterr()
    assert f'numerical value : 91' in captured.out
