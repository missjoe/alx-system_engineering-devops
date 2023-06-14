#!/usr/bin/python3
"""
Recursive function that queries the Reddit API and returns a list
containing the titles of all hot articles for a given subreddit.
"""

import requests


def recurse(subreddit, hot_list=[], after=None):
    """
    Recursively fetches hot articles for a given subreddit and returns
    a list of their titles.

    subreddit: string representing the subreddit to search.
    hot_list: list containing the hot article titles.
    after: string indicating the last post ID from the previous page.
    """
    headers = {'User-Agent': 'Mozilla/5.0'}
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    params = {'limit': 100, 'after': after}
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)

    if response.status_code != 200:
        return None

    data = response.json()
    children = data.get('data', {}).get('children', [])
    for child in children:
        title = child.get('data', {}).get('title', '')
        if title:
            hot_list.append(title)

    after = data.get('data', {}).get('after', None)
    if not after:
        return hot_list
    else:
        return recurse(subreddit, hot_list, after)
