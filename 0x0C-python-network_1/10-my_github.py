#!/usr/bin/python3
"""script taskes github credentials and displays id using github api"""
from sys import argv
import requests


if __name__ == '__main__':
    username = argv[1]
    pat = argv[2]
    githubapi = 'https://api.github.com/user'
    response = requests.get(githubapi, auth=(username, pat))
    if response.status_code > 400:
        print('None')
    else:
        jformatbody = response.json()
        print(jformatbody['id'])
