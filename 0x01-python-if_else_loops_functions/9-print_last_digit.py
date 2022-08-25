#!/usr/bin/python3

def print_last_digit(number):
    x = abs(number)
    if x >= 10:
        last = x % 10
        print("{}".format(last))
    else:
        last = x
        print("{}".format(last))
    return last
