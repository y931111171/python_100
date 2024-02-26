# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : Question_27.py
# Time       : 2023年1月17日 19:31:33
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


# 例027：递归输出
#     题目 利用递归函数调用方式，将所输入的5个字符，以相反顺序打印出来。

# def fac(txt):
#     txt = txt[0:-1]

def Question_27(txt):
    ''' 例027:递归输出 '''
    txt_0 = txt = str(txt)
    sum_txt =''
    for i in range(len(txt)):
        sum_txt += txt[-1]
        # print(f'sum_txt:{sum_txt}')
        txt = txt[0:-1]
        # print(f'txt:{txt}')
    # print(f'{sum_txt}')
    # print(f'{txt_0} 递归输出 为:{sum_txt}')
    put_text(f'{txt_0} \n递归输出为:\n{sum_txt}')

if __name__ == '__main__':
    Question_27('lkjhg')
    # Question_20()
