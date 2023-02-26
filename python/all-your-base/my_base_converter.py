def number_to_letter_func(number):
    num_letter_dict = {
        10: 'A',
        11: 'B',
        12: 'C',
        13: 'D',
        14: 'E',
        15: 'F'
    }

    return num_letter_dict[number]

def letter_to_number_func(letter):
    letter_num_dict = {
        'A': 10,
        'B': 11,
        'C': 12,
        'D': 13,
        'E': 14,
        'F': 15
    }

    return letter_num_dict[letter]

def _divisor(digit, output_base):
    new_digit = int(digit/output_base)
    remainder = digit % output_base

    if remainder > 9 and output_base == 16:
        remainder = number_to_letter_func(remainder)

    return (new_digit, remainder)

def decimal_to_other_base(digits, output_base):
    output_digit_list=[]
    while digits > 0:
            (digits, remainder) = _divisor(digits, output_base)
            output_digit_list.insert(0, remainder)
    output_digit_list = [str(dig) for dig in output_digit_list]   
    return "".join(output_digit_list)

def other_base_to_decimal(digits, input_base):
    hexa_characters = {'A', 'B', 'C', 'D', 'E', 'F'}
    digit_length = len(str(digits))
    digit_list = list(str(digits))
    for i in range(digit_length):
        if digit_list[i] in hexa_characters:
            digit_list[i] = letter_to_number_func(digit_list[i])
    digit_list = [int(x) for x in digit_list]
    power_list = [pow(input_base, x) for x in reversed(range(digit_length))]
    resultant_list = list(map(lambda x, y: x * y, digit_list, power_list))

    return sum(resultant_list)

def rebase(input_base, digits, output_base):
    if output_base == 10:
        return other_base_to_decimal(digits, input_base)

    elif input_base == 10:
         other_base_to_decimal(digits, output_base)   

    else:
        digits_to_decimal = other_base_to_decimal(digits, input_base)
        return decimal_to_other_base(digits_to_decimal, output_base)


print(rebase(3, 1120, 16))
