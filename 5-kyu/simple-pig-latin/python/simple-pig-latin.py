from string import punctuation

def pig_it(text):
    final_words = []
    for word in text.split():
        if word in punctuation:
            final_words.append(word)
            continue
        final_words.append(f"{word[1:]}{word[0]}ay")
    return " ".join(final_words)