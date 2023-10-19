def duplicate_encode(word):
    final_string = ""
    word_lower = word.lower()
    for character in word_lower:
        if word_lower.count(character) > 1:
            final_string += ")"
        else:
            final_string += "("
    return final_string