#!/usr/bin/python3


def print_matrix_integer(matrix=[[]]):

    if matrix:
        for list in matrix:
            for number in list:
                if number == list[-1]:
                    print("{:d}".format(number), end='')
                else:
                    print("{:d}".format(number), end=' ')
            print()
