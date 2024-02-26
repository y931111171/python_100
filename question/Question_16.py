# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : Question_16.py
# Time       : 2022年12月12日 13:20:33
# Author     : sanmu 
# version    : python 3.7
# email      : 349258449@qq.com 
"""
 
from ast import Pass, Return
import os
import sys


BAST_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BAST_DIR)


from datetime import datetime
from pywebio.output import *
from pywebio.input import *
from pywebio.output import *
from pywebio.pin import *
from Q_class.Isit_number import *



# 实例016：输出日期
#     题目 输出指定格式的日期。


def Question_16(YEAR,MONTH,DAY):
    '''实例016：输出日期'''
    import datetime
    Q16_day = DAY
    Q16_month = MONTH
    Q16_YEAR = YEAR
    put_text(f'当前时间为：{datetime.date.today()}')    #年-月-日
    put_text(f'输入时间为：{datetime.date(Q16_YEAR,Q16_month,Q16_day)}')  #2333-03-03
    put_text(datetime.date.today().strftime('%d/%m/%Y'))  #日 /月 /年
    day=datetime.date(Q16_YEAR,Q16_month,Q16_day)  
    day=day.replace(year=day.year+22)
    put_text(f'22年后的这个时间为: {day}')

if __name__ == '__main__':  
    Question_16(2022,1,2)
    # Question_16()
