#!/usr/bin/python3
"""Send a post request to an email"""
import requests
import sys

if __name__ == "__main__":
    values = {'email': sys.argv[2]}
    r = requests.post(sys.argv[1], data=values)
    print(r.text)
