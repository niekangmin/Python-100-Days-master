# Project: Python-100-Days-master 
# File: nkm_test1.py
# Author: nkm 276019
# Date: 2022/3/21 20:07

def test():
    grade = float(input("请输入分数："))
    if grade >= 90:
        grade = 'A'
    elif grade >= 80:
        grade = 'B'
    elif grade >= 70:
        grade = 'C'
    elif grade >= 60:
        grade = 'D'
    else:
        grade = 'E'
    print("分数等级：", grade)


def test2():
    a = float(input('a='))
    b = float(input('b='))
    c = float(input('c='))
    if a+b>c and a+c>b and b+c>a:
        print('周长：%f' % (a+b+c))
        p = (a + b + c) / 2
        area = (p * (p - a) * (p - b) * (p - c)) ** 0.5
        print('面积:%f' % area)
    else:
        print('不构成三角形')


if __name__ == '__main__':
    test()
    test2()