# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : Question_01.py
# Time       ：2022年7月5日 22:04:33
# Author     ：sanmu 
# version    ：python 3.7
# email      ：349258449@qq.com 
"""
from distutils.log import Log
import itertools
from pywebio.output import *
import logging
import info_log


@use_scope('time', clear=True)
def Question_01(TUPLE1):
    """实例001：数字组合"""
    tuple1=TUPLE1
    count1=0
    list_01=[]
    for i in itertools.permutations(tuple1,len(tuple1)):
        num=0
        # print(i)
        for j in range(len(i),0,-1):
            num += i[len(i)-j] * 10**(j-1)
        list_01.append(num)
        count1+=1
    Qlist_01=list_01

    QLog_01 =put_text( f'一共有{count1}个组合,分别是\n{Qlist_01}', position=0)

    # return  Qlist_01,QLog_01

# T=(1,2,3,4)
# f1=Question_01(T)
