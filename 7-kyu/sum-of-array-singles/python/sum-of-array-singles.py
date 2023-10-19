def repeats(arr):
    filtered_list = [x for x in arr if arr.count(x) <= 1]
    return sum(filtered_list)