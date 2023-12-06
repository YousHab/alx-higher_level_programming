#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    sorted_dic = sorted(a_dictionary.items())
    for elt in sorted_dic:
        value = a_dictionary[elt]
        print("{} : {}".format(elt, value))
