from src.roman_convertor_mod import main, process_args
from dataclasses import dataclass
import argparse


@dataclass()
class mock_arguments:
    RomanNumeral: list


def test_main(capsys, mocker):
    roman_input = mock_arguments(['IV'])
    process_args_mocker = mocker.patch('src.roman_convertor_mod.process_args')
    process_args_mocker.return_value = roman_input
    main()
    captured = capsys.readouterr()
    assert f'numerical value : {4}' in captured.out


def test_parse_args(mocker):
    mocker_arguments = mocker.patch('argparse.ArgumentParser.parse_args')
    mocker_arguments.return_value = argparse.Namespace(RomanNumeral=['IV'])
    xx = process_args()
    # print(xx.RomanNumeral)
    assert xx.RomanNumeral[0] == 'IV'
