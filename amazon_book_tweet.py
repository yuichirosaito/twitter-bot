# coding=utf-8
import tweepy
import random
import requests
import bs4
import os

# 認証情報を「.env」から読み取る
CONSUMER_KEY = os.environ['CONSUMER_KEY']
CONSUMER_SECRET = os.environ['CONSUMER_SECRET']
ACCESS_TOKEN = os.environ['ACCESS_TOKEN']
ACCESS_TOKEN_SECRET = os.environ['ACCESS_TOKEN_SECRET']

# 以下のリンクは、先ほどコピーしておいたAmazonのURLで置き換える。ここでは「リーダブルコード」の詳細ページのURLになっている。
AMAZON_BOOK_URL = 'https://www.amazon.co.jp/%E3%82%AA%E3%83%BC%E3%83%89%E3%83%AA%E3%83%BC%E3%83%BB%E3%82%BF%E3%83%B3-%E3%83%87%E3%82%B8%E3%82%BF%E3%83%AB%E3%81%A8AI%E3%81%AE%E6%9C%AA%E6%9D%A5%E3%82%92%E8%AA%9E%E3%82%8B/dp/4833423995/ref=msx_wsirn_v1_5/358-6374752-4424844?_encoding=UTF8&pd_rd_i=4833423995&pd_rd_r=8df5da79-dedb-457a-9769-f5cdb7da4d32&pd_rd_w=zVp3x&pd_rd_wg=yoATD&pf_rd_p=5369296e-7a8b-4cb4-8afd-800132ad0363&pf_rd_r=86902842J16AC33E49N5&psc=1&refRID=86902842J16AC33E49N5'
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
formatted_book_title = book_title.split('　|')[0]

# ツイート文章を作成する。
comment = random.choice(RANDOM_COMMENTS)
tweet_text = comment.format(formatted_book_title, AMAZON_BOOK_URL, TEXT)

# Amazonの本の紹介ツイートをする。
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)
api.update_status(status=tweet_text)