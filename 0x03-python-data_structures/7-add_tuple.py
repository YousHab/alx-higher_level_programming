#!/usr/bin/python3
def size_check(tuple_a=()):
    len_a = len(tuple_a)
    if len_a == 0:
        tuple_a = (0, 0)
    if len_a == 1:
        tuple_a = (tuple_a[0], 0)
    if len_a > 2:
        tuple_a = (tuple_a[0], tuple_a[1])
    return tuple_a


def add_tuple(tuple_a=(), tuple_b=()):
    result = ()
    tuple_a = size_check(tuple_a)
    tuple_b = size_check(tuple_b)
    result = (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])
