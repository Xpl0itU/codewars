def count_nested_lists(lst, count):
    count = 0
    for item in lst:
        if isinstance(item, list):
            count +=1
            count += count_nested_lists(item, count)
    return count

def compare_list(a, b):
    if len(a) != len(b):
        return False
    for item_a, item_b in zip(a, b):
        if isinstance(item_a, list) == list:
            compare_list(item_a, item_b)
    return True

def same_structure_as(original, other):
    if isinstance(original, list) != isinstance(other, list):
        return False
    if count_nested_lists(original, 0) != count_nested_lists(other, 0):
        return False
    for item_original, item_other in zip(original, other):
        item_original_is_list = isinstance(item_original, list)
        item_other_is_list = isinstance(item_other, list)
        if all([item_original_is_list, item_other_is_list]):
            if not compare_list(item_original, item_other):
                return False
        elif any([item_original_is_list, item_other_is_list]):
            return False

    return True