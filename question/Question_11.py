# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : Question_11.py
# Time       : 2022年9月10日 21:30:33
# Author     : sanmu 
# version    : python 3.7
# email      : 349258449@qq.com 
"""
 
from ast import Pass
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
import time

#  C1: 题目 有一对兔子，从出生后第3个月起每个月都生一对兔子，
#     小兔子长到第三个月后每个月又生一对兔子，
#     假如兔子都不死，问每个月的兔子总数为多少？

# @use_scope('time', clear=True)
# def Question_09(Time9_hour,Time9_minute,Time9_second,Time9_year=None,Time9_month= None,Time9_day= None):
def Question_11(NUM_rabbit,time_month,born_month=3):
    ''' 养兔子  '''
    try:
        NUM_rabbit = int(NUM_rabbit)
        if int(time_month) < 3:
            put_text(f'输入 {time_month}月 时间太短')
            NUM_end_rabbit= NUM_rabbit
            put_text(f'{time_month}月后,兔子数数量为{NUM_end_rabbit}对')
            exit(0)
        else:
            time_month = int(time_month)
    except:
        put_text('输入不正确')
        pass
    NUM_end_rabbit = NUM_rabbit
    for i  in range(time_month//born_month ):
        NUM_end_rabbit =NUM_end_rabbit +  NUM_end_rabbit
    
    put_text(f'{time_month}月后,兔子数数量为{NUM_end_rabbit}对')


if __name__ == '__main__':  
    Question_11(3,7)
    