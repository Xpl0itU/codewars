def find_it(seq):
    occurrences = [seq.count(num) for num in seq]
    odd_occurrence = 0
    for occurrence in occurrences:
        if occurrence % 2 != 0:
            odd_occurrence = occurrence
            break
    return seq[occurrences.index(odd_occurrence)]
