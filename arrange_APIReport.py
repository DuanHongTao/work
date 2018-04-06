# -*- coding:utf-8 -*-
import urllib
import time
import jenkins
import datetime
import os
import re
# 到Jenkins上抓job名字
server = jenkins.Jenkins('http://10.2.154.223:8080')
# 把所有的job名字复制给d，为什么叫d我也不知道，随便改
d = server.get_all_jobs()

foldername_time = time.strftime('%Y-%m-%d %H%M%S')
filepath = 'C:\Users\DHT\Desktop\API_Monitor_Arrange\%s\\' % foldername_time
pathexist = os.path.exists(filepath)
# 自动创建文件夹，判断文件夹是否存在，如果不存在就自动创建
if not False != pathexist:
    os.mkdir(filepath)
else:
    pass
# 获取job字典（也就是d）的name对应的值，用来组成下载路径
for i in d:
    # 只回去正式环境的文件
    if 'Formal' in i['name']:
        # 下载每个Formal job的BugReoirt
        week_BugReport = urllib.urlretrieve('http://10.2.154.223:8080/job/'
                                            + i['name'] +
                                            '/ws/Bug_Report.txt',
                                            filename=
                                            filepath
                                            + i['name'] +
                                            '_Bug_Report.txt')
# 遍历上面创建的文件夹里的文件，为读取文件内容使用
result = os.walk(filepath)
time_1 = datetime.datetime.now()
weekago = datetime.timedelta(days=7)
weektitle = "%s-%s" % ((time_1 - weekago).strftime('%m.%d'), time_1.strftime('%m.%d'))
print weektitle+"接口监控情况统计\n"
for a, b, c in result:
    for f in c:
        with open(a+f) as myF:
            # 找到该环境报错次数，打印出来，省的再去Jenkins上看了
            regex = re.findall('所在环境:.+:\d{1,10}?次', myF.read())
            if regex:
                print f + ':' + regex[0].decode('utf-8')
            else:
                print f+"接口本周没有监控到异常".decode('utf-8')
raw_input(">>>>>>>>>>>>")