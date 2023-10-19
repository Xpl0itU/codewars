def expanded_form(num):
    result = []
    for i, _ in enumerate(str(num)):
        if str(num)[i] != "0":
            result.append(str(num)[i] + "0" * (len(str(num)) - i - 1))
    return " + ".join(str(x) for x in result)