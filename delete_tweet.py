# coding=utf-8
import tweepy
import feedparser
import os
import urllib
import json
import pprint

# 以下4つ「xxxxx」を、先ほど控えた値で書き換える。
CONSUMER_KEY = os.environ['CONSUMER_KEY']
CONSUMER_SECRET = os.environ['CONSUMER_SECRET']
ACCESS_TOKEN = os.environ['ACCESS_TOKEN']
ACCESS_TOKEN_SECRET = os.environ['ACCESS_TOKEN_SECRET']

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

for status in tweepy.Cursor(api.user_timeline).items():
    print(status.text)
    print("Delete OK?")
    if input()=="y"or "Y": #削除するかどうかの最後の確認
        api.destroy_status(status.id)


"""import tweepy

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
api = tweepy.API(auth)

def my_tweet_delete(RT,keyword):
    for status in tweepy.Cursor(api.user_timeline).items():
        if RT==False and "RT @" in status.text: #リツイートを含めるかどうか
            pass
        elif keyword!=""and  keyword in status.text: #キーワードが空白でない
            print(status.text)
            print("Delete OK?")
            if input()=="y"or "Y": #削除するかどうかの最後の確認
                api.destroy_status(status.id)

if __name__ == '__main__':
    keyword='python'
    my_tweet(True,keyword) 
#api制限で最大取得できるツイートが3190"""
