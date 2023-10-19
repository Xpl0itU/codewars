def unique_in_order(sequence):
    final = []
    for item in sequence:
        if len(final) == 0:
            final.append(item)
            continue
        if final[-1] == item:
            continue
        final.append(item)
    return final