#!/usr/bin/python3
"""Takes in a url, sends a request
display the contents of the body
handle errors
"""
import urllib.request
import sys

if __name__ == "__main__":
    req = urllib.request.Request(sys.argv[1])
    try:
        with urllib.request.urlopen(req) as response:
            body = response.read()
            print(body.decode('utf-8'))
    except urllib.error.URLError as e:
        print(f"Error code: {e.code}")
