#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    count = len(sys.argv) - 1

    if count == 0:
        print("0 arguments.")
    elif count == 1:
        print("1 argument:\n1: {:s}".format(sys.argv[1]))
    else:
        print("{:d} arguments: ".format(count))
        for i in range(1, count):
            print("{:d}: {:s}".format(i, sys.argv[i]))