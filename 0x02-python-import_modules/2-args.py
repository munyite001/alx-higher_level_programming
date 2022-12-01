#!/usr/bin/python3

if __name__ == "__main__":
    import sys

    n = len(sys.argv)
    if n > 2 or n == 1:
        print("{:d} arguments".format(n-1))
    else:
        print("{:d} argument".format(n-1))
    for i in range(1,n):
        print("{:d}: {:s}".format(i, sys.argv[i]))
