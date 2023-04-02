#!/usr/bin/python3
"""Fetch a url using urllib and display the response
"""
if __name__ == '__main__':
    import urllib.request
    with urllib.request.urlopen("https://alx-intranet.hbtn.io/status") as response:
        page = response.read()
        print("Body response:")
        print(f"\t -type: {type(page)}")
        print(f"\t -content: {page}")
        print(f"\t -utf8 content: {page.decode('utf-8')}")

