# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : Question_30.py
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


# 实例030：回文数
#     题目 一个5位数，判断它是不是回文数。
#     即12321是回文数，个位与万位相同，十位与千位相同。

def Question_30(num,len_num=5):
    ''' 实例030：回文数 '''

    if isit_natural(num) == False or len(str(num)) % 2 == 0 and num > 10000:
        # print("非数字！")
        put_text(f"数字 {num} 输入错误或非单数,请输入一个正整数：")
        return False
    if isit_number(len_num) == False :
        # print("非数字！")
        put_text(f" {len_num} 输入错误,请输入一个正整数：")
        return False
    elif len_num < 5 or len_num % 2 == 0:
        put_text(f"位数 {len_num} 输入错误,请输入位数大于 5 的单数")
        return False
    elif len(str(num)) < len_num:
        # print("输入长度小于五位数，请重新输入")
        put_text(f"输入长度小于{len_num}位数，请重新输入")
        return False
    else:
        num_txt = str(num)
        number_num = int(len_num/2)
        # if num_txt[-2] == num_txt[1]  and num_txt[-1] == num_txt[0]:
        #     put_text(f"该数字{num}:是回文数")
        #     return num       
        # else:
        #     put_text(f"该数字{num}:不是回文数")
        #     return False

        for i in range(number_num):
            if num_txt[-1-i] == num_txt[0+i]:
                continue
            else:
                put_text(f"该数字{num}:不是回文数")
                return False
        put_text(f"该数字{num}:是回文数")
            
if __name__ == '__main__':
    num = 12321
    Question_30(12321)
    Question_30(13321)
    Question_30(12321,4)   
    Question_30(12321,8)
    Question_30(1234321,7)
