import argparse
# import sys

roman_dict = {
    "I":
        {"position": 1,
         "value": 1
         },
    "V":
        {"position": 2,
         "value": 5
         },
    "X": {"position": 3,
          "value": 10
          },
    "L": {"position": 4,
          "value": 50
          },
    "C": {"position": 5,
          "value": 100
          },
    "D": {"position": 6,
          "value": 500
          },
    "M": {"position": 7,
          "value": 1000
          },
}


def process_args():
    parser = argparse.ArgumentParser(description='Roman numeral convertor')
    parser.add_argument('--RomanNumeral', metavar='input',
                        type=str, nargs='+',
                        help='Please enter Roman Numeral to be converted')
    return parser.parse_args()


def main():
    # roman_input = "CLMXVI"
    args = process_args()
    roman_input = args.RomanNumeral[0]
    top_level_calc(roman_input)


def top_level_calc(roman_input):
    if _check_repeating_letters(roman_input) == 'Valid':
        return_value = _calculate_number(roman_input)
        print(f'numerical value : {return_value}')


def _calculate_number(roman_input: str):

    valid_combination = ['IV', 'IX', 'XL', 'XC', 'CD', 'CM']
    sum = 0
    len1 = len(roman_input)
    print(f'length : {len1}')
    for i, letter in enumerate(roman_input):
        letter_value = roman_dict.get(letter).get("value")
        # print(f'letter :{i} {letter}')
        if i >= len1-1:
            temp = letter_value
        else:
            next_letter = roman_input[i+1]
            # print(f'next letter : {next_letter}')
            letter_position = roman_dict[letter]['position']
            next_letter_position = roman_dict[next_letter]['position']
            if letter_position < next_letter_position:
                temp = letter_value * -1
                if f'{letter}{next_letter}' not in valid_combination:
                    print(f'roman input {roman_input} is Invalid')
                    return 'Invalid'
                else:
                    if i != 0:
                        earlier_letter = roman_input[i-1]
                        print(f'earlier letter at {i-1} : {earlier_letter}')
                        earlier_letter_position =\
                            roman_dict[earlier_letter]['position']
                        earlier_letter_value = \
                            roman_dict[earlier_letter]['value']
                        if earlier_letter_position < next_letter_position:
                            print(f'roman input {roman_input} is Invalid')
                            return 'Invalid'
                        elif earlier_letter_position == next_letter_position\
                                and earlier_letter_value % 10 != 0:
                            print(f'roman input {roman_input} is Invalid')
                            return 'Invalid'
                    # checking next letters for combination
                    if i+2 < len1:
                        junk_letter = roman_input[i+2]
                        junk_letter_position = \
                            roman_dict[junk_letter]['position']
                        if junk_letter_position >= letter_position:
                            print(f'roman input {roman_input} is Invalid')
                            return 'Invalid'
            else:
                temp = letter_value
        sum = sum + temp
    return sum


def _check_repeating_letters(roman_input):
    non_repeatable_letters = ['V', 'L', 'D']
    cnt = 0
    len1 = len(roman_input)
    for i, letter in enumerate(roman_input):
        # print(f'for i: {i} value of cnt {cnt}')
        if i+1 < len1 and letter == roman_input[i+1]:
            if letter in non_repeatable_letters:
                print(f'roman input {roman_input} is Invalid')
                return 'Invalid'
            cnt = cnt + 1
        else:
            cnt = 0

        if cnt >= 3:
            print(f'roman input {roman_input} is Invalid')
            return 'Invalid'

    return 'Valid'


if __name__ == '__main__':
    main()
