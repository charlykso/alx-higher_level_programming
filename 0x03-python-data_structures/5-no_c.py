#!/usr/bin/python3

from operator import ixor


def no_c(my_string):
    for i in "cC":
        my_string = my_string.replace(i, "")
    return my_string
