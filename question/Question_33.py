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


def Question_33(list_33):
    ''' 实例033：列表转字符串 '''
    #list_33 = [1,2,3,4,5]
    if isit_list(list_33) == True:
        put_text(','.join(str(n) for n in list_33))
    else:
        put_text('输入的不是列表')
        return

if __name__ == '__main__':
    num = [1,2,3,4,5,6,7,8,9]
    Question_33(num)
    num = 123123
    Question_33(num)



