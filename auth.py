# 認証するやつ
# 入力: コンシューマートークン、コンシューマーシークレットの入ったファイルの名前、案内に従って入手した認証用コード。改行区切り
# 出力: コンシューマートークン、コンシューマーシークレット、アクセストークン、アクセスシークレット。改行区切り

import tweepy
import sys

sys.stderr.write("filename : ")
file = input()

with open(file, mode='r', encoding='utf-8') as f:
    text = f.readlines()
    c_token = text[0].strip()
    c_secret = text[1].strip()

auth = tweepy.OAuthHandler(c_token, c_secret)

sys.stderr.write(auth.get_authorization_url() + " : ")
verifier = input()

auth.get_access_token(verifier)

print(c_token)
print(c_secret)
print(auth.access_token)
print(auth.access_token_secret)
