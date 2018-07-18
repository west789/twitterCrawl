import time
import datetime
import os
from loggingModule import logger

def runTask():
    logger.info(f"执行任务开始,时间开始于 {datetime.datetime.now()}")
    
    os.system("python main.py")

    logger.info(f"执行任务开始,时间结束于 {datetime.datetime.now()}")
def timeFun(sched_timedo):
    flag = 0
    while True:
        now = datetime.datetime.now()
        if sched_timedo < now < sched_timedo+datetime.timedelta(seconds=1):
            flag = 1
            time.sleep(1)
            runTask()
        else:
            if flag == 1:
                sched_timedo = sched_timedo+datetime.timedelta(hours=3)
                print(f"sched_timedo change:{sched_timedo}")
                flag = 0

if __name__ == "__main__":
    sched_timedo = datetime.datetime.now()+datetime.timedelta(seconds=10)
    print(f"执行Timer{sched_timedo}")
    timeFun(sched_timedo)       