# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : Question_14.py
# Time       : 2022年11月12日 12:20:33
# Author     : sanmu 
# version    : python 3.7
# email      : 349258449@qq.com 
"""
 
from ast import Pass, Return
import os
import sys

from cv2 import putText
from requests import put
BAST_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BAST_DIR)


from datetime import datetime
from pywebio.output import *
from pywebio.input import *
from pywebio.output import *
from pywebio.pin import *
from Q_class.Isit_number import *
import time


# 实例014：分解质因数
#     题目 将一个整数分解质因数。例如：输入90,打印出90=2*3*3*5。


def Question_14(number):
    '''实例014：分解质因数'''
    text_141= str(number) + '='
    count = int(number)+1
    list14=[]
    text_14 = ''
    while count > 1:
        for i in range(2,int(number)+1):
            if number%i == 0:
                if number == i:
                    count=0
                    list14.append(i)
                    break
                else:
                    list14.append(i)
                    number = number/i
                    count-=1
                    break
            else:
                count-=1
                continue
    if len(list14) == 1:
        put_text('该数值为质数')
        return  False

    for i in range(0,len(list14)):
        if i ==len(list14)-1:
            text_14 += str(list14[i])
        else:
            text_14 += str(list14[i]) + "*"

    # put_text(list14)
    put_text(text_141+text_14)


if __name__ == '__main__':  
    Question_14(256)
    Question_14(2)
    Question_14(13)
    Question_14(1024)