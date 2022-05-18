#!/usr/bin/python3
def search_replace(my_list, search, replace):
    # make copy of og list into newlist as placeholder
    newlist = my_list.copy()
    # iterate through lists to search & replace
    for elem in range(len(my_list)):
        if my_list[elem] == search:
            newlist[elem] = replace
    return newlist
