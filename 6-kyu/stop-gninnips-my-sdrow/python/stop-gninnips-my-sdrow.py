def spin_words(words):
    word_list = words.split()
    spinned_word_list = []
    for word in word_list:
        if len(word) >= 5:
            spinned_word_list.append(word[::-1])
        else:
            spinned_word_list.append(word)
    return " ".join(spinned_word_list)