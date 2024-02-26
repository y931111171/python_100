# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : Question_22.py
# Time       : 2022年12月13日 16:41:33
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

# 实例022：比赛对手
#     题目 两个乒乓球队进行比赛，各出三人。甲队为a,b,c三人，乙队为x,y,z三人。已抽签决定比赛名单。有人向队员打听比赛的名单。a说他不和x比，c说他不和x,z比，请编程序找出三队赛手的名单。


def Question_22(team_a = ['a','b','c'], team_b = ['x','y','z']):
    '''实例022：比赛对手'''
    team_a22 = team_a
    team_b22 = team_b
    a = set(team_b22)
    b = set(team_b22)
    c = set(team_b22)
    c -= set(('x','z'))
    a -= set('x')
    for i in a:
        for j in b:
            for k in c:
                if len(set((i,j,k)))==3:
                    put_text(f'a 对战 {i} , b 对战 {j},c 对战 {k}')


if __name__ == '__main__':  
    a = ['a','b','c']
    b = ['x','y','z']

    Question_22(a,b)
    # Question_20()
