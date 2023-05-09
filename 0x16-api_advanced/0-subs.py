import requests


def number_of_subscribers(subreddit):
    # Set custom User-Agent header to avoid Too Many Requests error
    headers = {'User-Agent': 'my_bot/0.0.1'}

    # Send GET request to Reddit API
    url = f'https://www.reddit.com/r/{subreddit}/about.json'
    response = requests.get(url, headers=headers, allow_redirects=False)

    # Check if subreddit exists
    if response.status_code == 200:
        data = response.json()
        subscribers = data['data']['subscribers']
        return subscribers
    else:
        return 0
