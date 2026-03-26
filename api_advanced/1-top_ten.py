#!/usr/bin/python3
"""Prints the titles of the first 10 hot posts for a given subreddit."""
import json
import urllib.request
 
 
def top_ten(subreddit):
    """Query Reddit API and print top 10 hot post titles."""
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    req = urllib.request.Request(url, headers={"User-Agent": "MyRedditBot/1.0"})
    try:
        with urllib.request.urlopen(req) as response:
            if response.geturl() != url and "search" in response.geturl():
                print("None")
                return
            data = json.loads(response.read().decode("utf-8"))
            posts = data.get("data", {}).get("children", [])
            for post in posts:
                print(post.get("data", {}).get("title"))
    except Exception:
        print("None")
