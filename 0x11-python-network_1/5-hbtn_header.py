#!/usr/bin/python3
"""Take in a url, send a request
and display contents of X-Request-Id
"""
import requests
import sys

if __name__ == '__main__':
    r = requests.get(sys.argv[1])
    print(dict(r.headers).get('X-Request-Id'))
