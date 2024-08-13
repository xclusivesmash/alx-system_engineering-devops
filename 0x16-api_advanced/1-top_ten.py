#!/usr/bin/python3
"""
Module: 1-top_ten
Description: Query Reddit API for titles of top ten posts of a given subreddit
"""
import requests


def top_ten(subreddit):
    """return top ten titles for a given subreddit
        return None if invalid subreddit given
    """
    user = {'User-Agent': 'Lizzie'}
    url = requests.get('https://www.reddit.com/r/{}/hot/.json?limit=10'
                       .format(subreddit), headers=user).json()
    # implement the try-catch method.
    try:
        for post in url.get('data').get('children'):
            print(post.get('data').get('title'))
    except Exception:
        print(None)


if __name__ == "__main__":
    top_ten(argv[1])
