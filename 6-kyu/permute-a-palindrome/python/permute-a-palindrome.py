def permute_a_palindrome(input): 
    odd_occurrences = 0
    for char in set(input):
        char_occurrence_count = input.count(char)
        if char_occurrence_count % 2 != 0:
            odd_occurrences += 1
    return odd_occurrences < 2