#!/usr/bin/python3
"""imports a module to retrieve info"""
import requests


def number_of_subscribers(subreddit):
    """function that queries the Reddit API
    and returns the number of subscribers"""

    custom_user_agent = 'your_custom_user_agent/1.0 by Wallace'
    api_url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {'User-Agent': custom_user_agent}
    response = requests.get(api_url, headers=headers, allow_redirects=False)

    if response.status_code == 404:

        return (0)

    subreddit_info = response.json().get('data')
    return subreddit_info.get('subscribers')
