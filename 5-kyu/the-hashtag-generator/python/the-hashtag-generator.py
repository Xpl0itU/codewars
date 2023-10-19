def generate_hashtag(s):
    word_list = s.split()
    if len(word_list) == 0:
        return False
    final_string = "#"
    for i in range(len(word_list)):
        final_string += word_list[i][0].upper()
        final_string += word_list[i][1:].lower()
    return final_string if len(final_string) < 141 else False