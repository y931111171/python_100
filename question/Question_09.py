# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : Question_09.py
# Time       : 2022年8月23日 23:30:33
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

# @use_scope('time', clear=True)
# def Question_09(Time9_hour,Time9_minute,Time9_second,Time9_year=None,Time9_month= None,Time9_day= None):
def Question_09(time_list):
    '''____ 实例009：指定时间(TIME)输出 ____'''
    Time9_hour=time_list[0]
    Time9_minute=time_list[1]
    Time9_second=time_list[2]
    try:
        Time9_year=int(time_list[3])
    except:
        Time9_year = None
    try:
        Time9_month= int(time_list[4])
    except:
        Time9_month = None
    try:
        Time9_day= int(time_list[5])
    except:
        Time9_day = None
    
    setting_time = isit_Time(Time9_hour,Time9_minute,Time9_second,Time9_year,Time9_month,Time9_day)
    # print(type(setting_time))

    now_time =  datetime.strptime(str(datetime.now())[0:-7],"%Y-%m-%d %H:%M:%S")
    if type(setting_time) == bool :
        print(f'输入非法')
        put_text(f'输入非法')
        pass

    elif setting_time  > now_time :
        
        Difference_value = setting_time - now_time
        print(f'等待{Difference_value.seconds}秒执行')
        put_text(f'输入时间为{setting_time}比当前时间{now_time}大，等待{Difference_value.days}天{Difference_value.seconds}秒执行')
        pass
        # time.sleep(Difference_value)
    else:
        print(f'立即执行')
        put_text(f"输入时间为{setting_time}比当前时间{now_time}小，立即执行")
        pass


if __name__ == '__main__':
    A1 = "a2"
    B1 = 40
    c1 = 56
    D1 =11 
    D2 = 22
    D3 = 33
    # Question_09(A1,B1,c1)
    # Question_09(D1,D2,D3)
    Question_09([D1,D1,D1,D1,D1,D1])
    