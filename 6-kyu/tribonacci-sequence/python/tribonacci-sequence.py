def tribonacci(signature, n):
    if n <= 3:
        final_list = []
        for i in range(n):
            final_list.append(signature[i])
        return final_list
    sequence = signature[:]
    for i in range(len(sequence) - 1, n - 1):
        last_three_nums = []
        for j in range(3):
            last_three_nums.append(sequence[i - j])
        sequence.append(sum(last_three_nums))
    return sequence