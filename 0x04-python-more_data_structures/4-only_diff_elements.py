#!/usr/bin/python3


def only_diff_elements(set_1, set_2):
    unique = []
    for elem in set_1:
        if elem not in set_2:
            unique.append(elem)
    for elem in set_2:
        if elem not in set_1:
            unique.append(elem)
    return unique
