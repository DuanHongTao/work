# -*- coding:utf-8 -*-
import os
import subprocess
import time


def startmonkey(log_name):
    print '尝试启动Monkey'.decode('utf-8')
    try:
        res = os.popen('adb shell "monkey -c android.intent.category.LAUNCHER\
                        -c android.intent.category.MONKEY -c android.intent.category.DEFAULT\
                        -p com.sohu.newsclient  -p com.sohu.kan\
                        --ignore-crashes --ignore-timeouts --ignore-security-exceptions --ignore-native-crashes\
                        --monitor-native-crashes --pct-touch 90 --pct-motion 10 -v -v -v --hprof --throttle 1000\
                        18000000 > /sdcard/'+log_name+'.txt 2>&1"')
    except WindowsError:
        print 'Monkey启动失败'.decode('utf-8')


def getdevicesno():
    try:
        devicesno = subprocess.Popen("adb devices", stdin=subprocess.PIPE, stdout=subprocess.PIPE).stdout.read().split()
        return devicesno[4]
    except BaseException:
        print '请检查是否连接设备'.decode('utf-8')
        return False


def main():
    devices = getdevicesno()
    if devices:
        log_name = '%s_%s_%s' % (devices, time.strftime("%y-%m-%d_%H%M%S"), 'MonkeyLog')
        print str('本次的文件名为' + log_name).decode('utf-8')
        with open('D:\MyScript\DeleteLogStartMonkey\login_name.txt', 'r+') as f:
            f.write(log_name+".txt\n")
            try:
                print '记录完毕'.decode('utf-8')
            except:
                print '记录失败'.decode('utf-8')
        startmonkey(log_name)
        raw_input('>>>>>>>>>')

    # device_no = getdevicesno()
    # time_stamp = time.strftime("%y-%m-%d_%H%M%S")
    # create_device_name = "%s_monkey_%s" % (device_no, time_stamp)
    # print str("本次的文件名为:"+create_device_name).decode('utf-8')
    # try:
    #     f = open(r'D:\MyScript\DeleteLogStartMonkey\login_name.txt', "w+")
    #     r = f.read()
    #     if device_no in r and time_stamp in r:
    #         print "i am in here"
    #
    #     elif device_no in r and time_stamp not in r:
    #         a = re.sub('(?P<devicename>' + device_no + ')_monkey_(?P<time>.{15})', r'' + device_no + '_monkey_' + time_stamp + '', r)
    #         print "将之前的文件名变更为:%s" %a
    #         f.seek(0, 0)
    #         f.write(a)
    #
    #     elif r == "":
    #         print "文件名存储文本中没有其他的文件名"
    #         r = r + create_device_name
    #         f.seek(0, 0)
    #         f.write(r)
    #
    #     else:
    #         print "添加新的文件名：%s" % create_device_name
    #         r = r + "\n%s" % create_device_name
    #         print r
    #         f.seek(0, 0)
    #         f.write(r)
    # except:
    #     print "设备记录失败，请检查连接是否正常"
    #     os._exit(0)
    # f.close()
    # startmonkey(create_device_name)


if __name__ == '__main__':
    main()
