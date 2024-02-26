# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : Question_17.py
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



# 实例017：字符串构成
#     题目 输入一行字符，分别统计出其中英文字母、空格、数字和其它字符的个数。


def Question_17(string):
    '''实例017：字符串构成'''
    str_string = string
    count_english=0
    count_num=0
    count_spa=0
    count_oth=0
    for i in range(len(str_string)):
        if string[i].isspace():
            count_spa+=1
        elif string[i].isdigit():
            count_num+=1
        elif string[i].isalpha():
            count_english+=1
        else:
            count_oth+=1
    put_text(f'空格数量: {count_spa}')
    put_text(f'数字数量: {count_num}')
    put_text(f'中英文数量: {count_english}')
    put_text(f'其他字符数量: {count_oth}')

if __name__ == '__main__':  
    Question_17('ssahjasdhjahzda啊大大阿松大阿松大阿萨,,,,,,,      撒大1241412苏打阿松大。。阿松大')
    # Question_17()
