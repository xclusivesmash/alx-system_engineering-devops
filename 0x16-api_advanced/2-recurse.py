#!/usr/bin/python3
"""
Description: Query Reddit API recursively for all hot articles
"""
import requests


def recurse(subreddit, hot_list=[], after="tmp"):
    """
        return all hot articles for a given subreddit
        return None if invalid subreddit given
    """
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    headers = {
        "User-Agent": "0x16-api_advanced:project:\
v1.0.0 (by /u/firdaus_cartoon_jr)"
    }
    parameters = {
        "after": after,
        "count": count,
        "limit": 100
    }
    response = requests.get(url, headers=headers, params=parameters,
                            allow_redirects=False)
    if response.status_code == 404:
        return None
    results = response.json().get("data")
    after = results.get("after")
    count = count + results.get("dist")
    for m in results.get("children"):
        hot_list.append(m.get("data").get("title"))
    if after is not None:
        return recurse(subreddit, hot_list, after, count)
    return hot_list
