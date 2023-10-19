def disemvowel(string_):
    return "".join([char for char in string_ if char.lower() not in ["a", "e", "i", "o", "u"]])