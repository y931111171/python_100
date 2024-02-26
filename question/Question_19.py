# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : Question_19.py
# Time       : 2022年12月13日 09:01:33
# Author     : sanmu 
# version    : python 3.7
# email      : 349258449@qq.com 
"""
 
from ast import Pass, Return
import os
import sys


BAST_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BAST_DIR)



from pywebio.output import *
from pywebio.input import *
from pywebio.output import *
from pywebio.pin import *
from Q_class.Isit_number import *


# 实例019：完数
#     题目 一个数如果恰好等于它的因子之和，这个数就称为"完数"。例如6=1＋2＋3.编程找出1000以内的所有完数（注意因子去重）。

# def Question_19(num):
#     '''实例019：完数'''

    # for k in range(2, num + 1):
    #     number = k
    #     count = int(number)+1
    #     list19=[1]        
    #     list19_sum =0
    #     list19_mul = 1
    #     while count > 1:
    #         for i in range(2,int(number)+1):
    #             if number%i == 0:
    #                 if number == i:
    #                     count=0
    #                     list19.append(i)
    #                     break
    #                 else:
    #                     list19.append(i)
    #                     number = number/i
    #                     count-=1
    #                     break
    #             else:
    #                 count-=1
    #                 continue
    #     # print(list19)  #打印分解质因数
    #     for i in list19:
    #         list19_sum += i
    #         list19_mul *= i
    #     print(list19_sum,list19_mul)  #打印分解质因数
    #     if list19_sum == list19_mul:
    #         print(f"{k} 是完数")
    #     else:
    #         continue

def factor(num):
 
    target=int(num)
    res=set()   #使用集合保存数据，可筛除重复因子
    for i in range(1,num):
        if num%i==0:
            res.add(i)
            res.add(num/i)
    return res

def  Question_19(count):
    '''实例019：完数'''
    for i in range(2,count+1):
        if i==sum(factor(i))-i:
            put_text(f'{i} 是完数')
        else:
            continue
if __name__ == '__main__':  
    Question_19(1000)
    # Question_19()
