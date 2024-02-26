# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : Question_24.py
# Time       : 2023年1月17日 15:41:33
# Author     : sanmu 
# version    : python 3.7
# email      : 349258449@qq.com 
"""
 
from ast import Pass, Return
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


# 实例024：斐波那契数列II
#     题目 有一分数序列：2/1，3/2，5/3，8/5，13/8，21/13…求出这个数列的前20项之和。



def Question_24(num):
    '''实例024：斐波那契数列II
            题目 有一分数序列：2/1，3/2，5/3，8/5，13/8，21/13…求出这个数列的前20项之和。'''
    num_up = 1
    num_dow = 1
    sum_num = 0
    sum_txt = ''
    for i in range(num):
        num_up = num_up + num_dow   
        # print(num_up,num_dow)   #2  1 
        sum_num += num_up / num_dow
        sum_txt += str(num_up) + '/' + str(num_dow) + '+'
        num_dow += num_up     
    sum_txt = sum_txt[0:-1]

    # print(f'{sum_txt} = {str(sum_num)[0:9]}(保留小数)')
    put_text(f'{sum_txt} =  \n{str(sum_num)[0:9]}(保留小数)')


        # print(num_up+num_dow ,num_dow)   #2  1 
        # sum_num += num_up / num_dow
        # num_dow += num_up        # 2
        # if i == 0:
        #     print(2,1)
        #     sum_num = 2 / 1
        #     num_dow += num_up  
        # else:
        #     num_up = num_up+num_dow   
        #     print(num_up,num_dow)   #2  1 
        #     sum_num += num_up / num_dow
        #     num_dow += num_up        # 2


            

        




if __name__ == '__main__':  
   
    Question_24(5)
    # Question_20()
