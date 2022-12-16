#!/bin/bash
# Bash script that takes in a URL, sends a request to that URL, 
# and displays the size of the body of the response.
# usage: ./0-body_size.sh 0.0.0.0:5000

curl -sI "$1" | grep Content-Length: | cut -d' ' -f2
