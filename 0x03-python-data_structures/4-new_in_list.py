#!/usr/bin/python3

"""Replace an element from a given index in an array

    Args:
        my_list: array
        idx: index
        element: the element to be placed at the specified index

    Returns:
        the modified list
"""


def new_in_list(my_list, idx, element):

    new_list = my_list[:]
    if idx < 0 or idx >= len(my_list):
        return new_list
    else:
        new_list[idx] = element
        return new_list
