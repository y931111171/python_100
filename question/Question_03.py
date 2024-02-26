# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : Question_03.py
# Time       ：2022年8月16日 1:30:33
# Author     ：sanmu 
# version    ：python 3.7
# email      ：349258449@qq.com 
"""
import math
from ast import Break
from pywebio.output import *
from pywebio import start_server
from pywebio.input import *
from pywebio.output import *
from pywebio.pin import *


@use_scope('time', clear=True)
def Question_03(a,b):
    '''实例003：完全平方数'''
    # 题目
    # 一个整数，它加上100后是一个完全平方数，再加上168又是一个完全平方数，请问该数是多少？
    # x +100 = n２   x + 268 = m２    m２-n２ = 168  m２ + n２ = 368 +2x
    #f1=Perfect_square(100,168)
    #print('\n————————开始运行优化案例2————————————')
    max = 0
    L = []

    while  (max+1)**2 - max*max <= b:
        max=max+1
    # print(f"{max}")
    for i in  range(a,(max+1)**2,1):
        if math.sqrt(i).is_integer() == True:
            x = math.sqrt(i) == int(i ** 0.5)
            y = math.sqrt(i + b) == int((i + b) ** 0.5)
        else:
            continue
        if x and y :
            L.append(i-a)
        else:
            continue
    if L==[]:
        put_text(f'没有这个数')
    else:
        put_text(f'完全平方数合集为{L}')