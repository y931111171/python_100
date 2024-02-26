# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : 20220609.py
# Time       ：2022/6/9 8:19
# Author     ：sanmu 
# version    ：python 3.7
# email      ：349258449@qq.com 
"""

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
@timeit
def my_func2(x):
    time.sleep(x)


my_func(3)
my_func2(1)