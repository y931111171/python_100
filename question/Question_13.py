# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : Question_12.py
# Time       : 2022年11月12日 12:20:33
# Author     : sanmu 
# version    : python 3.7
# email      : 349258449@qq.com 
"""
 
from ast import Pass, Return
import os
import sys

from cv2 import putText
from requests import put
BAST_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BAST_DIR)


from datetime import datetime
from pywebio.output import *
from pywebio.input import *
from pywebio.output import *
from pywebio.pin import *
from Q_class.Isit_number import *
import time

# 实例013：所有水仙花数
#     题目 打印出所有的"水仙花数"，所谓"水仙花数"是指一个三位数，其各位数字立方和等于该数本身。例如：153是一个"水仙花数"，因为153=1的三次方＋5的三次方＋3的三次方。


def Question_13(number_x,number_y):
    list_Narcissistic = []
    try:
        if 100<= int(number_x) <= 1000 and 100<= int(number_y) <=1000:
            # put_text('输入校验正确')
            if number_y > number_x:
                number_small = number_x
                number_big = number_y
            else: 
                number_small = number_y
                number_big = number_x
        else:
            put_text(f'{number_x,number_y}不是三位数')
            return
    except:
        put_text('输入错误')
        return

    for i in range(number_small,number_big):
        if (i//100)**3 + (i%100//10)**3 + (i%10)**3 == i :
            list_Narcissistic.append(i)
            # put_text(i)
        else:
            continue
    put_text(f'从数字 {number_x} 到数字 {number_y} 的所有水仙花数为：\n {list_Narcissistic}')   
    return list_Narcissistic
    
if __name__ == '__main__':  
    Question_13(999,111)
    # Question_13(101,200)
    