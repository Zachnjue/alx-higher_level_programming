#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    """
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print(matrix[i][j], end=' ')
            # print("{:d}".format(matrix[i][j]), end='')
        print()
    """
    for row in matrix:
       # print(row)
        for column in row:
            #    print(column)
            if column == row[-1]:
                print('{:d}'.format(column), end='')
            else:
                print('{:d}'.format(column), end=' ')
        print()
