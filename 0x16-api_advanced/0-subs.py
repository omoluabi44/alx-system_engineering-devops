#!/usr/bin/python3
"""get subscribers"""

import requests
def number_of_subscribers(subreddit):
    if subreddit is None or type(subreddit) is not str:
        return 0
    url = "https://www.reddit.com/r/" + subreddit + "/about.json"

    response = requests.get(url, timeout=10)

    data = response.json()
    if "data" in data and "subscribers" in data["data"]:
                sub =  data["data"]["subscribers"]
                print(sub)
                return sub
    else:
        return 0
              

    

 