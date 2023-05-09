#!/usr/bin/python3
"""
Queries the Reddit API, parses the title of all hot articles,
and prints a sorted count of given keywords.
"""

import requests


def count_words(subreddit, word_list, after=None, counts={}):
    """
    Recursive function that queries the Reddit API, parses the title of all hot
    articles, and prints a sorted count of given keywords.

    Args:
        subreddit (str): The subreddit to query.
        word_list (list): A list of words to count.
        after (str, optional): The "after" parameter in the API request.
        counts (dict, optional): A dictionary that keeps track of the counts of
            each word.

    Returns:
        The counts dictionary.
    """
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}
    params = {"limit": 100, "after": after}
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)

    if response.status_code != 200:
        return None

    data = response.json().get("data", {})
    after = data.get("after", None)
    children = data.get("children", [])

    for child in children:
        title = child.get("data", {}).get("title", "").lower()
        for word in word_list:
            count = title.count(word.lower())
            if count > 0:
                if word in counts:
                    counts[word] += count
                else:
                    counts[word] = count

    if after is not None:
        return count_words(subreddit, word_list, after, counts)
    else:
        sorted_counts = sorted(counts.items(), key=lambda x: (-x[1], x[0]))
        for count in sorted_counts:
            print("{}: {}".format(count[0], count[1]))

        return counts
