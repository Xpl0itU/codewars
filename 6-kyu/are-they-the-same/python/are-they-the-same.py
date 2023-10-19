def comp(array1, array2):
    if array1 is None or array2 is None:
        return False
    if len(array1) != len(array2):
        return False
    if sorted([multiplicity ** 2 for multiplicity in array1]) != sorted(array2):
        return False
    return True