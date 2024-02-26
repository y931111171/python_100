# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : Question_18.py
# Time       : 2022年12月12日 15:20:33
# Author     : sanmu 
# version    : python 3.7
# email      : 349258449@qq.com 
"""
 
from ast import Pass, Return
import os
import sys


BAST_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BAST_DIR)



from pywebio.output import *
from pywebio.input import *
from pywebio.output import *
from pywebio.pin import *
from Q_class.Isit_number import *


# 实例018：复读机相加
#     题目 求s=a+aa+aaa+aaaa+aa…a的值，其中a是一个数字。例如2+22+222+2222+22222(此时共有5个数相加)，几个数相加由键盘控制。

def Question_18(num,count):
    '''实例018：复读机相加'''
    num = num
    count = count
    if count <= 0:
        put_text('输入重复值异常')
        return

    sum_18 = 0 
    for i in range(1,count+1):
        sum_18 += int(str(num)*i)
    put_text(sum_18)

if __name__ == '__main__':  
    Question_18(2,5)
    # Question_18()
