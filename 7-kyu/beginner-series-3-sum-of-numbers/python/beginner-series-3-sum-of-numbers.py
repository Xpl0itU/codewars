def get_sum(a,b):
    sum_all_nums = 0
    for i in range(min(a, b), max(a, b) + 1):
        sum_all_nums += i
    return sum_all_nums