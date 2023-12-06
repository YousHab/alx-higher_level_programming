#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    flag = 0
    for k, v in a_dictionary.items():
        if k == key:
            v = value
            flag = 1
    if flag == 0:
        a_dictionary[key] = value
