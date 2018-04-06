# -*- coding:utf-8 -*-


from multiprocessing import Process, freeze_support
import time
import BackToTimeline
import DelandStart


def main():
    p2 = Process(target=DelandStart.main)
    p1 = Process(target=BackToTimeline.main)
    p2.start()
    time.sleep(7200)
    p1.start()


if __name__ == '__main__':
    freeze_support()
    i = 0
    while i < 5:
        main()
        i += 1
        time.sleep(60)


