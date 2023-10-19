def first_n_smallest(arr, n):
    original_list = arr[:]
    index_value_mins = []
    while len(index_value_mins) < n and original_list:
        min_original_list = min(original_list)
        index_min = original_list.index(min_original_list)
        original_index_min = arr.index(min_original_list)
        while original_index_min in [elem[0] for elem in index_value_mins]:
            original_index_min = arr.index(min_original_list, original_index_min + 1)
        index_value_mins.append((original_index_min, original_list.pop(index_min)))
    return [elem[1] for elem in sorted(index_value_mins, key=lambda x: x[0])]