def order(sentence):
    sentence_list = sentence.split()
    ordered_words = []
    for i in range(1, len(sentence_list) + 1):
        for word in sentence_list:
            if str(i) in word:
                ordered_words.append(word)
                break
    return " ".join(ordered_words)
