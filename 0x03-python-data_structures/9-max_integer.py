#!/usr/bin/python3


def max_integer(my_list=[]):
    if my_list:
        biggest = my_list[0]
        for num in my_list:
            if biggest < num:
                biggest = num
    else:
        return None:
    return biggest
