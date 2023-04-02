#!/usr/bin/python3
"""Take in a url, send a request and display contents of X-Request-Id"""
import urllib.request
import sys


if __name__ == '__main__':
    req = urllib.request.Request(sys.argv[1])
    with urllib.request.urlopen(req) as response:
        print(dict(response.headers).get('X-Request-Id'))
