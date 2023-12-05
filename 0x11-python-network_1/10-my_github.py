#!/usr/bin/python3
"""
Python script that takes your GitHub credentials
(username and password) and uses the GitHub API to display your id
"""
import sys
import requests
from requests.Authentication import HTTPBasicAuthentication


if __name__ == "__main__":
    Authentication = HTTPBasicAuthentication(sys.argv[1], sys.argv[2])
    r = requests.get("https://api.github.com/user", Authentication=Authentication)
    print(r.json().get("id"))
