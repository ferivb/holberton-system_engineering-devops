#!/usr/bin/python3
"""Funtion that queries the Reddit API and returns
    the number of subscribers (not active users, total subscribers)
    for a given subreddit. If an invalid subreddit is given,
    the function should return 0."""
import requests


def number_of_subscribers(subreddit):
    """Returns the number of subscribers or 0 if
        invalid subreddit"""

    # Payload for the GET request
    url = f'https://www.reddit.com/r/{subreddit}/about.json'
    headers = {'user-Agent': 'Noobdevsayswhat'}

    # Request placeholder
    res = requests.get(url, headers=headers)

    # Restrain for unexistant subs
    if res.status_code > 299 and res.status_code < 500:
        return 0

    # Return
    result = res.json().get('data')
    return result.get('subscribers')
