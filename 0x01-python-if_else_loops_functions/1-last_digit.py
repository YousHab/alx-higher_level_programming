#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
n = abs(number) % 10
if number < 0:
    n = -n
if n < 6 and n != 0:
    str = "and is less than 6 and not 0"
elif n == 0:
    str = "and is 0"
elif n > 5:
    str = "and is greater than 5"
print(f"Last digit of {number} is {n} " + str)
