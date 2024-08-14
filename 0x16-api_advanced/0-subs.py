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
    if subreddit is None or not isinstance(subreddit, str):
        return 0
    user_agent = {'User-agent': 'Google Chrome Version 81.0.4044.129'}
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    response = get(url, headers=user_agent)
    results = response.json()
    try:
        return results.get('data').get('subscribers')
    except Exception:
        return 0
