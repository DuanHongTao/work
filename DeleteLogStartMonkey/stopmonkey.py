# -*- coding:utf-8 -*-
import os
import subprocess


def stopmonkey():
    monkeycode = subprocess.Popen("adb shell ps | grep monkey",stdin=subprocess.PIPE,stdout=subprocess.PIPE)
    a = monkeycode.stdout.readline()
    b = str(a).split()
    try:
        print "[+]尝试停止MONKEY线程"
        print b[1]
        os.system("adb shell kill " +b[1])
    except:
        print "[!]没有找到MONKEY线程 或 无法停止MONKEY"


def getdevicesno():
    devicesno = subprocess.Popen("adb devices",stdin=subprocess.PIPE,stdout=subprocess.PIPE).stdout.read().split()
    return devicesno[4]


def takelog(log_name):
    result = os.system("adb pull /sdcard/"+log_name+".txt C:\Users\DHT\Desktop\MonkeyLog")
    if result == 1:
        print "[!]没有拉取到日志文件"
        createfile = open(log_name+".txt","w+")
        createfile.close()
        i = 0
        while result == 1 and i < 10:
            print "尝试重新拉取第%s次".decode('utf-8') % (i+1)
            result = os.system("adb pull /sdcard/" + log_name + ".txt C:\Users\DHT\Desktop\MonkeyLog")
            i += 1
    else:
        print "[+]已将文件拉取到桌面MonkeyLog文件夹中"

def main():
    openfile = open("D:\MyScript\DeleteLogStartMonkey\login_name.txt","r").readlines()
    print openfile
    deviceno = getdevicesno()
    for i in openfile:
        if deviceno in i.replace("\n", ""):
            stopmonkey()
            takelog(i.replace("\n", ""))

    raw_input(">>>>>press ENTER to exit")

if __name__ == '__main__':
    main()
