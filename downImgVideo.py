import requests
import os
import aiohttp
import asyncio
from loggingModule import logger
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36"}
basePath = os.path.join(os.getcwd())

# 创建目录


def mkdirThreeFiles():
    if not os.path.exists(basePath+"/videos"):
        os.mkdir(basePath+"/videos")
    if not os.path.exists(basePath + "/images"):
        os.makedirs(os.path.join(basePath+"/images", 'headImg'))
        os.makedirs(os.path.join(basePath+"/images", 'tweetImg'))
        os.makedirs(os.path.join(basePath+"/images", 'bannerImg'))
# 下载视频


def downloadVideo(videoUrl):
    try:
        videoUrl = videoUrl.split("?")[0]
        baseVideoPath = os.path.join(basePath, "videos")
        videoName = os.path.basename(videoUrl)
        response = requests.get(videoUrl, headers=headers)
        videoContent = response.content
        with open(baseVideoPath+"/%s" % videoName, "wb") as f:
            f.write(videoContent)
        return videoName
    except Exception as e:
        logger.warning(e)
        return ""

# 下载推文照片


def downloadImg(imgUrl):
    try:
        imgName = os.path.basename(imgUrl)
        response = requests.get(imgUrl, headers=headers)
        imgContent = response.content
        with open(basePath + "/images/tweetImg" + "/%s" % imgName, 'wb') as f:
            f.write(imgContent)
        # imgPath = basePath + "/images" + "/%s" % imgName
        return imgName
    except Exception as e:
        logger.warning(e)
        return ""

# 下载头像图片


def downloadHead(profileImgUrl):
    try:
        if not os.path.exists(basePath + "/images"):
            os.mkdir(basePath + "/images")
            if not os.path.exists(basePath + '/images/headImg'):
                os.mkdir(basePath + '/images/headImg')
        profileImgName = os.path.basename(profileImgUrl)
        response = requests.get(profileImgUrl, headers=headers)
        with open(basePath + '/images/headImg/%s' % profileImgName, 'wb') as f:
            f.write(response.content)
        return profileImgName
    except Exception as e:
        logger.warning(e)
        return ""

#下载背景图片
def downloadBanner(bannerUrl):
    try:
        if not os.path.exists(basePath + '/images/bannerImg'):
                os.mkdir(basePath + '/images/bannerImg')
        bannerImgName = os.path.basename(bannerUrl)
        if not bannerImgName.endswith('jpg' or 'png'):
            bannerImgName = bannerImgName+".jpg"
        response = requests.get(bannerUrl, headers=headers)
        with open(basePath + '/images/bannerImg/%s'%bannerImgName, 'wb')as f:
            f.write(response.content)
        return bannerImgName
    except Exception as e:
        logger.warning("%s %s"%(bannerUrl, str(e)))