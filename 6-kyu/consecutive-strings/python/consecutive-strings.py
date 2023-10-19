def longest_consec(strarr, k):
    if k > len(strarr):
        return ""
    if k == 1:
        return max(strarr, key=len)
    longest_string = ""
    for i, _ in enumerate(strarr):
        current_string = ""
        for j in range(i, i + k):
            if j >= len(strarr):
                break
            current_string += strarr[j]
        if len(current_string) > len(longest_string):
            longest_string = current_string

    return longest_string