# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : Question_10.py
# Time       : 2022年9月10日 20:30:33
# Author     : sanmu 
# version    : python 3.7
# email      : 349258449@qq.com 
"""
 
import os
import sys
BAST_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BAST_DIR)


from pickle import TRUE
from datetime import datetime
from pywebio.output import *
from pywebio.input import *
from pywebio.output import *
from pywebio.pin import *
from Q_class.Isit_number import *
import time

@use_scope('time', clear=True)
# def Question_09(Time9_hour,Time9_minute,Time9_second,Time9_year=None,Time9_month= None,Time9_day= None):
def Question_10(time_sleep):
    '''____  暂停x秒输出，并格式化当前时间。 ____'''
    try:
        time_sleep = int(time_sleep)
        put_text(f'请等待 {time_sleep}s 后输出当前时间')
        time.sleep(time_sleep)            
        time_now=datetime.strftime(datetime.now(),'%Y-%m-%d %H:%M:%S')
        # return time_now
        put_text(f'时间到,当前时间为{time_now}')
    except:
        put_text('输入错误')

  
if __name__ == '__main__':  
    Question_10('5')
    