#!/usr/bin/python3
def uppercase(str):
    for letter in str:
        car = ord(letter)
        if (car >= 97 and car <= 122):
            car = car - 32
        print("{:c}".format(car), end='')
    print("{}".format(''))
