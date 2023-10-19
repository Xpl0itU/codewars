def find_uniq(arr):
    occurrence_count_dict = {}
    for item in arr:
        if item not in occurrence_count_dict:
            occurrence_count_dict[item] = arr.count(item)
    for key, value in occurrence_count_dict.items():
        if value < 2:
            return key
    return None