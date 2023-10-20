def multiplication_table(size):
    final_list = []
    for i in range(1, size + 1):
        final_list.append([j * i for j in range(1, size + 1)])
    return final_list