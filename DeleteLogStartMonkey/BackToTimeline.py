# -*- coding:utf-8 -*-

import os

import time

from multiprocessing import freeze_support

import DelandStart
import stopmonkey


def backtotimeline():
    # 退到新闻端的activity
    while True:
        target = r'channel.intimenews.activity.NewsTabActivity'
        phoneDesktop = 'activities.LauncherActivity'
        act = os.popen('adb shell dumpsys activity activities | findstr "mFocusedActivity"')
        result = act.read()
        if target in result or phoneDesktop in result:
            if target in result:
                print '在客户端内'
                os.system("adb shell input tap 650 1800")
                break
            elif phoneDesktop in result:
                print "在手机桌面上"
                break
        else:
            os.system("adb shell input keyevent 4")
        time.sleep(0.4)
    # 点击狐友tab



def main():
    # 等待半个小时运行一次，需要加上停止monkey的命令
    # time.sleep(5)
    stopmonkey.main()
    backtotimeline()


if __name__ == '__main__':
    main()
