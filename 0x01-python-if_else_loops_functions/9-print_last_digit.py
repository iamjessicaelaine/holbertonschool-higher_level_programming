#!/usr/bin/python3
def print_last_digit(number):
    if number < 0:
        lastnum = abs(number % -10)
    else:
        lastnum = number % 10
    print(lastnum, end='')
    return(lastnum)
