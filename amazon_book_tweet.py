# coding=utf-8
import tweepy
import random
import requests
import bs4
import os
from IPython import embed


# 認証情報を「.env」から読み取る
CONSUMER_KEY = os.environ['CONSUMER_KEY']
CONSUMER_SECRET = os.environ['CONSUMER_SECRET']
ACCESS_TOKEN = os.environ['ACCESS_TOKEN']
ACCESS_TOKEN_SECRET = os.environ['ACCESS_TOKEN_SECRET']

# 以下のリンクは、先ほどコピーしておいたAmazonのURLで置き換える。ここでは「リーダブルコード」の詳細ページのURLになっている。
AMAZON_BOOK_URL = 'https://www.amazon.co.jp/gp/product/4297107384/ref=ox_sc_act_title_1?smid=AN1VRQENFRJN5&psc=1'
TEXT = 'こんにちは！'

# いずれかのコメント文章をランダムに利用する。
RANDOM_COMMENTS = ['『{}』はめちゃくちゃいい本！駆け出しエンジニアにオススメ！\n\n{}\n{}',
                   '初心者で読んで良かったのは『{}』。ちょっと高いけどオススメです。\n\n{}\n{}',
                   '今日はこれ読みます！\n『{}』\n\n{}\n{}']

# Amazonの本の詳細ページのデータ取得
response = requests.get(AMAZON_BOOK_URL)
soup = bs4.BeautifulSoup(response.text, "html.parser")
book_title = soup.find('title').text

# 「タイトル | 著者名 | ...」というデータが取得できるので、「タイトル」と「 | 著者名 | ...」に分けて前半のデータを使う。
formatted_book_title = book_title.split('|')[0]

# ツイート文章を作成する。
comment = random.choice(RANDOM_COMMENTS)
tweet_text = comment.format(formatted_book_title, AMAZON_BOOK_URL, TEXT)

# Amazonの本の紹介ツイートをする。
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)
api.update_status(status=tweet_text)