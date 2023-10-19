def get_middle(s):
    len_s = len(s)
    chars_to_get = []
    if len_s % 2 != 0:
        chars_to_get.append(int(len_s / 2))
    else:
        chars_to_get.append(int((len_s / 2) - 1))
        chars_to_get.append(int(len_s / 2))
    
    result_chars = ""
    for char_to_get in chars_to_get:
        result_chars += s[char_to_get]
    return result_chars