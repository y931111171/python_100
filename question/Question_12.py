# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : Question_12.py
# Time       : 2022年10月3日 12:20:33
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

# 实例012：100到200的素数
#     题目 判断101-200之间有多少个素数，并输出所有素数。

def Question_12(number_x,number_y):
    '''100(x)到200(y)的素数 '''
    try:
        number_x=int(number_x)
        number_y=int(number_y)
        if number_x > number_y:
            put_text(f'{number_x}大于{number_y},请重新输入')
            return
    except:
        put_text('输入异常,请重新输入')
        return
    
    list_q12 = []
    for i in range(number_x,number_y):
        for j in range(2,int(i ** 0.5) + 1):
            if i % j == 0 :
                break
            else:
                if i not in list_q12:
                    list_q12.append(i)
                continue  
    put_text(f'{number_x} 到{number_y} 有{len(list_q12)}个素数，\n用列表展示值为：{list_q12}')
    return list_q12

if __name__ == '__main__':  
    Question_12(100,200)
    