#!/usr/bin/python3

"""imports a module to retrieve info"""
import requests


def number_of_subscribers(subreddit):
    """function that queries the Reddit API
    and returns the number of subscribers"""
    api_url = "https://www.reddit.com/r/{}/about.json".format(subreddit)

    response = requests.get(api_url, headers={'User-Agent': 'your_user_agent'},
                            allow_redirects=False)

    if response.status_code == 200:
        subreddit_info = response.json().get('data', {}).get('subscribers', 0)

        return subreddit_info

    elif response.status_code == 404:

        return (0)
