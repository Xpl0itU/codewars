# taken from https://stackoverflow.com/a/9368616
def next_bigger(n):
    num_str = str(n)
    num_list = list(num_str)

    if all(i == num_list[0] for i in num_list):
        return -1

    for i in range(len(num_list) - 2, -1, -1):
        if num_list[i] < num_list[i + 1]:
            break

    for j in range(len(num_list) - 1, i, -1):
        if num_list[j] > num_list[i]:
            break

    num_list[i], num_list[j] = num_list[j], num_list[i]

    num_list[i + 1:] = reversed(num_list[i + 1:])

    result = int("".join(num_list))
    if result > n:
        return result
    return -1