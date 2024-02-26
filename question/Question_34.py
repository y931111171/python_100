# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : Question_34.py
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

# 实例034：调用函数
#     题目 练习函数调用。

def hello():
    print('Hello World!')
def helloAgain(strs_34):
    for i in range(int(strs_34)):
        hello()

def Question_34(strs_34):
    ''' 实例034：调用函数 '''    

    if strs_34 == 'hellow':
        hello()
    elif isit_natural(strs_34) == True and strs_34 > 0:
        helloAgain()
    else:
        print('输入错误')


if __name__ == '__main__':
    Question_34('hellow')
    Question_34(5)


