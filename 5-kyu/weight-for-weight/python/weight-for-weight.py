def order_weight(strng):
    number_list = [int(x) for x in strng.split()]
    number_weight_list = []
    for number in number_list:
        sum_digits = sum([int(x) for x in str(number)])
        number_weight_list.append((number, sum_digits))
    return " ".join([str(x[0]) for x in sorted(number_weight_list, key=lambda x: (x[1], str(x[0])))])