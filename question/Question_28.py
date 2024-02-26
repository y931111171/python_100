# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : Question_28.py
# Time       : 2023年1月17日 19:31:33
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


# 实例028：递归求等差数列
#     题目 有5个人坐在一起，问第五个人多少岁？他说比第4个人大2岁。
#     问第4个人岁数，他说比第3个人大2岁。问第三个人，又说比第2人大两岁。
#     问第2个人，说比第一个人大两岁。最后问第一个人，他说是10岁。请问第五个人多大？

def Question_28(num,age=10):
    ''' 实例028:递归求等差数列 '''
    age_2 = age
    for i in range(num):
        age_2 +=  2

    put_text(f'第{num}人年龄为:\n{age_2}')

if __name__ == '__main__':
    num = 5
    Question_28(num,10)
    # Question_20()
