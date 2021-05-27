#!/usr/bin/python3
""" This is a single function module.
"""
import json
import requests


def recurse(subreddit, hot_list=[]):
    """This function takes a subreddit as parameter and recursively
    fills the list of titles of hot articles, until the entire subreddit
    has been parsed. This function returns the list of hot articles.
    If no results found, it returns None.
    """
    if subreddit == "":
        return None

    head = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64)'}
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    if not hot_list:
        par = {'limit': 100}
    else:
        par = {'limit': 100, 'after': hot_list[-1][1]}
    r = requests.get(url, headers=head, params=par)
    res = r.json()
    if res.get('data').get('children'):
        print('theres a post')
        print()
        for post in res['data']['children']:
            post_list = []
            post_list.append(post['data']['title'])
            # print('title: ' + post['data']['title'])
            fullname = post['kind'] + '_' + post['data']['id']
            post_list.append(fullname)
            hot_list.append(post_list)
        recurse(subreddit, hot_list)
    else:
        print('else')
        if hot_list:
            print('recursion happened')
            titles = []
            for post in hot_list:
                titles.append(post[0])
            hot_list = titles
            return hot_list
        else:
            print('fail')
            return None
