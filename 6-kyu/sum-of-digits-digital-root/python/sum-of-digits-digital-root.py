def digital_root(n):
    sum_digits = n
    digits = [int(x) for x in str(n)]
    while len(digits) != 1:
        sum_digits = sum(digits)
        digits = [int(x) for x in str(sum_digits)]
    return sum_digits