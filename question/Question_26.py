# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : Question_26.py
# Time       : 2023年1月17日 18:51:33
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


# 实例026：递归求阶乘
#     题目 利用递归方法求5!。


def Question_26(num):
    '''实例026：递归求阶乘'''
    sum_max= num
    sum_txt = ''
    for i in range(num,0,-1):
    #    print(factorial(i))
        sum_txt += str(i)  + '*'
        if i == 1:
            sum_max *= 1
        else:
            sum_max *= (i-1)
        # print(sum_max)
    sum_txt= sum_txt[0:-1]
    # print(f'{sum_txt} = \n{sum_max} ')
    put_text(f'{sum_txt} = \n{sum_max} ')




if __name__ == '__main__':    
    Question_26(5)
    # Question_20()
