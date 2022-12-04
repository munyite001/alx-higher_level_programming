#!/usr/bin/python3

"""Replace an element from a given index in an array

    Args:
        my_list: array
        idx: index
        element: the element to be placed at the specified index

    Returns:
        the modified list
"""


def replace_in_list(my_list, idx, element):
    if idx < 0 or idx >= len(my_list):
        return my_list
    else:
        my_list[idx] = element
        return my_list
