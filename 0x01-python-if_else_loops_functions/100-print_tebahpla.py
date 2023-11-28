#!/usr/bin/python3
for elt in range(ord('z'), ord('a') - 1, -1):
    print("{}".format(chr(elt - n)), end="")
    n = 32 if n == 0 else 0
