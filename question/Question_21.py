# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : Question_21.py
# Time       : 2022年12月13日 15:41:33
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
# 实例021：猴子偷桃
#     题目 猴子吃桃问题：猴子第一天摘下若干个桃子，当即吃了一半，还不过瘾，又多吃了一个第二天早上又将剩下的桃子吃掉一半，又多吃了一个。以后每天早上都吃了前一天剩下的一半零一个。到第10天早上想再吃时，见只剩下一个桃子了。求第一天共摘了多少。


def Question_21(day,num):
    '''实例021：猴子偷桃'''
    day_21 = day
    number_21 = num
    for i in range(day_21-1):   #实际吃了九天
        number_21 += 1
        number_21 *= 2
    put_text(f'第一天摘了{number_21}个桃子')



if __name__ == '__main__':  
    Question_21(10,1)
    # Question_20()
