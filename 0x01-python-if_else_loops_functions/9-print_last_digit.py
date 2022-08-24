#!/usr/bin/python3

def print_last_digit(number):
    x = abs(number)
    if x >= 10:
        last = x % 10
    else:
        last = x
    return last
