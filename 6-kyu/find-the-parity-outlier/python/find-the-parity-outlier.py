def find_outlier(integers):
    return min([x for x in integers if x % 2 != 0], [x for x in integers if x % 2 == 0],key=len)[0]