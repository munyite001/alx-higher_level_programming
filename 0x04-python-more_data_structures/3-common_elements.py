#!/usr/bin/python3


def common_elements(set_1, set_2):
    unique = []
    for elem in set_1:
        if elem in set_2:
            unique.append(elem)
    return unique
