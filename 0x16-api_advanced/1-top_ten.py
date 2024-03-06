#!/usr/bin/python3

"""imports a module to retrieve info"""
import requests


def top_ten(subreddit):
    """function that queries the Reddit API and prints
    the titles of the first 10 hot posts"""

    api_url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {'User-Agent': 'your_user_agent'}

    params = {'limit': 10}
    response = requests.get(api_url, headers=headers, allow_redirects=False,
                            params=params)

    subreddit_info = response.json()

    if response.status_code == 200:

        for post in subreddit_info['data']['children']:
            print(post['data']['title'])

    else:
        print(None)
