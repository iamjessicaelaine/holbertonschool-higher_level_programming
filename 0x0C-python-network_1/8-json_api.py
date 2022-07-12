#!/usr/bin/python3
"""
script that takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter
"""
from sys import argv
import requests

if __name__ == '__main__':
    givenurl = 'http://0.0.0.0:5000/search_user'
    if len(argv) > 1 and type(argv[1]) != int:
        q = argv[1]
    else:
        q = ""
    response = requests.post(givenurl, data={'q': q})
    try:
        result = response.json()
        if result == {}:
            print('No result')
        else:
            print('[{}] {}'.format(result.get('id'), result.get('name')))
    except:
        print('Not a valid JSON')
