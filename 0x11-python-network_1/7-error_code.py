#!/usr/bin/python3
"""
HTTP status code is greater than or equal to 400
print: Error code: followed by the value of the HTTP status code
use the packages requests and sys
"""
import sys
import requests


if __name__ == "__main__":
    url = sys.argv[1]
    m = requests.get(url)
    if m.status_code >= 400:
        print("Error code: {}".format(m.status_code))
    else:
        print(m.text)
