#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    div_by_2 = []
    for elt in my_list:
        if (elt % 2) == 0:
            div_by_2.append(True)
        else:
            div_by_2.append(False)
    return div_by_2
