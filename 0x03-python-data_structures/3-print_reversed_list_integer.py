#!/usr/bin/python3

""" Print a list of integers in reverse
    
    Args:
        my_list: The array with the list of integers
    
    Returns:
        prints the integers
"""

def print_reversed_list_integer(my_list=[]):
    for number in range(len(my_list), 0, -1):
        print("{:d}".format(number))
