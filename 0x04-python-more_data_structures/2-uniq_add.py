#!/usr/bin/python3


def uniq_add(my_list=[]):
    unique_total = 0
    for num in set(my_list):
        unique_total += num
    return unique_total
