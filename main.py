# 导入相关包
from initConfig import init
from saveData import TwitterPip
from tweetInfo import getTweetsUser
from datetime import datetime

# 主函数


def main():
    # 用户配置初始化
    apiConfig = init()

    # 实例化对象
    twitterPip = TwitterPip()

    # 获取Tweeter账号信息
    for accountName in apiConfig[1]:
        getTweetsUser(apiConfig[0], accountName.strip(), twitterPip)
    twitterPip.close()


if __name__ == '__main__':
    starTime = datetime.now()
    print("程序开始运行")
    print("---------------")
    main()
    endTime = datetime.now()
    print("---------------")
    print("程序执行完毕，共耗时%s" % (endTime - starTime))
