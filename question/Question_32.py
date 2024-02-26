# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : Question_32.py
# Time       : 2023年1月18日 14:31:33
# Author     : sanmu 
# version    : python 3.7
# email      : 349258449@qq.com 
"""
 
from ast import Pass, Return
from math import factorial
import os
from re import I
from symbol import subscript
import sys

BAST_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BAST_DIR)



from pywebio.output import *
from pywebio.input import *
from pywebio.output import *
from pywebio.pin import *
from Q_class.Isit_number import *

# 实例032：反向输出II
#     题目 按相反的顺序输出列表的值。


def Question_32(list_0):
    ''' 实例032：列表反向输出II '''
    list_per = []
    list_0 = list(list_0)
    
    for i in range(len(list_0),0,-1):
        list_per.append(list_0[i-1])
    # print(list_per)
    put_text(f'{list_0} 反向输出为: {list_per}')

if __name__ == '__main__':
    num = [1,2,3,4,5,6,7,8,9]
    Question_32(num)



