#!/bin/bash
# Bash script that sends a request to a URL passed as an argument
# Displays only the status code of the response
curl -sI -w '%{response_code}' "$1" -o /dev/null
