def xo(s):
    x_count = 0
    o_count = 0
    for char in s:
        if char in ["x", "X"]:
            x_count += 1
        elif char in ["o", "O"]:
            o_count += 1
    return x_count == o_count