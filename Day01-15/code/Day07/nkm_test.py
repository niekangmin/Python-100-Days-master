# Project: Python-100-Days-master 
# File: nkm_test.py
# Author: nkm 276019
# Date: 2022/3/31 18:56
import os
import random
import sys

# -----------字符串--------------
import time

s1 = 'aa\\n'  # 转义
s2 = 'bb\n'
print(s1)
print(s2)

s1 = r'\'hello, world!\''
s2 = r'\n\\hello, world!\\\n'
print(s1, s2, end='')

str2 = 'abcd123456'
# 从字符串中取出指定位置的字符(下标运算)
print(str2[2]) # c
# 字符串切片(从指定的开始索引到指定的结束索引)
print(str2[2:5]) # c12
print(str2[2:]) # c123456
print(str2[2::2]) # c246
print(str2[::2]) # ac246
print(str2[::-1]) # 654321  cba
print(str2[-3:-1]) # 45

# 格式化输出
a, b = 5, 10
print('%d * %d = %d' %(a, b, a*b))
print('{0} * {1} = {2}'.format(a, b, a*b))
print(f'{a} * {b} = {a * b}')

# 内置字符串函数
str1 = ' hello, world! '
print(len(str1))
print(str1.upper())
print(str1.index('or'))
print(str1.split(', ')) #以', '拆分
print(str1.strip()) #去除左右两侧空格


# --------列表---------------
list1 = [1, 3, 5, 100]
# 添加元素
list1.append(200) # 添加
print(list1)
list2 = [300]
list1 += list2 # 相加
print(list1)
if 3 in list1:
    list1.remove(3) # 删除元素
    print(list1)
list1.pop(-1) # 通过位置删除元素
print(list1)
list1.clear()
print(list1)

# 列表切片操作
str4 = 'abcd'
list3 = ['1', '2', '3', 3, 2, 1]
list4 = list3[1:3]
print(list4)
print(str4[1:3]) # 切割
list5 = list3[:] # 复制列表
print(list5)
print(str4[::-1]) # 反向切片，倒转输出字符串
print(list5[::-1]) # 反向切片，倒序输出列表

# 列表排序
list6 = [1, 5, 9, 3, 2, 1]
list1 = ['orange', 'apple', 'zoo', 'internationalization', 'blueberry']
list2 = sorted(list1, key=len)
print(list2)
list7 = sorted(list6) # 从小到大顺序输出
print(list7)
list8 = sorted(list6, reverse=True) #倒序输出
print(list8)
for i in range(1, 3):
    print(i)

# 生成式
list9 = [x for x in range(1,10)]
print(list9)
print(sys.getsizeof(list9))

# 生成器
list10 = (x**2 for x in range(1,10))
print(sys.getsizeof(list10))
for var in list10:
    print(var, end=' ')
print()


# -------------元组----------
t = (1, 2, '聂康敏', True, False, 1.2345)
# t[1] = 222  # typeError 元组不能被修改
print(t)

list11 = list(t) # 元组转换成列表
list11[1] = 999  # 列表是可以修改的
print(list11)
t = ('王大锤', 20, True, '云南昆明') # 变量t重新引用了新的元组原来的元组将被垃圾回收
print(t)
t1 = tuple(list11) # 列表转换成元组
print(t1)

# ----------集合-----------
set1 = {1,2,3,4}
set2 = set(range(1,10))
print(set1,set2)
set1.add(5)
print(set1)
set2.update([1,12])
print(set2)
# 运算
print(set1 & set2) # 交集


# ---------字典----------
dict1 = {'1':1,'2':2,'3':'聂康敏',5:'aaa'}
print(dict1)
print(dict1[5])
for key in dict1:
    print(f'{key}:{dict1[key]}')

print(dict1.get('3'))

def main():
    content = '北京欢迎你为你开天辟地。。。。'
    while True:
        # 清理屏幕上的输出
        os.system('cls')  # os.system('clear')
        print(content)
        # 休眠200毫秒
        time.sleep(0.2)
        content = content[1:] + content[0]

def main1():
    all_chars = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    print(len(all_chars))
    s = ''
    for x in range(4):
        index = random.randint(0, len(all_chars)-1)
        s += all_chars[index]
    return s

if __name__ == '__main__':
    # main()
    print(main1())

