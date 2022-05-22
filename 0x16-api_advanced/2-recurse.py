#!/usr/bin/python3
"""Function to query a list of all hot posts on a given Reddit subreddit."""
import requests


def recurse(subreddit, hot_list=[], after="", count=0):
    """Returns a list of titles of all hot posts on a given subreddit."""
    # Payload for the GET request
    url = f'https://www.reddit.com/r/{subreddit}/hot/.json'
    headers = {'user-Agent': 'Noobdevsayswhat'}
    params = {
        "after": after,
        "count": count,
        "limit": 100
    }

    # Request placeholder
    res = requests.get(url, headers=headers, params=params)
    
    # Restrain for unexistant subs
    if res.status_code > 299 and res.status_code < 500:
        return None

    results = res.json().get("data")
    after = results.get("after")
    count += results.get("dist")
    for post in results.get("children"):
        hot_list.append(post.get("data").get("title"))

    if after is not None:
        return recurse(subreddit, hot_list, after, count)
    return hot_list
    