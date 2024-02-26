# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : Question_08.py
# Time       : 2022年8月23日 23:30:33
# Author     : sanmu 
# version    : python 3.7
# email      : 349258449@qq.com 
"""
import os
import sys
BAST_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BAST_DIR)


from ast import Or
import numbers
from pickle import TRUE
import time
from pywebio.output import *
from pywebio.input import *
from pywebio.output import *
from pywebio.pin import *

from Q_class.Isit_number import isit_number

@use_scope('time', clear=True)
def Question_08(frist_number,last_number):
    '''____ 实例008：九九乘法表 ____'''
    if (isit_number(frist_number) == False) or (isit_number(frist_number) == False):
        put_text(f'第一个数{frist_number}或第二个数{last_number}不是自然数')
    elif frist_number == last_number:
        numbers_big = frist_number
        put_text(f'第一个数{frist_number}与第二个数一致{last_number}，\n输出{frist_number}*{last_number}乘法表')
        for i in range(1,numbers_big+1):
            text_number=''
            for j in range(1,i+1):
                text_number +=f'{j}*{i}={i*j}'+ '   '
            put_text(f'{text_number} \n')
        return
    elif frist_number > last_number:
        numbers_small = last_number
        numbers_big = frist_number
    
    else:
        numbers_small = frist_number
        numbers_big = last_number

    for i in range(numbers_small,numbers_big+1):
        text_number=''
        for j in range(numbers_small,i+1):
            text_number +=f'{j}*{i}={i*j}'+ '   '
        put_text(f'{text_number} \n')
        

if __name__ == '__main__':
    A1 = 6
    B1 = 3
    Question_08(A1,B1)
    