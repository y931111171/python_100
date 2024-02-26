# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : Question_07.py
# Time       : 2022年8月19日 22:30:33
# Author     : sanmu 
# version    : python 3.7
# email      : 349258449@qq.com 
"""
from ast import IsNot, Return
from asyncio.windows_events import NULL
from re import L
import time
from pywebio.output import *
from pywebio.input import *
from pywebio.output import *
from pywebio.pin import *



@use_scope('time', clear=True)
def Question_07(Question_list1,Question_list2=[]):
    '''____ 实例007：copy ____'''

    if Question_list1 == [] or Question_list1 == '' or Question_list1== NULL:
        put_text(f'第一个列表值为空,结束会话') 
        return
    try:
        list1= eval(Question_list1)
        put_text(f'LIST_1:{list1_1}')
        list2= eval(Question_list2)
        put_text(f'LIST_2:{list2}')
    except:
        from Q_class.Str_replace_list import Replace_list
        list1= Replace_list(Question_list1)
        list2= Replace_list(Question_list2)     
    list2.extend(list1)
    put_text(f'将{Question_list1}插入到{Question_list2},\n获得的值为：{list2}')
    return list2

   
if __name__ == '__main__':
    list1_1= "['111','222',333,'aaa','bbb']"
    # put_text(f'LIST_1{list1_1}')
    list2_2='[22,233,41,1]'
    # put_text(list2_2)
    Question_07(list1_1,list2_2)

    