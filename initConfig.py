import tweepy
import json
from loggingModule import logger
import os


#初始化访问twitter的API配置的key
def init():
    try:
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
        # logger.warning("获取失败")
        # 获取api对象
        api = tweepy.API(auth, wait_on_rate_limit=True)
        return (api, userList)
    except Exception as e:
        print("获取API设置KEY错误", e)
        logger.warning("获取失败%s" % e)
