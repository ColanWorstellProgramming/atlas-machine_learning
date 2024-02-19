#!/usr/bin/env python3
"""
Imports
"""


if __name__ == '__main__':
    """
    User Locations
    """
    import sys
    import requests
    import time

    response = requests.get(sys.argv[1])

    if response.status_code == 200:
        print(response.json()['location'])
    elif response.status_code == 404:
        print("Not found")
    elif response.status_code == 403:
        time = (int(response.headers['X-RateLimit-Reset']) - int(time.time()))
        print("Reset in {} min".format(time//60))