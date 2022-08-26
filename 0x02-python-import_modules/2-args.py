#!/usr/bin/python3

import sys
if len(sys.argv) == 1:
    print(".")
else:
    print("{} arguments:".format(len(sys.argv) - 1))
    j = 1
    while j < len(sys.argv):
        print("{}: {}".format(j, sys.argv[j]))
        j = j + 1
