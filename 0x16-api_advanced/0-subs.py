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
    headers = {
        "User-Agent": "API/siphamandla"
        }
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code != 200:
        return 0
    sub = response.json().get("data").get("subscribers")
    return sub
