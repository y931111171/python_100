# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : Question_31.py
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

# 实例031：字母识词
#     题目 请输入星期几的第一个字母来判断一下是星期几，
#     如果第一个字母一样，则继续判断第二个字母。
# 星期日 Sunday
# 星期一 Mondy
# 星期二 Tuesday
# 星期三 Wednesday
# 星期四 Thursday
# 星期五 Friday
# 星期六 Saturday


def Question_31(text):
    ''' 实例031：字母识词 '''
    L_WEEK = {'星期一':'Mondy', '星期二':'Tuesday','星期三':'Wednesday','星期四':'Thursday','星期五':'Friday','星期六':'Saturday','星期日':'Sunday'}
    if len(text) < 5:
        put_text(f'{text} 输入字符少于5')
    elif text[:1] == L_WEEK['星期一'][:1] :
        put_text(f'{text} 为:星期一')
    elif text[:1] == L_WEEK['星期三'][:1] :
        put_text(f'{text} 为:星期三')
    elif text[:1] == L_WEEK['星期五'][:1] :
        put_text(f'{text} 为:星期五')
    elif text[:2] == L_WEEK['星期二'][:2] :
        put_text(f'{text} 为:星期二')        
    elif text[:2] == L_WEEK['星期四'][:2] :
        put_text(f'{text} 为:星期四')     
    elif text[:2] == L_WEEK['星期六'][:2] :
        put_text(f'{text} 为:星期六') 
    elif text[:2] == L_WEEK['星期日'][:2] :
        put_text(f'{text} 为:星期日')       
    else:
        put_text(f'{text} 输入异常')

if __name__ == '__main__':
    num = 12321
    Question_31(12321)



