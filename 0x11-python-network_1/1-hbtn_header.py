#!/usr/bin/python3

"""
Script that takes in a URL, sends a request to the URL, \
        and displays the value of the X-Request-Id variable \
        found in the header of the response.
"""

import urllib.request
import sys


if __name__ == "__main__":
    # Retrieve the URL from the command line arguments
    url = sys.argv[1]

    # Create a request object with the specified URL
    req = urllib.request.Request(url)

    with urllib.request.urlopen(req) as response:
        # Retrieve the value of the X-Request-Id \
        #        variable from the response header
        x_request_id = response.getheader('X-Request-Id')

    print(x_request_id)
