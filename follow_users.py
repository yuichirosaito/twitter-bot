# coding=utf-8
import tweepy
from time import sleep
import os

# 認証情報を「.env」から読み取る
CONSUMER_KEY = os.environ['CONSUMER_KEY']
CONSUMER_SECRET = os.environ['CONSUMER_SECRET']
ACCESS_TOKEN = os.environ['ACCESS_TOKEN']
ACCESS_TOKEN_SECRET = os.environ['ACCESS_TOKEN_SECRET']
# 自分のアカウントIDをで書き換える
USER_SCREEN_NAME = 'Louis08565325'

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

# ツイート検索する文章
search_text = '#東京オリンピック'
MAX_FOLLOW_COUNT = 10

# ツイートを検索する
search_results = api.search(q=search_text, count=100, lang='ja', result_type='mixed')

# 以下の条件を満たしたユーザーを{MAX_FOLLOW_COUNT}人を上限としてフォローする。
# ・フォロワーが200人以上（200人以下のアカウントは、しっかり利用していないアカウントの可能性が低い）
# ・まだフォローしていない
follow_ids = api.friends_ids(USER_SCREEN_NAME)
new_follow_ids = []
for status in search_results:
    print('---------------------------------------')
    user = status.user
    user_id = user.id
    user_screen_name = user.screen_name
    user_name = user.name
    follower_count = user.followers_count

    # すでにフォローしているユーザーの場合は無視する。
    if user_id in follow_ids or user_id in new_follow_ids:
        print('{}（@{}）はすでにフォローしているから、フォローしなかったよ'.format(user_name, user_screen_name))
        continue

    # フォロワーが200人より少ない場合は無視する。
    if follower_count < 200:
        print('{}（@{}）はフォロワーが{}人しかないから、フォローしなかったよ'.format(user_name, user_screen_name, follower_count))
        continue

    # ユーザーをフォローする
    try:
        api.create_friendship(user_id)
        new_follow_ids.append(user_id)
        print('{}（@{}）を新規フォローしたよ'.format(user_name, user_screen_name))
    except Exception as e:
        print("{}（@{}）をフォローしようとしたらエラーになったよ:{}".format(user_name, user_screen_name, e))

    # 指定した上限人数のフォローが完了したらfor文を抜けて処理終了する。
    if len(new_follow_ids) >= MAX_FOLLOW_COUNT:
        break

print('{}人の駆け出しエンジニアを新しくフォローしたよ！'.format(len(new_follow_ids)))