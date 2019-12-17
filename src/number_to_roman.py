

number_dict = {
    '1': 'I',
    '4': 'IV',
    '5': 'V',
    '9': 'IX',
    '10': 'X',
    '40': 'XL',
    '50': 'L',
    '90': 'XC',
    '100': 'C',
    '400': 'CD',
    '500': 'D',
    '900': 'CM',
    '1000': 'M',
    }


def convert_number_roman(mynum: int):
    remainder = mynum
    roman_list = []
    while remainder > 0:
       highest_dec = know_highest_value_in_list(remainder)
       roman_list.append(number_dict.get(highest_dec))
       remainder = remainder - int(highest_dec)

    romannumeral = ''.join(roman_list)
    # print(f'romannumeral for {mynum}: {romannumeral}')

    return romannumeral



def know_highest_value_in_list(mynum):
    if mynum == 0:
        return '0'
    else:
        position = '1'
    for k in number_dict.keys():
        if int(k) > mynum:
            # return position
            break
        position = k
    return position
