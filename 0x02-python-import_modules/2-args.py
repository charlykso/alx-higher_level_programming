#!/usr/bin/python3
from asyncio import Task
import sys


def main():
    if len(sys.argv) == 1:
        print("0 arguments.")
    else:
        print("{} arguments:".format(len(sys.argv) - 1))
        j = 1
        while j < len(sys.argv):
            print("{}: {}".format(j, sys.argv[j]))
            j = j + 1


if __name__ == "__main__":
    main()
