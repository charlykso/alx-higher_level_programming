#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    x = []
    j = 0
    lent = len(my_list)
    while j < lent:
        if my_list[j] % 2 == 0:
            x.append(True)
            j = j + 1
        else:
            x.append(False)
            j = j + 1
    return x
            