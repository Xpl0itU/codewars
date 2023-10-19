def get_count(sentence):
    vowel_count = 0
    for char in sentence:
        if char in ["a", "e", "i", "o", "u"]:
            vowel_count += 1
    return vowel_count