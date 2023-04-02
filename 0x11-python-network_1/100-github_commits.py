#!/usr/bin/python3
"""List 10 commits of a given repo
by a given user
"""
import requests
import sys


if __name__ == "__main__":
    url = f"https://api.github.com/repos/{sys.argv[2]}/{sys.argv[1]}/commits"
    r = requests.get(url)

    response = r.json()
    try:
        for i in range(10):
            print("{}: {}".format(
                response[i].get('sha'),
                response[i].get('commit').get('author').get('name')
            ))
    except IndexError:
        pass
