#!/usr/bin/python3
'''Takes in a letter and sends a POST requestr to
http://0.0.0.0:5000/search_user'''

import sys
import requests

if __name__ == '__main__':
    letter = "" if len(sys.argv) == 1 else sys.argv[1]
    data = {'q': letter}
    try:
        with requests.post('http://0.0.0.0:5000/search_user', data) as req:
            response = req.json()
            if response == {}:
                print('No result')
            else:
                print(f'[{response.get("id")}] {response.get("name")}')
    except ValueError:
        print('Not a valid JSON')
