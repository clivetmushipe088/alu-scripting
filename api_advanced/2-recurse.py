#!/usr/bin/python3
"""Recursively queries Reddit API and returns all hot article titles."""
import requests
 
 
def recurse(subreddit, hot_list=[], after=None):
    """Recursively get all hot post titles for a subreddit."""
    url = "https://www.reddit.com/r/{}/hot.json?limit=100".format(subreddit)
    headers = {"User-Agent": "MyBot/1.0"}
    params = {"after": after} if after else {}
    res = requests.get(url, headers=headers,
                       params=params, allow_redirects=False)
    if res.status_code != 200:
        return None
    data = res.json().get("data", {})
    posts = data.get("children", [])
    after = data.get("after")
    for post in posts:
        hot_list.append(post.get("data", {}).get("title"))
    if after is None:
        return hot_list
    return recurse(subreddit, hot_list, after)
