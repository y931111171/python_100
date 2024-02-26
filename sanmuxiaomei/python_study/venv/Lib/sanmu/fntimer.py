# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : 20220525.py
# Time       ：2022/6/08 22:51
# Author     ：sanmu
# version    ：python 3.7
# email      ：349258449@qq.com
"""

import time
import fntimer from fn_timer

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








if __name__ == '__main__':
    from setuptools.command.easy_install import main
    main()