def descending_order(num):
    return int(''.join(sorted([i for i in str(num)], reverse=True)))