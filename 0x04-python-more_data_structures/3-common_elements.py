#!/usr/bin/python3


def common_elements(set_1, set_2):
    unique = []
    for num in set_1:
        if num in set_2:
            unique.append(unique)
    return unique
