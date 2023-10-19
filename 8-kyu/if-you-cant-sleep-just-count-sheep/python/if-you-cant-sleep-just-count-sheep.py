def count_sheep(n):
    final_string = ""
    for i in range(1, n + 1):
        final_string += f"{i} sheep..."
    return final_string