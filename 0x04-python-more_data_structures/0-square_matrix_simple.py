#!/usr/bin/python3
# if __name__ == '__main__':
def square_matrix_simple(matrix=[]):
    return [list(map(lambda x: x ** 2, row)) for row in matrix]
