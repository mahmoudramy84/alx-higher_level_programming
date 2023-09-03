#!/usr/bin/python3
"""Lists the 10 most recent commits on a given GitHub repository"""

from sys import argv
from requests import get

if __name__ == "__main__":
    url = f'https://api.github.com/repos/{argv[2]}/{argv[1]}/commits'

    res = get(url)
    commits = res.json()
    try:
        for i in range(10):
            print('{}: {}'.format(
                commits[i].get('sha'),
                commits[i].get('commit').get('author').get('name')))
    except IndexError:
        pass
