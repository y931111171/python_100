# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : Question_06.py
# Time       : 2022年8月19日 1:30:33
# Author     : sanmu 
# version    : python 3.7
# email      : 349258449@qq.com 
"""
from re import L
import time
from pywebio.output import *
from pywebio.input import *
from pywebio.output import *
from pywebio.pin import *


@use_scope('time', clear=True)
def Question_06(number):
    '''____ 实例006：斐波那契数列 ____'''
    '''斐波那契数列是一位意大利的数学家，他闲着没事去研究兔子繁殖的过程，研究着就发现，
    可以写成这么一个序列：1，1，2，3，5，8，13，21… 
    也就是每个数等于它前两个数之和。那么给你第 n 个数，问 F (n) 是多少。'''
    number_ZERO=[1]
    sum_number_ZERO = number_ZERO[0]
    for i in range(number-1):
        if i == 0:
            number_ZERO.append(1)
            sum_number_ZERO+=1
        else:
            number_ZERO.append(number_ZERO[i-1]+number_ZERO[i])
            sum_number_ZERO+= number_ZERO[i-1]+number_ZERO[i]
    # put_text(number_ZERO)
    put_text(f'第{number}个数的值为{number_ZERO[number-1]}')
    put_text(f'数列的和：{sum_number_ZERO}')
    put_text(f'这个数列是{number_ZERO}')




if __name__ == '__main__':
    Question_06(5)
    