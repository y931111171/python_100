# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : 20220407_urllib_1.py
# Time       ：2022/4/4 16:40
# Author     ：sanmu 
# version    ：python 3.7
# email      ：349258449@qq.com 
"""


s=[1,2,3,4,5,"aaaj",[6,7,8,9,"asdfs"],"ae"]

for i in s:
    if type(i) is list:
        for j  in i:
            print(j)
    else:
        print(i)