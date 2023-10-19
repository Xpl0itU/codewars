def sum_strings(x, y):
    max_len = max(len(x), len(y))
    x = x.zfill(max_len)
    y = y.zfill(max_len)

    carry = 0
    result = ["0"] * max_len

    for i in range(max_len - 1, -1, -1):
        digit_sum = int(x[i]) + int(y[i]) + carry
        carry = digit_sum // 10
        result[i] = str(digit_sum % 10)

    if carry:
        result.insert(0, str(carry))

    final_result = "".join(result)

    final_result = final_result.lstrip("0")

    if not final_result:
        final_result = "0"

    return final_result