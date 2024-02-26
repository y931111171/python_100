# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : 20220525.py
# Time       ：2022/5/25 22:51
# Author     ：sanmuxiaomei 
# version    ：python 3.7
# email      ：349258449@qq.com
#python 100练习
"""
import time
from functools import wraps
import math

def Min_Number(number_start,number_end):
    '''计算从a至b的和'''
    # a=0
    # b=100
    # f1 = Min_Number(a,b)
    number_zero=0
    for i in range(number_start,number_end):
        number_zero= number_zero + i
    print(f'从{number_start}至{number_end}的和是{number_zero}')



def Nar_Number(number_start,number_end):
    """水仙花数"""
    # a=0
    # b=1000
    # f1=Nar_Number(a,b)
    a=100
    b=10
    c=3
    L=[]
    if number_start <100:
        number_start = 100

    for i in range(number_start,number_end):
        if (i//a)**c + (i% a//b)**c + (i% b)**c == i:
            L.append(i)
        else:
            continue
    print(L)
    return L



def Jou_Number(number_start,number_end):
    """打印1000以内的偶数"""
    # a=0
    # b=1000
    # f1=Jou_Number(a,b)
    Lji=[]
    Lou=[]
    a=2
    b=0

    for i in range(number_start,number_end):
        if i%a == b:
           Lou.append(i)
        else:
            Lji.append(i)
    print(Lou,Lji)
    return Lou,Lji




def TIME_Number(hour,minute,second):
    '''打印当天所有时间'''
    # a=60
    # b=60
    # c=60
    # f1=TIME_Number(a,b,c)
    TIME=[]
    for i in range(hour):
        for j in range (minute):
            for k in range(second):
                time_zer0=str(i)+":"+str(j)+":"+str(k)
                TIME.append(time_zer0)
    print(TIME)


def Read_day(year,month,day):
    '''输入某年某月某日，判断这一天是这一年的第几天？'''
    # a1=2008
    # a2='12'
    # a3='23'
    # f1=Read_day(a1,a2,a3)
    L = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    Number_day=0
    a = 4
    if year % a == 0:
        L[1]=29
    else:
        print('当前年份不是闰年')
    if int(month) <= 12 and int(day) <= 31:
        None
    else:
        print('月份或日期有误')
        return
    for i in range(int(month)-1):
        Number_day = L[i]+Number_day
    Number_day= Number_day+ int(day)
    print(f'{year}年{month}月{day}日是这一年的{Number_day}天')




import time
from functools import wraps

import math


import time

def fn_timer(func):
    """
    定义一个计算函数运行时间的装饰器（计算时间使用time模块实现）
    调用方法：@fn_timer
    """
    def count_time(*args,**kwargs):
        start_time=time.time()
        print(f'运行开始时间{start_time}')
        func(*args,**kwargs)
        end_time=time.time()
        print(f'运行结束时间{end_time}')
        print('函数运行的时间为:{:.5f}'.format(end_time-start_time))
    return count_time

@fn_timer
def Perfect_square(a,b):
    print('\n————————开始运行优化案例2————————————')
    '''实例003：完全平方数'''
    # 题目
    # 一个整数，它加上100后是一个完全平方数，再加上168又是一个完全平方数，请问该数是多少？
    # x +100 = n２   x + 268 = m２    m２-n２ = 168  m２ + n２ = 368 +2x
    #f1=Perfect_square(100,168)
    max = 0
    L = []

    while  (max+1)**2 - max*max <= b:
        max=max+1
    # print(f"{max}")
    for i in  range(a,(max+1)**2,1):
        if math.sqrt(i).is_integer() == True:
            x = math.sqrt(i) == int(i ** 0.5)
            y = math.sqrt(i + b) == int((i + b) ** 0.5)
        else:
            continue
        if x and y :
            L.append(i-a)
        else:
            continue
    print(f'完全平方数合集为{L}')

@fn_timer
def Perfect_square2(a,b):
    print('\n————————开始运行未优化案例2————————————')
    '''实例003：完全平方数'''
    # 题目
    # 一个整数，它加上100后是一个完全平方数，再加上168又是一个完全平方数，请问该数是多少？
    # x +100 = n２   x + 268 = m２    m２-n２ = 168  m２ + n２ = 368 +2x
    #f1=Perfect_square(100,168)
    max = 0
    L = []

    while  (max+1)**2 - max*max <= b:
        max=max+1
    # print(f"{max}")

    for i in  range(a,(max+1)**2,1):
        x = i ** 0.5 == int(i ** 0.5)
        y = (i + b) ** 0.5 == int((i + b) ** 0.5)
        if x and y :
            L.append(i-a)
        else:
            continue
    print(f'完全平方数合集为{L}')


# Perfect_square(100,168)
#
# Perfect_square2(100,168)


# import time
# from functools import wraps
#
#
# def fn_timer2(function):
#     @wraps(function)
#     def function_timer(*args, **kwargs):
#         t0 = time.time()
#         result = function(*args, **kwargs)
#         t1 = time.time()
#         print("Total time running %s: %s seconds" %
#                (function.func_name, str(t1 - t0))
#               )
#         return result
#
#     return function_timer



import time

def timeit(f):

    def wapper(x):
        start =time.time()
        ret = f(x)
        print(time.time() - start)
        return ret
    return wapper

@timeit
def my_func(x):
    time.sleep(x)

my_func(3)