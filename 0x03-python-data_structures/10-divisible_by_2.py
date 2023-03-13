#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    i = 0
    while i < len(my_list):
        new_list = []
        for lst in my_list:
            if lst % 2 == 0:
                new_list.append(True)
            else:
                new_list.append(False)
            i += 1
        return new_list
