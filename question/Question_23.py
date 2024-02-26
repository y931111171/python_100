# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : Question_23.py
# Time       : 2022年12月14日 09:41:33
# Author     : sanmu 
# version    : python 3.7
# email      : 349258449@qq.com 
"""
 
from ast import Pass, Return
import os
from re import I
import sys


BAST_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BAST_DIR)



from pywebio.output import *
from pywebio.input import *
from pywebio.output import *
from pywebio.pin import *
from Q_class.Isit_number import *

# 实例023：画菱形
#     题目 打印出如下图案（菱形）:
#     *
#    ***
#   *****
#  *******
#   *****
#    ***
#     *

def Question_23(num):
    '''实例023：画菱形'''
    if num % 2  == 0:
        put_text('输入值不是单数')
        return '输入值不是单数'
        print(K_STR)
        
        # num = int(num/2)
    else: 
        num = int((num+1)/2)

    K_STR = ''
    for i in range(num):
        L_str = ' ' * ((num+1)-i) + '*' * (i*2 + 1) + '\n'
        K_STR += L_str
        # if i == num -1:
        #     L_str = ' ' * ((num+1)-i) + '*' * (i*2 + 1) + '\n'
        #     K_STR += L_str
        # else:
        #     L_str = ' ' * ((num+1)-i) + '*' * (i*2 + 1) + '\n'
        #     K_STR += L_str
        #     continue

    for j in range(num-2,-1,-1):
        I_str = ' ' * ((num+ 1) - j) + '*' * (j*2 + 1) + '\n' + 
        K_STR += I_str

    # print(K_STR)
    put_text(K_STR, sep=' ', inline=False, scope=None)




if __name__ == '__main__':  

    Question_23(9)
    Question_23(8)
    # Question_20()
