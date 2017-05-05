# !pip install tweepy
import sys

def download_recent_tweets_by_user(user_account_name, keys):
    """Downloads tweets by one Twitter user.

    Args:
        user_account_name (str): The name of the Twitter account
          whose tweets will be downloaded.
        keys (dict): A Python dictionary with Twitter authentication
          keys (strings), like this (but filled in):
            {
                "consumer_key": "<your Consumer Key here>",
                "consumer_secret":  "<your Consumer Secret here>",
                "access_token": "<your Access Token here>",
                "access_token_secret": "<your Access Token Secret here>"
            }

    Returns:
        list: A list of Status objects, each representing one tweet."""
    import tweepy
    import keys
    auth = tweepy.OAuthHandler(keys.consumer_key, keys.consumer_secret)
    auth.set_access_token(keys.access_token, keys.access_token_secret)
    api = tweepy.API(auth)

    # Getting as many recent tweets as Twitter will let us have:
    tweets = list(tweepy.Cursor(api.user_timeline, id=user_account_name).items(sys.argv[2]))
    return tweets

def save_tweets(tweets, path):
    """Saves a list of tweets to a file in the local filesystem.

    Args:
        tweets (list): A list of tweet objects (of type Status) to
          be saved.
        path (str): The place where the tweets will be saved.

    Returns:
        None"""
    # Saving the tweets to a file as "pickled" objects:
    with open(path, "wb") as f:
        import pickle
        pickle.dump(tweets, f)

def archive_tweets(user_account_name, keys_path):
    """Archives recent tweets from one user.
    
    Args:
        user_account_name (str): The Twitter handle of a user, without the @.
        keys_path (str): The path to a JSON keys file in your filesystem.
    """
    import time
    import datetime
    st = datetime.datetime.fromtimestamp(time.time()).strftime('%m-%d-%Y___%H-%M-%S')
    save_path = "archived_tweets/{}___{}.pkl".format(user_account_name, st)
    tweets = download_recent_tweets_by_user(user_account_name)
    save_tweets(tweets, save_path)

""" =========================================== SCARY CODE ABOVE =========================================== """

""" Note: Install Python3.2 before running script 

Takes in twitter handle as command line argument. Must have a keys.py file in same folder, with appropriate variables.
"""

user_account_name = sys.argv[1]

archive_tweets(user_account_name, keys_path)
