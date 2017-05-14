#!/usr/bin/env/python3

from flask import Flask, render_template, request, json
import search_TwitterAPI
import os
import sys
from py2neo import Graph

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

	graphenedb_url = os.environ.get("GRAPHENEDB_BOLT_URL")
	graphenedb_user = os.environ.get("GRAPHENEDB_BOLT_USER")
	graphenedb_pass = os.environ.get("GRAPHENEDB_BOLT_PASSWORD")
	graph = Graph(graphenedb_url, user=graphenedb_user, password=graphenedb_pass, bolt = True, secure = True, http_port = 24789, https_port = 24780)

	constraint("Tweet", "id")
	constraint("User", "username")
	constraint("Hashtag", "name")

	since_id = -1
	
	try:
		tweets = find_tweets(search, number_objects, since_id=since_id)
		since_id = tweets[0].get('id')
		upload_tweets(tweets)
	except Exception as e:
		console.log(e)

	result = graph.run("MATCH (n) RETURN (n)")

	return render_template('index.html', data=result)

if __name__ == "__main__":
	app.run(debug=True)
	# Bind to PORT if defined, otherwise default to 5000.
	port = int(os.environ.get('PORT', 5000))
	app.run(host='0.0.0.0', port=port)