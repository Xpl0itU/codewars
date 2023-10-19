brace_pairs = {")": "(", "]": "[", "}": "{"}

def is_opener_brace(brace):
    return brace in brace_pairs.values()

def is_closer_brace(brace):
    return brace in brace_pairs.keys()

def valid_braces(string):
    temp_array = []
    for character in string:
        if not is_opener_brace(character) and not is_closer_brace(character):
            return False
        if is_opener_brace(character):
            temp_array.append(character)
            continue
        if is_closer_brace(character):
            if len(temp_array) == 0 or temp_array.pop() != brace_pairs[character]:
                return False
    return len(temp_array) == 0