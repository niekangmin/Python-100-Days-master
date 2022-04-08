# Project: Python-100-Days-master
# File: nkm_test1.py
# Author: nkm 276019
# Date: 2022/4/6 20:11
import json
import time

import requests as requests


def main():
    try:
        with open('致橡树.txt', 'r', encoding='utf-8') as f:
            # 全文输出
            print(f.read())
    except FileNotFoundError:
        print('无法打开指定的文件!')


def main1():
    try:
        with open('致橡树.txt', 'r', encoding='utf-8') as f:
            # 逐行输出
            for line in f:
                print(line, end='')
                time.sleep(0.5)
            print()
    except FileNotFoundError:
        print('无法打开指定的文件!')


def main2():
    try:
        with open('致橡树.txt', 'r', encoding='utf-8') as f:
            # 逐行添加到list
            lines = f.readlines()
            print(lines)
    except FileNotFoundError:
        print('无法打开指定的文件!')


def main3():
    try:
        with open('mm.jpg', mode='rb') as f:
            data = f.read()
            print(type(data))
        with open('mm1.jpg', mode='wb') as wf:
            wf.write(data)
    except Exception as e:
        print(e)
    print('图片拷贝完成')


def main4():
    mydict = {
        'name': '骆昊',
        'age': 38,
        'qq': 957658,
        'friends': ['王大锤', '白元芳'],
        'cars': [
            {'brand': 'BYD', 'max_speed': 180},
            {'brand': 'Audi', 'max_speed': 280},
            {'brand': 'Benz', 'max_speed': 320}
        ]
    }
    # 将Python对象处理成JSON格式的字符串
    print(json.dumps(mydict, ensure_ascii=False))
    try:
        with open('nkm.json', mode='w', encoding='utf-8') as sf:
            # 将Python对象按照JSON格式序列化到文件中
            json.dump(mydict, sf, ensure_ascii=False)
        with open('nkm.json', mode='r', encoding='utf-8') as sf1:
            print(sf1.read())

    except IOError as e:
        print(e)
    print('保存数据完成!')


def main5():
    # 天行数据的api
    resp = requests.get('http://api.tianapi.com/networkhot/index?key=def6d7a27c67de138c76e74ee5dee5bb')
    # 将文件中的JSON数据反序列化成对象
    try:
        with open('nkm1.json', 'w', encoding='utf-8') as sf:
            sf.write(resp.text)
        with open('nkm1.json', 'r', encoding='utf-8') as sf:
            data_dict = json.load(sf)
            print(type(data_dict))
            print(data_dict)
    except Exception as e:
        print(e)
    # 将字符串的内容反序列化成Python对象 dict
    data_model = json.loads(resp.text)
    print(data_model)
    for news in data_model['newslist']:
        print(news['title'])


if __name__ == '__main__':
    # main()
    # main1()
    # main2()
    # main3()
    # main4()
    main5()
