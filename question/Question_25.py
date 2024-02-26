# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : Question_25.py
# Time       : 2023年1月17日 18:41:33
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


# 实例025： 阶乘求和
#     题目 求1+2!+3!+…+20!的和。



def Question_25(num):
    '''实例025： 阶乘求和
         题目 求1+2!+3!+…+20!的和。'''
    sum_max = 0
    sum_txt =''
    for i in range(1,num+1):
    #    print(factorial(i))
        sum_txt += str(i) +'!' +'+'
        sum_max += factorial(i)
    # print(sum_max)
    sum_txt= sum_txt[0:-1]
    put_text(f'{sum_txt} = \n{sum_max} ')

            

        




if __name__ == '__main__':  
   
    Question_25(5)
    # Question_20()
