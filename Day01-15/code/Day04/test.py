# Project: Python-100-Days-master 
# File: nkm_test.py
# Author: nkm 276019
# Date: 2022/3/23 17:28

import random


# 1-100偶数求和
def test():
    sum = 0
    for i in range(2, 101, 2):
        sum = i + sum
    return sum


def test1():
    # 1-100随机数
    n = random.randint(1, 100)
    a = 0
    while True:
        a = a + 1
        x = int(input('请输入1-100的整数：'))
        if x < n:
            print('小了')
        elif x > n:
            print('大了')
        else:
            print('猜对了')
            break
    print('总共猜了%d' % a)
    if a > 7:
        print('智商有待考证哦')


if __name__ == '__main__':
    print('0-100中偶数之和：%d' % test())
    test1()