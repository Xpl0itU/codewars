def positive_sum(arr):
    sum = 0
    for num in arr:
        sum += max(0, num)
    return sum
