# !pip install tweepy
import sys

def load_tweets(path):
    """Loads tweets that have previously been saved.
    
    Args:
        path (str): The place where the tweets were be saved.

    Returns:
        list: A list of Status objects, each representing one tweet."""
    with open(path, "rb") as f:
        import pickle
        tweets = pickle.load(f)
    return tweets

""" =========================================== SCARY CODE ABOVE =========================================== """

""" Note: Install Python3.2 before running script """

""" 
Note: must include '.pkl' at end. Also must be in quotation marks.

Ex. "ali_wetrill___02-23-2017___17-34-36.pkl" is VALID
Ex. ali_wetrill___02-23-2017___17-34-36.pkl is invalid
Ex. "ali_wetrill___02-23-2017___17-34-36" is invalid

Takes this in as a command line argument. Must have an archived_tweets folder within file structure

"""

filename = sys.argv[1]

load_tweets("archived_tweets/" + filename)