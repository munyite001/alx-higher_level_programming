#!/usr/bin/python3
"""send a post request with a letter
"""
import requests
import sys

if __name__ == "__main__":
    url = 'https://api.github.com/user'
    username = sys.argv[1]
    password = sys.argv[2]

    r = requests.get(url, auth=(username, password))

    res = r.json()
    if res == {}:
        print("None")
    else:
        print(f"{res.get('id')}")
