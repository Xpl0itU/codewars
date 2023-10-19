def find_missing_letter(chars):
    missing_letter = 0
    for i, char in enumerate(chars):
        next_letter = ord(char) + 1
        if i + 1 >= len(chars):
            break
        if next_letter != ord(chars[i + 1]):
            missing_letter = next_letter
        
    return chr(missing_letter)

