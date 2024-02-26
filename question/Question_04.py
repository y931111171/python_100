# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : Question_04.py
# Time       ：2022年8月16日 21:30:33
# Author     ：sanmu 
# version    ：python 3.7
# email      ：349258449@qq.com 
"""
import time
from pywebio.output import *
from pywebio import start_server
from pywebio.input import *
from pywebio.output import *
from pywebio.pin import *


@use_scope('time', clear=True)
def Question_04(year,month,day):
    '''实例004：当天是一年第几天'''
    '''输入某年某月某日，判断这一天是这一年的第几天？'''
    # a1=2008
    # a2='12'
    # a3='23'
    # f1=Read_day(a1,a2,a3)
    L = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    Number_day=0
    a = 4
    if year % a == 0:
        L[1]=29
        put_text('当前年份为闰年')
    else:
        put_text('当前年份不是闰年')
    if 0<int(month) <= 12 and 0<int(day) <= L[month-1]:
        None
    else:
        put_text('月份或日期有误')
        return
    for i in range(int(month)-1):
        Number_day = L[i]+Number_day
    Number_day= Number_day+ int(day)
    put_text(f'{year}年{month}月{day}日是这一年的第{Number_day}天')