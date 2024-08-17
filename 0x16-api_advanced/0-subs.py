#!/usr/bin/python3
"""get subscribers"""

import requests
def number_of_subscribers(subreddit):
    """
    Return the number of subscribers for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit.

    Returns:
        int: The number of subscribers.
    """
    # Construct the url
    url = "https://www.reddit.com/r/" + subreddit + "/about.json"

    # Make a request to the url
    response = requests.get(url)
    # Get the data from the response
    data = response.json()

    # Get the number of subscribers from the data
    subscribers = data["data"]["subscribers"]

    # Return the number of subscribers
    return subscribers
