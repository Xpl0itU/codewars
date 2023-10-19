def narcissistic( value ):
    digits = [int(x) for x in str(value)]
    len_value = len(digits)
    narc_number = 0
    for digit in digits:
        narc_number += digit ** len_value
    return value == narc_number