#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    flag = 0
    for k, v in a_dictionary.items():
        if k == key:
            v = value
            flag = 1
        print("{}: {}".format(k, v))
    if flag == 0:
        a_dictionary[key] = value
        print("{}: {}".format(key, value))
