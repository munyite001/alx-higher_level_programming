#!/usr/bin/python3
"""Take in a url and an email, send a post request
and display contents of X-Request-Id
"""
import urllib.parse
import urllib.request
import sys


if __name__ == '__main__':
    values = {'email': sys.argv[2]}
    data = urllib.parse.urlencode(values).encode('ascii')
    req = urllib.request.Request(sys.argv[1], data)
    with urllib.request.urlopen(req) as response:
        print(response.read().decode('utf-8'))
