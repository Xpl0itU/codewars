def longest(a1, a2):
    tmp = ""
    for char in a1:
        if char not in tmp:
            tmp += char
    for char in a2:
        if char not in tmp:
            tmp += char
    return "".join(sorted(tmp))