#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
print("Last digit of {:d} is ".format(number), end='')
num_str = repr(number)
negornah = num_str[0]
lastdig_str = num_str[-1]
lastdig = int(lastdig_str)
if negornah == '-':
    print("-{} and is less than 6 and not 0".format(lastdig_str))
else:
    print("{} ".format(lastdig), end='')
    if lastdig > 5:
        print("and is greater than 5")
    if((lastdig < 6) and (lastdig != 0)):
        print("and is less than 6 and not 0")
    if lastdig == 0:
        print("and is 0")
