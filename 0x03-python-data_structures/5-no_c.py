#!/usr/bin/env python3
def no_c(my_string):
    indx = my_string.find('C')
    index_1 = my_string.find('c')
    result_str = ""
    for i in range(0, len(my_string)):
        if i != indx and i != index_1:
            result_str = result_str + my_string[i]
    return result_str
