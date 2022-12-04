#!/usr/bin/python3


def delete_at(my_list=[], idx=0):
    if idx < 0 or idx >= len(my_list):
        return my_list
    else:
        new_list = []
        for num in my_list:
            if num != my_list[idx]:
                new_list.append(num)
    return new_list
