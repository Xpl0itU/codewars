def count_sheeps(sheep):
    present_sheep = 0
    for item in sheep:
        if item:
            present_sheep += 1
    return present_sheep