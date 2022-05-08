#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    lastdig = number % -10
else:
    lastdig = number % 10
print("The last digit of {} is {} ".format(number, lastdig), end='')
if lastdig > 5:
    print('and is greater than 5')
if lastdig == 0:
    print('and is 0')
if lastdig < 6 and lastdig != 0:
    print("and is less than 6 and not 0")
