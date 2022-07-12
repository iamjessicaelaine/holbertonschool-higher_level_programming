#!/usr/bin/python3
"""script manages HTTPerror, requests from a url t0 display body of response"""
from urllib.request import urlopen
from urllib.error import HTTPError
from sys import argv


if __name__ == '__main__':
    givenurl = argv[1]
    try:
        with urlopen(givenurl) as response:
            body = response.read()
            decodedbody = body.decode("utf-8")
            print(decodedbody)
    except HTTPError as error:
        print("Error code: {}".format(error.code))
