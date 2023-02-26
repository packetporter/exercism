"""
A program to convert a list of digits from one base to another.
The hexadecimal base digits are using the numbers and not letters for characters greater than 9 as per convention
"""
def _divisor(digit, output_base):
    """
    Function used to divide a number with the output base required. This is a helper function for converting decimals
    numbers to other bases
    
    :param digit, output_base: int - number and divisor
    :return: tuple - Tuple returned which is a result of the divison and remainder of the division
    """
    new_digit = int(digit/output_base)
    remainder = digit % output_base
    return (new_digit, remainder)

def _convert_list_to_int(digit_list):
    """
    Helper function to combine a list of digits to a single decimal number

    :param digit_list: list - list of digits making up a decimal number
    :return: int - combined decimal
    """
    result = int("".join(map(str, digit_list)))
    return result

def decimal_to_other_base(digits, output_base):
    """
    Function to convert a decimal number to a non-decimal number

    :param digit: list - a list of digits that make up the decimal number. List items range from 0 - 9
    :param output_base: int - a interger of the base that the decimal will be converted to
    :return: list - A list of digits representing the new base
    """
    output_digit_list=[]
    digits_int = _convert_list_to_int(digits)
    if digits_int == 0:
        return [0]
    
    while digits_int > 0:
            (digits_int, remainder) = _divisor(digits_int, output_base)
            output_digit_list.insert(0, remainder)
    return output_digit_list

def other_base_to_decimal(digits, input_base):
    """
    Function to convert any base to a decimal

    :param digits: list - a list of digits that make up the non-decimal number. List items range from 0 - (input_base-1)
    :param input_base: int - a interger of the base of the input digits
    :return: list - A list of digits representing the decimal number
    """
    digit_length = len(digits)
    power_list = [pow(input_base, x) for x in reversed(range(digit_length))]
    resultant_list = list(map(lambda x, y: x * y, digits, power_list))
    converted_decimal = sum(resultant_list)

    return [int(i) for i in str(converted_decimal)]

def rebase(input_base, digits, output_base):
    """
    Main funtion that is rebasing a number from one base to another. Conversion off to/from base 10 number is done directly
    to the output base while other bases are first converted to base 10 then to the output base

    :param input_base: int - integer of the base of the given digits
    :param digits: list - a list of digits to be converted from the input base to the output base
    :param output_base: int - integer of the base the list of digits will be converted to
    :return: list - a list of the converted digits
    """
    if input_base < 2:
         raise ValueError("input base must be >= 2")
    for digit in digits:
        if not(input_base > digit >= 0):
            raise ValueError("all digits must satisfy 0 <= d < input base")
    if output_base < 2:
        raise ValueError("output base must be >= 2")

    if output_base == 10:
        return other_base_to_decimal(digits, input_base)

    elif input_base == 10:
        return decimal_to_other_base(digits, output_base)   

    else:
        digits_to_decimal = other_base_to_decimal(digits, input_base)
        return decimal_to_other_base(digits_to_decimal, output_base)


