#!/usr/bin/python3
"""Recursively queries Reddit API and counts keyword occurrences in titles."""
import requests


def count_words(subreddit, word_list, counts={}, after=None):
    """Recursively count keyword occurrences in hot post titles."""
    if not counts:
        for word in word_list:
            w = word.lower()
            counts[w] = counts.get(w, 0)

    url = "https://www.reddit.com/r/{}/hot.json?limit=100".format(subreddit)
    headers = {"User-Agent": "MyBot/1.0"}
    params = {"after": after} if after else {}
    res = requests.get(url, headers=headers,
                       params=params, allow_redirects=False)
    if res.status_code != 200:
        return

    data = res.json().get("data", {})
    posts = data.get("children", [])
    after = data.get("after")

    for post in posts:
        title = post.get("data", {}).get("title", "").lower().split()
        for word in title:
            if word in counts:
                counts[word] += 1

    if after is None:
        sorted_counts = sorted(counts.items(), key=lambda x: (-x[1], x[0]))
        for word, count in sorted_counts:
            if count > 0:
                print("{}: {}".format(word, count))
        return

    return count_words(subreddit, word_list, counts, after)
