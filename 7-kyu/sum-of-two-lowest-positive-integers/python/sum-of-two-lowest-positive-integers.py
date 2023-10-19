def sum_two_smallest_numbers(numbers):
    first_min_num = 0
    second_min_num = 0
    first_min_num = min(numbers)
    numbers.remove(first_min_num)
    second_min_num = min(numbers)
    return first_min_num + second_min_num