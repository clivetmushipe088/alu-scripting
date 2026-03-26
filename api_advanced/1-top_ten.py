#!/usr/bin/python3
"""Prints the titles of the first 10 hot posts for a given subreddit."""
import requests
 
 
def top_ten(subreddit):
    """Query Reddit API and print top 10 hot post titles."""
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    headers = {"User-Agent": "MyBot/1.0"}
    res = requests.get(url, headers=headers, allow_redirects=False)
    if res.status_code != 200:
        print("None")
        return
    posts = res.json().get("data", {}).get("children", [])
    for post in posts:
        print(post.get("data", {}).get("title"))
