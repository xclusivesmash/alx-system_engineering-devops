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
    headers = {'User-Agent': "Mozilla/5.0"}
    rs = requests.get(url, headers=headers, allow_redirects=False)
    if rs.status_code == 200:
        data = rs.json()
        subscribers = data['data']['subscribers']
        return subscribers
    else:
        return 0
