#!/usr/bin/python3
"""List 10 commits of a given repo
by a given user
"""
import requests
import sys


if __name__ == "__main__":
    repo = sys.argv[1]
    user = sys.argv[2]
    url = f"https://api.github.com/repos/{user}/{repo}/commits"
    r = requests.get(url)

    response = r.json()
    if response == {}:
        print("None")
    else:
        for i in range(10):
            author = response[i].get('author').get('login')
            sha = response[i].get('sha')
            print(f"{sha}: {author}")
