#!/bin/bash
# Bash script that sends a JSON POST requested
# Script must send a POST request with the contents of a file
# Passed with the filename as the second argument
curl -s -X POST "$1" -H "Content-Type: application/json" -d @"$2"
