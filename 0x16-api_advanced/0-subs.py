#!/usr/bin/python3
"""returns the number of subscribers.
"""
import requests
import sys


def number_of_subscribers(subreddit):
    base_url = 'https://www.reddit.com'
    api_uri = f'{base_url}/r/{subreddit}/about.json'

    user_agent = {'User-Agent': 'My User Agent 2.0'}

    # Use a session to persist cookies and headers across requests
    with requests.Session() as session:
        res = session.get(api_uri, headers=user_agent, allow_redirects=False)

        # Check for redirection
        if res.status_code == 302:
            return 0

        # Check for invalid subreddit
        if res.status_code == 404:
            return 0

        # Check if the response is successful (200 OK)
        if res.status_code == 200:
            return res.json().get('data', {}).get('subscribers', 0)
    return 0


# Test cases
print(number_of_subscribers('existing_subreddit'))
# Replace with an actual existing subreddit
print(number_of_subscribers('nonexisting_subreddit'))
# Replace with an invalid subreddit
