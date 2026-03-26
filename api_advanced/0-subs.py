#!/usr/bin/python3
"""Returns the number of subscribers for a given subreddit."""
import requests


def number_of_subscribers(subreddit):
    """Query Reddit API and return total subscribers for a subreddit."""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {"User-Agent": "MyRedditBot/1.0"}
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        return response.json().get("data", {}).get("subscribers", 0)
    return 0
