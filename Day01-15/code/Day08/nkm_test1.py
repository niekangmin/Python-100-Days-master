# Project: Python-100-Days-master 
# File: nkm_test1.py
# Author: nkm 276019
# Date: 2022/4/6 20:11
from time import sleep


class Clock:
    def __init__(self, h, m, s):
        self._second = s
        self._min = m
        self._hour = h

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
    c = Clock(23, 59, 50)
    while True:
        print(c.show())
        sleep(1)
        c.run()
