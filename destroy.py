# 標準入力で受け取ったIDの人をリムるやつ。
# 入力: コンシューマートークン、コンシューマーシークレット、アクセストークン、アクセスシークレット、以下対象者のID。改行区切り

import tweepy
import sys

c_token = input().strip()
c_secret = input().strip()
a_token = input().strip()
a_secret = input().strip()

auth = tweepy.OAuthHandler(c_token, c_secret)
auth.set_access_token(a_token, a_secret)
api = tweepy.API(auth, wait_on_rate_limit=True)

for target in sys.stdin:
    api.destroy_friendship(id=int(target.strip()))