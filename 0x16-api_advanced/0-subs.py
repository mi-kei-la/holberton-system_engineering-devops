#!/usr/bin/python3
""" This module contains a single function which takes a subreddit
as parameter, and returns the number of subscribers it has.
"""
import json
import requests


def number_of_subscribers(subreddit):
    """This function returns the number of subscribers of a given
    subreddit, 0 otherwise."""
    if subreddit == "":
        return 0

    head = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64)'}
    r = requests.get('https://www.reddit.com/r/{}/about.json'
                     .format(subreddit), headers=head)
    if r.status_code == 404:
        return 0
    else:
        res = r.json()
        if res.get('data'):
            return r.json().get('data').get('subscribers')
        else:
            return 0
