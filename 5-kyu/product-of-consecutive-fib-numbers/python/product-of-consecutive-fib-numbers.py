def fib(n):
    a = 0
    b = 1
    if n == 1:
        return a
    if n == 2:
        return b
    for i in range(3,n + 1):
        c = a + b
        a = b
        b = c
    return b

def productFib(prod):
    i = 0
    current_number = 0
    last_number = 0
    while True:
        last_number = current_number
        current_number = fib(i)
        if current_number * last_number == prod:
            return [last_number, current_number, True]
        if current_number * last_number >= prod:
            return [last_number, current_number, False]
        i += 1
