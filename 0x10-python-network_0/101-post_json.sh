#!/bin/bash
# Bash script that sends a JSON POST requested of the file.
curl -s -X POST "$1" -H "Content-Type: application/json" -d @"$2"
