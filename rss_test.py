# coding=utf-8
import feedparser

RSS_URL = 'https://employment.en-japan.com/engineerhub/rss'

# RSSのデータ取得
rss_dict = feedparser.parse(RSS_URL)

# RSSの記事データを1記事ずつ処理していく
entry_count = 0
for entry in rss_dict.entries:
    entry_count += 1
    if entry_count > 50:
        break
    print('------------------------------------------')
    # 何番目の記事か、記事のタイトル、記事のリンクを出力していく。
    print('{}個目の記事データ タイトル:{}\nURL:{}'.format(entry_count, entry.title, entry.link))