# dstscollider
Creating scripts to help defense analytics firms track terrorist activity on twitter.
Our current final projects are search_TwitterAPI.py, Archiver.py, Loader.py. Working on completing followers_selenium.py
After finals I'm going to embed these programs in a website or at least build out a GUI.

NOTE, in order for this to work you must have a file 'keys.py.' That file must have the following variables declared:

consumer_key, consumer_secret, access_token, access_token_secret, twitter_bearer

You can get all of these (except the twitter_bearer) by making a twitter application  here: https://apps.twitter.com
To get the twitter_bearer, set the field equal to anything (ex twitter_bearer = "Hello World"). Then run the get_twitter_bearer.py file which will replace it with the correct value.

## Archiver.py (main)
Archives tweets from account. Saves them in new folder called 'archived_tweets.'
Takes two commandline arguments, twitter handle and number of tweets to archive.

ex. python Archiver.py Beyonce 500

## Loader.py (main)
Loads saved tweets. 
Takes one commandline argument, name of file saved in archived_tweets folder.

ex. python Loader.py Beyonce___02-23-2017___17-34-36.pkl

## followers_API.py	
Incomplete - intended to pull out lists of followers using Twitter API and visualize them in Neo4j. Because of rate limiting switching to selenium.

## followers_selenium.py (main)
Incomplete - uses cookies to log into twitter account and pull lists of followers from other accounts. Problems is 1) it doesn't work with PhantomJS, only Chrome or any other non-headless drivers (because it 'scrolls down' to view the javascript and headless driver doesn't render that. Working on fixing it.

## get_cookies.py
Gets cookies and prints them in terminal. Used to put into followers_selenium.py so that we can re-use login information.

## get_twitter_bearer.py
Gets twitter bearer and (over)writes it into keys file. twitter_bearer is used in search_TwitterAPI.py

## openwebpage_selenium.py
This is a script that opens a webpage using selenium. Specific subsection of code that I thought might be useful to keep in a seperate file.

## search_TwitterAPI.py (main)
This program creates a visualization of twitter search using neo4j. You enter a search term. the program pulls users, hashtags, and posts and classifies the relationship (edge labels) as replies to, retweets, posts, etc. You must have the neo4j server open and runnning, and to show all you must do that in neo4j. This program seperates out the nodes and edge relationships and enters them in our neo4j database.

Setup: Start Neo4J server. Run the program with two command line arguments, the search term and the count of objects (users, posts and hashtags) you want. I recommend 100-500. Then go into Neo4J and run "Match (n) Return (n)"
