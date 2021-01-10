# coding=utf-8
import tweepy
import feedparser

# 以下4つ「xxxxx」を、先ほど控えた値で書き換える。
CONSUMER_KEY='Atedi8Lbymj7iaThZH66xBmJw'
CONSUMER_SECRET='SRZeWJNw5dlqTMuTEsgkEHhVpNb5hvWpXJYtpjZbb5wSOXxACI'
ACCESS_TOKEN='1346464627563978752-4pluUV4CxrM5YBsl4wQFiI0K2PT6EL'
ACCESS_TOKEN_SECRET='Ut3PmWI8iPaQFjGW9HwxcgJqriaZcVQan6wXxLZoZiiAc'

RSS_URL = 'https://employment.en-japan.com/engineerhub/rss'
TEXT = 'チュートリアル実践中！ #さぼりエンジニア養成所'

# RSSのデータ取得
rss_dict = feedparser.parse(RSS_URL)

# RSSの記事データを1記事ずつ処理していく
entry_count = 0
for entry in rss_dict.entries:
    entry_count += 1
    # 1記事分だけツイートしたいので、2個目以降の記事の処理が始まったら処理を抜ける。
    if entry_count > 1:
        break

    # ツイートする文章を作成する。
    tweet_text = '{}\n\n{}\n{}'.format(entry.title, entry.link, TEXT)

    # 記事のタイトルとリンクと一言をツイートする。
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
    api = tweepy.API(auth)
    api.update_status(status=tweet_text)