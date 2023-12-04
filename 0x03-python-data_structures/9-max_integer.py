#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return "None"
    maxi = my_list[0]
    for elt in my_list:
        if elt > maxi:
            maxi = elt
    return maxi
