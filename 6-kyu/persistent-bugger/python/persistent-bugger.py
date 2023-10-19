def mult(lst):
    result = 1
    for x in lst:
        result = result * x
    return result

def persistence(n):
    iterations = 0
    sum_digits = n
    digits = [int(x) for x in str(n)]
    while len(digits) != 1:
        sum_digits = mult(digits)
        digits = [int(x) for x in str(sum_digits)]
        iterations += 1
    return iterations