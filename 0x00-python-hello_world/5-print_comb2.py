#!/usr/bin/python3
for j in range(0, 100):
    if j <= 98:
        print("{0:02d}".format(j), end=', ')
    if j == 99:
        print("{0:02}".format(j))
