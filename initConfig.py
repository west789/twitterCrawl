import tweepy
import json


#初始化访问twitter的API配置的key
def init():
    with open("./config.json", 'r') as f:
        data = json.load(f)
        keyData = data.get("twitterKey")
        userList = data.get("userList")
    consumer_key = keyData.get("consumer_key")
    consumer_secret = keyData.get("consumer_secret")
    access_token = keyData.get("access_token")
    access_token_secret = keyData.get("access_token_secret")
    # 提交KEY和SECRET
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    # 获取api对象
    api = tweepy.API(auth, wait_on_rate_limit=True, proxy="127.0.0.1:1080")
    return (api, userList)