def move_zeros(lst):
    num_zeros = lst.count(0)
    while 0 in lst:
        lst.remove(0)
    for i in range(num_zeros):
        lst.append(0)
    return lst