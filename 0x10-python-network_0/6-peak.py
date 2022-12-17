#!/usr/bin/python3
"""
a function that finds a peak in a list of unsorted integers.
"""

def find_peak(list_of_integers):
    '''
    Finds the peak integer
    '''
    my_list = list_of_integers
    x = len(my_list)
    count = 0
    y = count + 1
    peak = 0
    if x != 0:
        while count < x:
            while y + 1 < x:
                if my_list[count] > my_list[y]:
                    peak = my_list[count]
                else:
                    peak = my_list[y]
                y = y + 1
            count = count + 1
    else:
        return None
    return peak
