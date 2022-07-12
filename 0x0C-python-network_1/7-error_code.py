#!/usr/bin/python3
"""script requests of givenurl & outputs body of response w/ errorhandling"""
from sys import argv
import requests


if __name__ == '__main__':
    givenurl = argv[1]
    response = requests.get(givenurl)
    status = response.status_code
    if status >= 400:
        print('Error code: {}'.format(status))
    else:
        print(response.text)
