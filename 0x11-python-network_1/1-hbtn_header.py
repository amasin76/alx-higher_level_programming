#!/usr/bin/python3
"""
displays the value of the X-Request-Id variable found in
the header of the response
"""


if __name__ == "__main__":
    from urllib.request import urlopen
    from sys import argv

    with urlopen(argv[1]) as response:
        head = response.headers.get("X-Request-Id")
        print(head)
