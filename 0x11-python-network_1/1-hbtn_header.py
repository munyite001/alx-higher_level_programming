#!/usr/bin/python3
"""take in a url, send a request and display contents of X-Request-Id"""
import urllib.request
import sys


if __name__ == '__main__':
    req = urllib.request.Request(f"{sys.argv[1]}")
    with urllib.request.urlopen(req) as response:
        print(response.headers['X-Request-Id'])
