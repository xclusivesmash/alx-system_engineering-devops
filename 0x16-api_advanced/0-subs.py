#!/usr/bin/python3
"""
Module: 0-subs
Description: Query Reddit API for number of subscribers for a given subreddit
"""
import requests


def number_of_subscribers(subreddit):
    """return number of subscribers for a given subreddit
        return 0 if invalid subreddit given.
    """
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = requests.utils.default_headers()
    headers.update({'User-Agent': 'My User Agent 1.0'})
    rq = requests.get(url, headers=headers).json()
    subscribers = rq.get('data', {}).get('subscribers')
    if subscribers:
        return subscribers
    else:
        return 0
