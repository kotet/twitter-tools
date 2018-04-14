# リストに入っている人のIDを標準出力に出すやつ
# 入力: コンシューマートークン、コンシューマーシークレット、アクセストークン、アクセスシークレット、リストのオーナー、リストのslug name。改行区切り

import tweepy

c_token = input().strip()
c_secret = input().strip()
a_token = input().strip()
a_secret = input().strip()
l_owner = input().strip()
l_slugname = input().strip()

auth = tweepy.OAuthHandler(c_token, c_secret)
auth.set_access_token(a_token, a_secret)
api = tweepy.API(auth, wait_on_rate_limit=True)

for user in tweepy.Cursor(api.list_members, owner_screen_name=l_owner, slug=l_slugname).items():
    print(user.id)
