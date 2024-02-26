# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : Question_20.py
# Time       : 2022年12月13日 14:41:33
# Author     : sanmu 
# version    : python 3.7
# email      : 349258449@qq.com 
"""
 
from ast import Pass, Return
import os
import sys


BAST_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BAST_DIR)



from pywebio.output import *
from pywebio.input import *
from pywebio.output import *
from pywebio.pin import *
from Q_class.Isit_number import *
# 实例020：高空抛物
#     题目 一球从100米高度自由落下，每次落地后反跳回原高度的一半；再落下，求它在第10次落地时，共经过多少米？第10次反弹多高？

def Question_20(high,count):
    '''实例020：高空抛物'''
    high_20 = high
    high_sum = 0
    count_20  = count
    for i in  range(count_20):
        high_sum += high_20
        high_20 /= 2
    put_text(f'从{high}落下,第{count}次落下时，共经过{high_sum} 米，第{count}次反弹高度{high_20}米')

if __name__ == '__main__':  
    Question_20(100,10)
    # Question_20()
