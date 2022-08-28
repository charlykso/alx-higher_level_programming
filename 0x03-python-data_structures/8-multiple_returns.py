#!/usr/bin/python3

def multiple_returns(sentence):
    a = 0
    b = ''
    if sentence == " ":
        b = None
    else:
        a = len(sentence)
        b = sentence[:1]
    return a, b
