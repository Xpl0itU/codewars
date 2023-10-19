def solution(s):
    final_list = []
    len_s = len(s)
    is_odd = len_s % 2 != 0
    for i in range(0, len_s, 2):
        if is_odd and i == len_s - 1:
            final_list.append(f"{s[i]}_")
            break
        final_list.append(f"{s[i]}{s[i + 1]}")
    return final_list