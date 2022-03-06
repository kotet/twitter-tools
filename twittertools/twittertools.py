from asyncore import read
import json
import pkgutil
import tweepy


def authorize() -> tweepy.API:
    conf_bytes = pkgutil.get_data("twittertools", "config.json")
    d = json.JSONDecoder()
    conf = d.decode(conf_bytes.decode("utf-8"))
    auth = tweepy.OAuthHandler(conf["key"], conf["secret"])
    url = auth.get_authorization_url()
    verifier = input(f"access {url} and enter verifier:")
    auth.get_access_token(verifier)
    api = tweepy.API(auth)
    return api


def unblock_all(api: tweepy.API):
    for id in tweepy.Cursor(api.get_blocked_ids).items():
        print(f"unblocking {id} ...")
        try:
            user: tweepy.User = api.destroy_block(user_id=id)
            print(f"unblock {user.name} (@{user.screen_name})")
        except tweepy.TweepyException as e:
            print(f"failed to unblock {id}: {e}")
