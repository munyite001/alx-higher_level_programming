#!/usr/bin/python3


def no_c(my_string):
    result = ''
    for letter in my_string:
        if letter != 'C' and letter != 'c':
            result += letter

    return result
