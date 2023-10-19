ALPHABET = "abcdefghijklmnopqrstuvwxyz"

def calculate_word_score(word):
    score = 0
    for i, letter in enumerate(ALPHABET):
        if letter in word:
            score += word.count(letter) * (i + 1)
    return score

def high(x):
    scores = {}
    words = x.split()
    for word in words:
        if scores:
            max_score = max(scores.values())
            word_score = calculate_word_score(word)
            if word_score > max_score:
                scores[word] = word_score
        else:
            scores[word] = calculate_word_score(word)
    return max(scores, key=scores.get)