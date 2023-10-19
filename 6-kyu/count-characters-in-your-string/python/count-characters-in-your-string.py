def count(s):
    char_count_dict = {}
    for character in s:
        if character not in char_count_dict:
            char_count_dict[character] = s.count(character)
    return char_count_dict