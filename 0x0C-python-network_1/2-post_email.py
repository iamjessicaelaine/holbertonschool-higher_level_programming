#!/usr/bin/python3
"""
script sends a post request to given url and email & displays decoded
body of the response
"""
from urllib.request import urlopen, Request
from urllib.parse import urlencode
from sys import argv


if __name__ == '__main__':
    url = argv[1]
    email = argv[2]
    datadict = {'email': email}
    encodeddata = urlencode(datadict)
    utf8data = encodeddata.encode("utf-8")

    with urlopen(url, data=utf8data) as response:
        body = response.read()
        print(response.body.decode("utf-8"))
