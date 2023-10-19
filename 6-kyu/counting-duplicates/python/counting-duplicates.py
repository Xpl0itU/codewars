def duplicate_count(text):
    character_count_dict = {}
    text_lower = text.lower()
    for character in text_lower:
        if character not in character_count_dict:
            character_count_dict[character] = text_lower.count(character)
    repeating_chars = 0
    for occurrence_count in character_count_dict.values():
        if occurrence_count > 1:
            repeating_chars += 1
    return repeating_chars
     