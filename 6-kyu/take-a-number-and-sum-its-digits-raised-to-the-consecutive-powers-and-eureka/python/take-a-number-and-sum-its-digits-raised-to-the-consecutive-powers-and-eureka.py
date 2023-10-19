def calculate_expected_number(n):
    digits = [int(x) for x in str(n)]
    final_int = 0
    for i, digit in enumerate(digits):
        i += 1
        final_int += digit ** i
    return final_int

def sum_dig_pow(a, b):
    final_list = []
    for i in range(a, b + 1):
        if i == calculate_expected_number(i):
            final_list.append(i)
        
    return final_list