#!/usr/bin/python3

import sys
import requests

if __name__ == '__main__':
    repo_name = sys.argv[1]
    owner_name = sys.argv[2]
    password = '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'
    url = \
        'https://api.github.com/repos/{}/{}/commits'.format(owner_name, repo_name)
    headers = {'Authorization': 'token {}'.format(password)}
    res = requests.get(url, headers=headers)
    # print(res.json())
    response = res.json()
    for item in response:
        print('{} {}'.format(item.tree.sha, item.author.name))
