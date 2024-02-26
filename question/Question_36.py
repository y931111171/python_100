# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : Question_36.py
# Time       : 2023年1月18日 14:31:33
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

# 实例036：算素数
#     题目 求100之内的素数。


def Question_36(num):
    ''' 实例036：算素数 '''
    list_num = []
    # for i in range(2,num+1):
    #     for j in range(2,i+1):
    #         if i == 2:
    #             list_num.append(i)
    #         elif  i % j == 0 and j != i:
    #             break
    #         elif j == i:
    #             if i not in list_num:    
    #                 list_num.append(i)
    #             else:
    #                 continue
    #         else:
    #             continue
    # count = 0
    for i in range(2,num):
        count = 0
        for j in range(2,i):
            if i  % j ==0 :
                count +=1
                break
                # print(f'{i}不是素数')
            else:
                continue
                # print(f'{i}是素数')
        if count == 0 :
            print(f'{i}是素数')
            list_num.append(i)
        else:
            print(f'{i}不是素数')
    # print(i)
    put_text(f'1-{num}之间的素数集合为：\n{list_num}')
if __name__ == '__main__':

    Question_36(100)



