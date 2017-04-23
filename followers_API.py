import os
import sys
import time
import requests
from bs4 import BeautifulSoup
from bs4 import SoupStrainer
import re
from py2neo import Graph, Relationship, Node

#########################################################################################################
# http://py2neo.org/v3/database.html - docs v3
# http://py2neo.org/2.0/essentials.html#py2neo.Graph.merge - docs v2
# https://dev.twitter.com/rest/reference/get/followers/ids - get followers
#########################################################################################################


def upload_accounts(accounts):
    u = accounts[0]
    followers = accounts[1:]
    
    user = Node("User", id=u['screen_name'])
    graph.merge(user)
    user['username'] = u['screen_name']
    user.push()
  
    for f in followers:
        follower = Node("Follower", id=f['screen_name'])
        graph.merge(follower)
        follower['username'] = f['screen_name']
        follower.push()

        graph.create(Relationship(follower, "FOLLOWS", user)) #is this follwer -> user ?
        


def constraint(label, property):
    schema = graph.schema
    if property not in schema.get_uniqueness_constraints(label):
        schema.create_uniqueness_constraint(label, property)


graph = Graph("http://neo4j:Berkatores19!@localhost:7474/browser/")
constraint("User", "username")
constraint("Follower", "username")

while True:
    try:
        # followers = open(input('search.py')).readlines()
        # PULL FOLLOWERS FROM TWITTER API // RATE LIMITED?!?!?!?
        upload_accounts(followers)
        time.sleep(60)

    except Exception as e:
        print(e)
        time.sleep(60)
        continue


# while True:
#     try:
#         followers = find_followers(sys.argv[1])
#         upload_accounts(followers)
#         time.sleep(60)
#         # print("trylol")

#     except Exception as e:
#         # print("fail")
#         print(e)
#         time.sleep(60)
#         continue