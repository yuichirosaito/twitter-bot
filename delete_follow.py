# coding=utf-8
import tweepy
import feedparser
import os
import urllib
import json
import pprint
from IPython import embed

# 以下4つ「xxxxx」を、先ほど控えた値で書き換える。
CONSUMER_KEY = os.environ['CONSUMER_KEY']
CONSUMER_SECRET = os.environ['CONSUMER_SECRET']
ACCESS_TOKEN = os.environ['ACCESS_TOKEN']
ACCESS_TOKEN_SECRET = os.environ['ACCESS_TOKEN_SECRET']

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth, wait_on_rate_limit=True)

user = "Louis08565325"
for status in api.friends(user="Louis08565325", count=100):
    print(status.id)
    print("Do you really want to unfollow this person?")
    """if input()=="y"or "Y": #削除するかどうかの最後の確認"""
    api.destroy_friendship(status.id)
