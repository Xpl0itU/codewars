def next_smaller(n):
    digits = [int(x) for x in str(n)]
    len_digits = len(digits)

    for i in range(len_digits - 1, 0, -1):
        if digits[i] < digits[i - 1]:
            break
    else:
        return -1

    for j in range(len_digits - 1, i - 1, -1):
        if digits[j] < digits[i - 1]:
            digits[i - 1], digits[j] = digits[j], digits[i - 1]
            break

    digits[i:] = sorted(digits[i:], reverse=True)

    result = int("".join(map(str, digits)))
    if result < n and len(str(result)) == len(str(n)):
        return result
    else:
        return -1