#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    n = len(argv) - 1
    print("{} arguments".format(n), end="")
    if n == 0:
        print(".")
    else:
        print(":")
        for i in range(1, n + 1):
            print("{}: {}".format(i, argv[i]))
