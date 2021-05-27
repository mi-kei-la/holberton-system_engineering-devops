#!/usr/bin/python3
""" This is a single function module.
"""
import json
import requests


def top_ten(subreddit):
    """ This function takes the name of a subreddit as parameter
    and prints the name of the first 10 hot posts. If no subreddit,
    print None.
    """
    if subreddit == "":
        print('None')
        return
    else:
        head = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64)'}
        url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
        par = {'limit': 10}
        r = requests.get(url, headers=head, params=par)
        if r.status_code == 404:
            print('None')
            return
        res = r.json()
        # count = 0
        if res.get('data').get('children'):
            for child in res['data']['children']:
                # if count == 10:
                #     break
                print(child.get('data').get('title'))
                # count += 1
