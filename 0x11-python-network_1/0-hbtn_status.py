#!/usr/bin/python3
"""Fetch a url using urllib and display the response"""
import urllib.request


if __name__ == '__main__':
    req = urllib.request.Request("https://alx-intranet.hbtn.io/status")
    with urllib.request.urlopen(req) as response:
        page = response.read()
        print("Body response:")
        print(f"\t- type: {type(page)}")
        print(f"\t- content: {page}")
        print(f"\t- utf8 content: {page.decode('utf-8')}")
