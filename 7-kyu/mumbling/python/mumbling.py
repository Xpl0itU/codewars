def accum(s):
    final_string = ""
    for i, char in enumerate(s):
        for j in range(i + 1):
            if j == 0:
                final_string += char.upper()
            else:
                final_string += char.lower()
        final_string += "-"
    return final_string[:-1]