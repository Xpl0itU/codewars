def remov_nb(n):
    total_sum = n * (n + 1) // 2
    result = []

    for a in range(1, n + 1):
        b_sum = total_sum - a
        if b_sum % (a + 1) == 0 and b_sum // (a + 1) <= n:
            result.append((a, b_sum // (a + 1)))

    return result