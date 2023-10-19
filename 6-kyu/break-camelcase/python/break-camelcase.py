def solution(s):
    final_string = ""
    for character in s:
        if character.isupper():
            final_string += " "
        final_string += character
    return final_string