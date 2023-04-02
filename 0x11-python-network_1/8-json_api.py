#!/usr/bin/python3
"""send a post request with a letter
"""
import requests
import sys

if __name__ == "__main__":
    url = 'http://0.0.0.0:5000/search_user'
    if len(sys.argv) == 2:
        q = sys.argv[1]
    else:
        q = ''
    values = {'q': q}

    r = requests.post(url, data=values)

    try:
        res = r.json()
        if res == {}:
            print("No result")
        else:
            print(f"[{res.get('id')}] {res.get('name')}")
    except ValueError:
        print("Not a valid JSON")
