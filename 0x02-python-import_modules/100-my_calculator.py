#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    from calculator1 import add, sub, mul, div
    operators = "+-*/"
    n = len(argv) - 1
    if n != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    flag == 0
    for op in operators:
        if op == argv[2]:
            flag = 1
    if flag == 0:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    else:
        a = int(argv[1])
        b = int(argv[3])
        sum_res = add(a, b)
        sub_res = sub(a, b)
        mul_res = mul(a, b)
        div_res = div(a, b)
        if argv[2] == "+":
            print("{} + {} = {}".format(a, b, sum_res))
        elif argv[2] == "-":
            print("{} + {} = {}".format(a, b, sub_res))
        elif argv[2] == "*":
            print("{} + {} = {}".format(a, b, mul_res))
        elif argv[2] == "/":
            print("{} + {} = {}".format(a, b, div_res))
