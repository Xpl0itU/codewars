CENT_VALUES = sorted({
    "Nickels": 5,
    "Pennies": 1,
    "Dimes": 10,
    "Quarters": 25,
}.items(), key=lambda x: x[1], reverse=True)

def loose_change(cents):
    change_dict = {
        "Nickels": 0,
        "Pennies": 0,
        "Dimes": 0,
        "Quarters": 0,
    }
    for coin, value in CENT_VALUES:
        while cents >= value:
            cents -= value
            change_dict[coin] += 1
    return change_dict