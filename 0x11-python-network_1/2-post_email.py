#!/usr/bin/python3
"""
Python script that takes in a URL and an email,
sends a POST request to the passed URL
with the email as a parameter,
and displays the body of the response (decoded in utf-8)
"""
from urllib import request, parse
import sys

if __name__ == '__main__':
    url = sys.argv[1]
    values = {'email': sys.argv[2]}

    new_values = parse.urlencode(values).encode('utf-8')
    req = request.Request(url, new_values)

    with request.urlopen(req) as response:
        the_page = response.read().decode('utf-8')
        print(the_page)
