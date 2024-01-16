#!/usr/bin/python3
"""
the number of subscribers for a given subreddit.
"""
import requests


def number_of_subscribers(subreddit):
    """Queries the Reddit API to get the number of
    subscribers for a given subreddit."""
    user_agent = 'My User Agent 1.0'
    headers = {'User-Agent': user_agent}
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code != 200:
        return 0

    data = response.json().get('data')
    subscribers = data.get('subscribers') if data and 'subscribers' in data else 0
    return subscribers
