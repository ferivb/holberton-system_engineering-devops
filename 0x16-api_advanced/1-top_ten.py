#!/usr/bin/python3
""" Function that queries the Reddit API and
    prints the titles of the first 10 hot posts
    listed for a given subreddit."""
import json
import requests


def top_ten(subreddit):
    # Payload for the GET request
    url = f'https://www.reddit.com/r/{subreddit}/hot.json'
    headers = {'user-Agent': 'Noobdevsayswhat'}
    params = {'limit': 10}

    # Request placeholder
    res = requests.get(url, headers=headers, params=params)

    # Restrain for unexistant subs
    if res.status_code > 299 and res.status_code < 500:
        print("None")
        return

    # Return
    result = res.json()
    # All the data of the Reddit API JSON response is
    # nested inside the ‘children’ object of the ‘data’.
    posts = result['data']['children']
    # For each post iterate the list in the middle:
    # ['data']['children'][0]['data'].keys():
    for post in posts:
        print(post.get('data').get('title'))
