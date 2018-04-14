# フォローしてる人全員分のIDを取得するやつ
# 入力: コンシューマートークン、コンシューマーシークレット、アクセストークン、アクセスシークレット、対象者のスクリーンネーム。改行区切り

import tweepy

c_token = input().strip()
c_secret = input().strip()
a_token = input().strip()
a_secret = input().strip()
target = input().strip()

auth = tweepy.OAuthHandler(c_token, c_secret)
auth.set_access_token(a_token, a_secret)
api = tweepy.API(auth, wait_on_rate_limit=True)

for user_id in tweepy.Cursor(api.friends_ids, screen_name=target).items():
    print(user_id)
