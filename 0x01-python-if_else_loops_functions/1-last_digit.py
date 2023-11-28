#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
n = abs(number) % 10
if n < 6:
    str = "and is less then 6 and not 0"
elif n == 0:
    str = "and is a 0"
else:
    str = "and is greater then 6 and not 0"
print(f"Last digit of {number} is {n} " + str)
