def duplicate_encode(word):
    character_count_dict = {}
    word_lower = word.lower()
    for character in word_lower:
        if character not in character_count_dict:
            character_count_dict[character] = word_lower.count(character)
    
    final_string = ""
    for character in word_lower:
        if character_count_dict[character] > 1:
            final_string += ")"
        else:
            final_string += "("

    return final_string