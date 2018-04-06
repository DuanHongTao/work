# -*- coding:utf-8 -*-
import os
import subprocess


def stopmonkey():
    monkeycode = subprocess.Popen("adb shell ps | grep monkey",stdin=subprocess.PIPE,stdout=subprocess.PIPE)
    # print monkeycode.stdout.readline()
    a = monkeycode.stdout.readline()
    b = str(a).split()
    # print b
    try:
        print "[+]尝试停止MONKEY线程".decode("utf-8")
        print 'Monkey PID code:%s' % b[1]
        os.system("adb shell kill " + b[1])
    except:
        print "[!]没有找到MONKEY线程 或 无法停止MONKEY".decode("utf-8")


def getdevicesno():
    devicesno = subprocess.Popen("adb devices",stdin=subprocess.PIPE,stdout=subprocess.PIPE).stdout.read().split()
    return devicesno[4]


def takelog(log_name):
    result = os.system("adb pull /sdcard/"+log_name+" C:\Users\DHT\Desktop\MonkeyLog")
    if result == 1:
        print "[!]没有拉取到日志文件".decode("utf-8")
        # createfile = open(log_name+".txt","w+")
        # createfile.close()
    else:

        print "[+]已将文件拉去到桌面".decode("utf-8")

def main():
    openfile = open("D:\MyScript\DeleteLogStartMonkey\login_name.txt","r").readlines()
    deviceno = getdevicesno()
    for i in openfile:
        if deviceno in i.replace("\n", ""):
            stopmonkey()
            takelog(i.replace("\n", ""))

    raw_input(">>>>>press ENTER to exit")


if __name__ == '__main__':
    main()
