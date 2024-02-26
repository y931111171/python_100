# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : Question_29.py
# Time       : 2023年1月17日 20:31:33
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


# 实例029：反向输出
#     题目 给一个不多于5位的正整数，
#     要求：一、求它是几位数，二、逆序打印出各位数字。

def Question_29(num,len_num=5):
    ''' 实例029：反向输出 '''
    if isit_number(num) == False:
        # print("非数字！")
        put_text(f"{num}输入错误,请输入一个正整数：")
        return False
    elif len(str(num)) > len_num:
        # print("输入长度大于五位数，请重新输入")
        put_text("输入长度大于{len_num}位数，请重新输入")

    else:
        number_len = len(str(num))
        number_txt = ''
        for i in range(1,number_len+1):
            number_txt += str(num)[-i]

        # print(f'正整数: {num} \n位数: {number_len} \n逆序打印值为: {number_txt}')
        put_text(f'正整数: {num} \n位数: {number_len} \n逆序打印值为: {number_txt}')



if __name__ == '__main__':
    num = 54321
    Question_29(num)

    Question_29('num')
    # Question_20()
