ALPHABET = "abcdefghijklmnopqrstuvwxyz"

def alphabet_position(text):
    positions = []
    for char in text:
        if char.lower() in ALPHABET:
            positions.append(str(ALPHABET.index(char.lower()) + 1))
    return " ".join(positions)