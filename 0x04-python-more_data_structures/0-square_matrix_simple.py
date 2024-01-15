#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    for num in (matrix):
           new_matrix.append([x*x for x in num])
    return new_matrix
