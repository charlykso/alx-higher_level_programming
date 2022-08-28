#!/usr/bin/python3

def max_integer(my_list=[]):
    x = len(my_list) - 1
    i = 0
    if len(my_list) == 0:
        return None
    else:
        while i < x:
            if my_list[i] > my_list[x]:
                big = my_list[i]
                x = x -1
            elif my_list[x] > my_list[i]:
                big = my_list[x]
                i = i + 1
            else:
                big = my_list[x]
                i = i + 1
        return big
