#!/usr/bin/env/python3

from flask import Flask, render_template, request, json
import search_TwitterAPI
import os
import sys
from py2neo import Graph

import os
import sys
import time
import requests
import keys
from py2neo import Graph, Relationship, Node

################# NOTES ##################
# add alerts for exam schedule conflicts #
##########################################

app = Flask(__name__)

@app.route("/")
def main():
	return render_template('index.html')

@app.route("/showGraph", methods=["POST"])
def graph():
	search = request.form["twitter_search_term"]
	number_objects = request.form["number_objects"]

	# graphenedb_url = os.environ.get("GRAPHENEDB_BOLT_URL")
	# graphenedb_user = os.environ.get("GRAPHENEDB_BOLT_USER")
	# graphenedb_pass = os.environ.get("GRAPHENEDB_BOLT_PASSWORD")
	# graph = Graph(graphenedb_url, user=graphenedb_user, password=graphenedb_pass, bolt = True, secure = True, http_port = 24789, https_port = 24780)
	graph = Graph("http://" + 'neo4j' + ":" + 'Berkatores19!' + "@localhost:7474/browser/")
	#possibly run detach to delete all nodes

	def constraint(label, property):
		schema = graph.schema
		if property not in schema.get_uniqueness_constraints(label):
			schema.create_uniqueness_constraint(label, property)
	

	constraint("Tweet", "id")
	constraint("User", "username")
	constraint("Hashtag", "name")

	since_id = -1
	

	def find_tweets(keyword, cnt, since_id=-1):
		TWITTER_BEARER = keys.twitter_bearer
		
		headers = dict(
		  accept = 'application/json',
		  Authorization='Bearer ' + TWITTER_BEARER
		)
		
		payload = dict(
		  q= keyword,
		  count = cnt,
		  result_type = "recent",
		  lang = "en",
		  since_id = since_id
		)
		
		base_url = "https://api.twitter.com/1.1/search/tweets.json?"
		url = base_url + "q={q}&count={count}&result_type={result_type}&lang={lang}&since_id={since_id}".format(**payload)
		
		r = requests.get(url, headers=headers)
		tweets = r.json()["statuses"]

		return tweets


	def upload_tweets(tweets):
		for t in tweets:
			u = t['user']
			e = t['entities']

			tweet = Node("Tweet", id=t['id'])
			graph.merge(tweet)
			tweet['text'] = t['text']
			tweet['id'] = t['id']
			tweet.push()

			user = Node("User", id=u['screen_name'])
			graph.merge(user)
			user['username'] = u['screen_name']
			user.push()

			graph.create(Relationship(user, "POSTS", tweet))

			for h in e.get('hashtags', []):
				hashtag = Node("Hashtag", id=h['text'].lower())
				graph.merge(hashtag)
				hashtag['name'] = h['text'].lower() #Hashtag searches are not case-sensitive
				hashtag.push()

				graph.create(Relationship(hashtag, "TAGS", tweet))


			for m in e.get('user_mentions', []):
				mention = Node("User", id=m['screen_name'])
				graph.merge(mention)
				mention['username'] = m['screen_name']
				mention.push()

				graph.create(Relationship(tweet, "MENTIONS", mention))

			reply = t.get('in_reply_to_status_id')
			if reply:
				reply_tweet = Node("Tweet", id=reply)
				graph.merge(reply_tweet)
				reply_tweet["id"] = reply
				reply_tweet.push()
		
				graph.create(Relationship(tweet, "REPLY_TO", reply_tweet))

			r = t.get('retweeted_status', {})
			r = r.get('id')

			if r:
				retweet = Node("Tweet", id=r)
				graph.merge(retweet)
				retweet["id"] = r
				retweet.push()
			
				graph.create(Relationship(tweet, "RETWEETS", retweet))


	try:
		tweets = find_tweets(search, number_objects, since_id=since_id)
		since_id = tweets[0].get('id')
		upload_tweets(tweets)
	except Exception as e:
		return render_template('error.html', data=e)

	#it finished loading things into the database. now we need to pull it out and render using d3

	return render_template('index.html', data=result)

if __name__ == "__main__":
	app.run(debug=True)
	# Bind to PORT if defined, otherwise default to 5000.
	port = int(os.environ.get('PORT', 5000))
	app.run(host='0.0.0.0', port=port)