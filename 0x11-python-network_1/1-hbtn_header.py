#!/usr/bin/python3
"""
takes in a URL, sends a request to the URL and displays 
the value of the X-Request-Id variable found in the header of the response.
"""

from urllib.request import Request, urlopen
from sys import argv

if __name__ == "__main__":
    url = argv[1]
    request = Request(url)
    with urlopen(request) as responce:
        head = (dict(responce.headers).get("X-Request-Id"))
        print (head)
