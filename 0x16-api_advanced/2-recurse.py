#!/usr/bin/python3
""" This is a single function module.
"""
import json
import requests


def recurse(subreddit, hot_list=[], next_page=""):
    """This function takes a subreddit as parameter and recursively
    fills the list of titles of hot articles, until the entire subreddit
    has been parsed. This function returns the list of hot articles.
    If no results found, it returns None.
    """
    if subreddit == "":
        return None

    headers = {'User-Agent': 'SoyYo!'}
    url = "https://www.reddit.com/r/" \
        + subreddit \
        + "/hot.json?after=" \
        + next_page
    res = requests.get(url, headers=headers, allow_redirects=False)
    if res.status_code == 200:
        for element in res.json().get('data').get('children'):
            hot_list.append(element.get('data').get('title'))
        next_page = res.json().get('data').get('after')
        if next_page:
            recurse(subreddit, hot_list, next_page)
        return hot_list
    else:
        return None
    return hot_list
