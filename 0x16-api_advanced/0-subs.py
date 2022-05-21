#!/usr/bin/python3
"""Funtion that queries the Reddit API and returns
    the number of subscribers (not active users, total subscribers)
    for a given subreddit. If an invalid subreddit is given,
    the function should return 0."""
import requests

def number_of_subscribers(subreddit):
    """Returns the number of subscribers or 0 if
        invalid subreddit"""
    
    # private and public keys provided by reddit
    # CLIENT_ID = 'q5kLCDMoyRPHdgqp93f8YA'
    # SECRET_KEY = 'tCS6kr5BHJB1Hf0LOiQ_KYAGOjRaBA'

    # Payload for the GET request
    url = f'https://www.reddit.com/r/{subreddit}/about.json'
    headers = {'user-Agent': 'Noobdevsayswhat'}

    res = requests.get(url, headers=headers)

    if res.status_code > 299 and res.status_code < 500:
        return 0
    result = res.json().get('data')
    return result.get('subscribers')
