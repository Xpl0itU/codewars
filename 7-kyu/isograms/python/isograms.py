def is_isogram(string):
    char_occurrence_dict = {}
    for char in string.lower():
        if char in char_occurrence_dict.keys():
            return False
        char_occurrence_dict[char] = 1
    return True