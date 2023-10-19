def find_even_index(arr):
    left_side = []
    right_side = []
    for i in range(len(arr)):
        left_side = arr[:i]
        right_side = arr[i + 1:]
        if sum(left_side) == sum(right_side):
            return i
    return -1