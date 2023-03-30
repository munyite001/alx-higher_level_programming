#!/usr/bin/python3
"""Find the biggest number in a list
"""
def find_peak(list_of_integers):
    biggest = 0
    for num in list_of_integers:
        if num > biggest:
            biggest = num
    return biggest
