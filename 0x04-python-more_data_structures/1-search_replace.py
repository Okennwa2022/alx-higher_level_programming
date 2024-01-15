#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = []
    for num in range(len(my_list)):
        new_list.append(my_list[num])
        if my_list[num] == search:
            newlist[num] = replace
    return new_list
