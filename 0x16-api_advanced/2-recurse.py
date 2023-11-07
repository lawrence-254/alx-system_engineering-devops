#!/usr/bin/python3
"""
a function that queries the Reddit API
Returns: the number of subscribers
(not active users, total subscribers) for a given subreddit
Returns 0 If an invalid subreddit is given
"""
import requests


def top_ten(subreddit):
    """
    Queries a given subredit API and returns number subscribers to the
    subredit

    subreddit(str): the name of the subreddit in question

    Returns: Number of sbscribers
        else 0 if none
    """
    user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36\
            (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36'
    headers = {'User-Agent': user_agent}
    url = f'https://www.reddit.com/r/{subreddit}/new/.json?limit=10'

    response = requests.get(url, headers=headers, allow_redirects=False)

    subs_count = 0
    if response.status_code == 200:
        resp_dict = response.json()
        resp_dict = resp_dict.get('data', {})
        resp_list = resp_dict.get('children', [])
        for posts in resp_list:
            post = posts.get('data', {})
            title = post.get('title')
            if title is not None:
                print(title)
    else:
        print(None)
