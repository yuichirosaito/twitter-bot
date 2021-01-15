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

s = '東京オリンピック 東京五輪'
#検索ワードをURLエンコードに変換
s_quote = urllib.parse.quote(s)
#グーグルニュース検索のURLの間に挟む
RSS_URL = "https://news.google.com/news/rss/search/section/q/" + s_quote + "/" + s_quote + "?ned=jp&amp;hl=ja&amp;gl=JP"

# RSSのデータ取得
rss_dict = feedparser.parse(RSS_URL)
news = []
for entry in rss_dict.entries:
    
    p = entry.published_parsed
    sortkey = "%04d%02d%02d%02d%02d%02d" % (p.tm_year, p.tm_mon, p.tm_mday, p.tm_hour, p.tm_min, p.tm_sec)

    tmp = {
    "title": entry.title,
    "link": entry.link,
    "sortkey": sortkey
    }

    news.append(tmp)

new_news = sorted(news, key=lambda x:x['sortkey'], reverse=True)
entry_count = 0
for entry in new_news:
    entry_count += 1
    # 1記事分だけツイートしたいので、2個目以降の記事の処理が始まったら処理を抜ける。
    if entry_count > 3:
        break

    # ツイートする文章を作成する。
    tweet_text = '{:.120}\n\n{}'.format(entry['title'], entry['link'])

    # 記事のタイトルとリンクと一言をツイートする。
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
    api = tweepy.API(auth)
    api.update_status(status=tweet_text)

