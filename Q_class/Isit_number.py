# Is_number.py
# !/usr/bin/env python
# -*-coding:utf-8 -*-
from asyncio.windows_events import NULL
import os
import sys
from xmlrpc.client import NOT_WELLFORMED_ERROR
BAST_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BAST_DIR)


def isit_number(s):
    '''判断是否为数字'''
    try:
        float(s)
        return True
    except ValueError:
        pass
    try:
        import unicodedata
        unicodedata.numeric(s)
        return True
    except (TypeError, ValueError):
        pass
        return False

def isit_natural(s):
    '''判断是否是自然数'''
    try:
        if float(s) == 0:
            return True
        int(s)
        return True
    except ValueError:
        pass
    try:
        import unicodedata
        unicodedata.numeric(s)
        return True
    except (TypeError, ValueError):
        pass
        return False

def isit_Time(Time_hour=None,Time_minute=None,Time_second=None,Time_year=None,Time_month=None,Time_day=None):
    '''判断是否是时间,
        是 输出对应时间
        空 获取并输出当前时间
        不是则输出False'''
    from datetime import datetime
    #如果年月日值为空,输入当前时间
    month_list = [31,29,31,30,31,30,31,31,30,31,30,31]
    if Time_year is None:
        Time_year = datetime.strftime(datetime.now(),'%Y')
    if Time_month is None:
        Time_month = datetime.strftime(datetime.now(),'%m')  
    if Time_day is None:
        Time_day = datetime.strftime(datetime.now(),'%d')  
    if 0 < int(Time_month) <= 12 and 0 < int(Time_day) <= month_list[int(Time_month)-1]:
        Time_month = int(Time_month)
        Time_day =int(Time_day)
        # Time_year = int(Time_year)
    else:
        print('年月日不正确')
        return False
    try:
        if Time_hour == None and Time_minute == None and Time_second == None:
            print(f'______输入值为空，系统获取当前时间______')
            # Setting_TIME= datetime.now()
            mow_TIME=datetime.strftime(datetime.now(),'%H:%M:%S')  #只输出时分秒
            # Setting_TIME=datetime.strftime(Setting_TIME,'%Y-%m-%d %H:%M:%S')  #输出年月日时分秒
            # print(Setting_TIME)
            now_day = ("%04d-%02d-%02d " % (int(Time_year),int(Time_month),int(Time_day)))  #输出年月日
            Setting_TIME = now_day + mow_TIME
            # print(Setting_TIME)
            Setting_TIME = datetime.strptime(str(Setting_TIME), "%Y-%m-%d %H:%M:%S")
            # print(f'01 {Setting_TIME}')
            return Setting_TIME
            pass
        elif 0 <= int(Time_hour) <= 23 and 0 <= int(Time_minute) <= 59 and 0 <= int(Time_second) <= 59:            
            print(f'______输入时间值正常，即将输出结果______')
            Setting_TIME = "%04d-%02d-%02d %d:%d:%d" % (int(Time_year),int(Time_month),int(Time_day),int(Time_hour),int(Time_minute),int(Time_second))
            # print(f"02 {Setting_TIME}")   
            # print(type(Setting_TIME))
            Setting_TIME = datetime.strptime(Setting_TIME,"%Y-%m-%d %H:%M:%S")  #输出最终结果,格式化为时间
            # print(f'01 {Setting_TIME}')
            return Setting_TIME
            pass
        else:
            return False
            pass
    except ValueError:
        if isit_number(Time_hour)== False or isit_number(Time_minute)== False or isit_number(Time_second)== False:
            print(f'不允许输入非数字')
            return False
        elif isit_natural(Time_hour) == False or isit_natural(Time_minute)== False or isit_natural(Time_second) == False:
            print(f'不允许输入非整数')
            return False
        else:
            return False
    except (TypeError, ValueError):
        return False
        pass

def isit_list(s):
    '''判断是否是一个列表'''
    try:
        if type(s) == list:
            return True
            
    except ValueError:
        pass
    try:
        import unicodedata
        unicodedata.numeric(s)
        return True
    except (TypeError, ValueError):
        pass
        return False




if __name__ == "__main__":
    # print(isit_number('sas'))
    # print(isit_number('1.222'))   
    # print(isit_natural('1.222')) 
    # print(isit_natural('0')) 
    # print(isit_natural('0.00')) 
    # print(isit_natural('0.01')) 
    # print(isit_natural('-0.01'))
    print('_____________分割线0_______________')
    print(isit_Time('11','22','59','1','11','20'))
    # print('_____________分割线1_______________')
    # print(isit_Time('aa','22.22','60','aa','22.22','60'))
    # print('_____________分割线2_______________')
    # print(isit_Time('1.22','22.22','60','1.22','22.22','60'))
    # print('_____________分割线2_______________')
    # print(isit_Time())