import os

def fib(num):
    if num == 0:
        return 0
    
    elif num == 1:
        return 1
    
    else:
        result = fib(num - 1) + fib(num - 2)
        return result

numFibValues = int(input("How mnay Fibonacci values: "))
i = 1
while i < numFibValues:
    fibValue = fib(i)
    print(fibValue)
    i += 1
