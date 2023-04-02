#!/usr/bin/python3
"""fetch https://alx-intranet.hbtn.io/status
diplay contents of the body
"""
import requests
if __name__ == "__main__":
    r = requests.get('https://alx-intranet.hbtn.io/status')
    print("Body response:")
    print(f"\t- type: {type(r)}")
    print(f"\t- content: {r.content}")
