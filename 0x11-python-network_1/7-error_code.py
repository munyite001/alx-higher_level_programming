#!/usr/bin/python3
"""Send a request to an email
display body of the response
handle errors
"""
import requests
import sys

if __name__ == "__main__":
    try:
        r = requests.get(sys.argv[1])
        print(r.text)
    except requests.exceptions.HTTPError as e:
        print(f"Error code: {e.response.status_code}")
