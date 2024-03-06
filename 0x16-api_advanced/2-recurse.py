#!/usr/bin/python3

"""imports a module to retrieve info"""
import requests


def recurse(subreddit, hot_list=[], after=None, count=0):
    """Write a recursive function that queries the Reddit API and
    returns a list containing the titles of all hot articles"""

    api_url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {'User-Agent': 'your_user_agent'}
    params = {'after': after, 'count': count}
    response = requests.get(api_url, headers=headers, allow_redirects=False,
                            params=params)

    subreddit_info = response.json().get('data')
    after = subreddit_info.get('after')
    count += subreddit_info.get('dist')
    if response.status_code == 404:

        return None
    for post in subreddit_info['children']:
        hot_list.append(post['data']['title'])

    if after is not None:
        return recurse(subreddit, hot_list, after, count)

    return hot_list
