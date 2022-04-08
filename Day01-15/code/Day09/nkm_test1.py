# Project: Python-100-Days-master
# File: nkm_test1.py
# Author: nkm 276019
# Date: 2022/4/6 20:11
import datetime
from time import sleep


class Clock:
    def __init__(self, h, m, s):
        self._second = s
        self._min = m
        self._hour = h

    # 类方法，第一个参数约定名为cls，它代表的是当前类相关的信息的对象（类本身也是一个对象，有的地方也称之为类的元数据对象），可以用cls创建出一个对象
    @classmethod
    def now(cls):
        now_time = datetime.datetime.now().strftime('%H:%M:%S')
        list_time = now_time.split(':')
        # print(type(list_time))
        return cls(int(list_time[0]), int(list_time[1]), int(list_time[2]))

    def run(self):
        self._second += 1
        if self._second == 60:
            self._second = 0
            self._min += 1
            if self._min == 60:
                self._min = 0
                self._hour += 1
                if self._hour == 24:
                    self._hour = 0

    def show(self):
        return '%02d:%02d:%02d' % (self._hour, self._min, self._second)
        # print(f'{self._hour}:{self._min}:{self._second}')


if __name__ == '__main__':
    clock = Clock.now()
    while True:
        print(clock.show())
        sleep(1)
        clock.run()
