# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : Question_15.py
# Time       : 2022年12月12日 10:20:33
# Author     : sanmu 
# version    : python 3.7
# email      : 349258449@qq.com 
"""
 
from ast import Pass, Return
import os
import sys

BAST_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BAST_DIR)


from datetime import datetime
from pywebio.output import *
from pywebio.input import *
from pywebio.output import *
from pywebio.pin import *
from Q_class.Isit_number import *



# 实例015：分数归档
#     题目 利用条件运算符的嵌套来完成此题：学习成绩>=90分的同学用A表示，60-89分之间的用B表示，60分以下的用C表示。


def Question_15(Score):
    '''实例015：分数归档'''
    Score_number = Score
    if Score_number >= 90:
        put_text('A')
    elif Score_number >= 60:
        put_text('B')
    else:
        put_text('C')


if __name__ == '__main__':  
    Question_15(100)
    Question_15(2)
    Question_15(13)
    Question_15(60)