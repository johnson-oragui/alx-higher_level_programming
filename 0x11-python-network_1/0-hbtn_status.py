#!/usr/bin/python3

"""
Script that fetches https://alx-intranet.hbtn.io/status
"""

import urllib.request

if __name__ == "__main__":
    # URL to fetch
    url = "https://alx-intranet.hbtn.io/status"

    # Create a request object with the specified URL
    req = urllib.request.Request(url)

    with urllib.request.urlopen(req) as response:
        # Read the response body
        body = response.read()

        # Decode the body content from bytes to UTF-8
        utf8_content = body.decode('utf-8')

    # Print the body response in the specified format
    print("Body response:")
    print("\t- type: {}".format(type(body)))
    print("\t- content: {}".format(body))
    print("\t- utf8 content: {}".format(utf8_content))
