#!/usr/bin/python3
"""Take in a url and an email, send a post request
and display contents of X-Request-Id
"""
import requests
import sys


if __name__ == '__main__':
    url = sys.argv[1]
    r = requests.get(url)
    print(r.headers['X-Request-Id'])
