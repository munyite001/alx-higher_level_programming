#!/usr/bin/python3

"""Retrieve an element from a given index in an array

    Args:
        my_list: array
        idx: index

    Returns:
        prints the element at given index
"""


def element_at(my_list, idx):
    if idx < 0 or idx >= len(my_list):
        return "None"
    else:
        print("Element at index {:d} is {}".format(idx, my_list[idx]))
