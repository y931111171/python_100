# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : Question_05.py
# Time       : 2022年8月17日 0:30:33
# Author     : sanmu 
# version    : python 3.7
# email      : 349258449@qq.com 
"""
import time
from pywebio.output import *
from pywebio import start_server
from pywebio.input import *
from pywebio.output import *
from pywebio.pin import *


@use_scope('time', clear=True)
def Question_05(number_one,number_two,number_three):
    '''____ 实例005: 三数排序 ____'''
    bubbleList=[int(number_one),int(number_two),int(number_three)]
    listLength = len(bubbleList)
    while listLength > 0:
        for i in range(listLength - 1):
            if bubbleList[i] > bubbleList[i+1]:
                bubbleList[i], bubbleList[i+1] = bubbleList[i+1], bubbleList[i]
        listLength -= 1
    put_text(bubbleList)
 
if __name__ == '__main__':
    Question_05(3, 4, 1)
    