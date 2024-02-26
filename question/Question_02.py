# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : Question_02.py
# Time       ：2022年7月5日 22:04:33
# Author     ：sanmu 
# version    ：python 3.7
# email      ：349258449@qq.com 
"""

from ast import Break
from pywebio.output import *
from pywebio import start_server
from pywebio.input import *
from pywebio.output import *
from pywebio.pin import *
import numpy as np
np.set_printoptions(suppress=True)   #  取消科学计数法
import pandas as pd
pd.set_option('display.max_columns',10000,'display.max_rows',1000,'display.precision',2)

@use_scope('time', clear=True)
def Question_02(I):
    """实例002：“个税计算” """
    list02_1=[100000,100000,200000,200000,400000]
    rates=[0.1,0.075,0.05,0.03,0.015,0.01]
    money1=0
    I=int(I)
    for i in range(len(list02_1)):
        if I <= list02_1[i]:
            money1 += I*rates[i]
            I=0
            Break
        else:
            money1+= list02_1[i]*rates[i]
            I -= list02_1[i]
    money1 += I*rates[-1]
    QLog_02=style(put_text(f'需要发放奖金{pd.money1}元',position=-1),'color:red')

# numbers = 9000000
# f1=Question_02(numbers)
