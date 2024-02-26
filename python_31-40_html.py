# !/usr/bin/env python
# -*-coding:utf-8 -*-
from ast import With
from cProfile import label
from ctypes.wintypes import PRECT
import json
from pickle import LIST
from tokenize import Number
from turtle import color
from matplotlib.pyplot import pink

from pywebio import start_server
from pywebio.input import *
from pywebio.output import *
from pywebio.pin import *
from pywebio.session import set_env, info as session_info
from datetime import datetime
from sqlalchemy import collate
import logging
import info_log
from functools import partial

from question.Question_09 import Question_09

# 日志打印
LOG_FORMAT = "%(asctime)s - %(levelname)s - %(filename)s"
DATE_FORMAT = "%Y-%m-%d %H:%M:%S"
formatter = logging.Formatter(fmt=LOG_FORMAT, datefmt=DATE_FORMAT)
# 输出到控制台
stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)

logger = logging.getLogger()
logger.addHandler(stream_handler)




@use_scope('time', clear=True)
def show_time():
    put_text(datetime.now())

from Q_class.get_yaml import get_yaml_data
Q_data = get_yaml_data("question\config.yaml")

#生成一个问题列表
Question_list= []
for i in Q_data:
    #g1 = [i.replace('"', '') for i in g1]  清除废弃字段
    Question_list.append(Q_data[i]['B1'])
    Question_list=[j.replace('_', '') for j in Question_list]
# print(Question_list)

 
# span(put_markdown('## Question_100'))
# span(put_scope('left_scope'))
# 将生成列表输出
def index():
    # put_table(table_1)
    put_markdown('## 三木 python_100 web练习列表')
    # put_scope('left_scope')
    with use_scope("left_scope",clear=False):
        # put_table(table_1)
        Number_list=31
        for i in Question_list[30::]:
            link_app = 'Question'+ str(Number_list) +'_app'
            put_link(i,app=link_app)
            Number_list = Number_list + 1
            put_text('    ')#换行


def Question31_app():
    put_scope('Q1',content=style(put_text(Q_data['Question31']['B1']),'color:red'))
    with use_scope('Q1', clear=False):
        from question.Question_31 import Question_31
        put_markdown(Q_data['Question31']['C1'])
        put_row([
            put_input('pin31_day',type=TEXT,label='请输入英文'),None,
            put_buttons([dict(label='计算结果', value='s', color='success')],lambda _: Question_31(
                pin.pin31_day
                )).style('padding-top:30px'),
            ])  

def Question32_app():
    put_scope('Q1',content=style(put_text(Q_data['Question32']['B1']),'color:red'))
    with use_scope('Q1', clear=False):
        from question.Question_32 import Question_32
        put_markdown(Q_data['Question32']['C1'])
        put_row([
            put_input('pin32_text',type=TEXT,label='请输入列表'),None,
            put_buttons([dict(label='计算结果', value='s', color='success')],lambda _: Question_32(
                pin.pin32_text
                )).style('padding-top:30px'),
            ])  

def Question33_app():
     put_scope('Q1',content=style(put_text(Q_data['Question33']['B1']),'color:red'))
     with use_scope('Q1', clear=False):
        from question.Question_33 import Question_33
        put_markdown(Q_data['Question33']['C1'])
        put_row([
            put_input('pin33_text',type=TEXT,label='请输入一个列表'),None,
            put_buttons([dict(label='返回结果', value='s', color='success')],lambda _: Question_33(
                pin.pin33_text
                )).style('padding-top:30px'),    
                 ])  
def Question34_app():
    put_scope('Q1',content=style(put_text(Q_data['Question34']['B1']),'color:red'))
    with use_scope('Q1', clear=False):
        from question.Question_34 import Question_34
        put_markdown(Q_data['Question34']['C1'])
        put_row([   
            put_input('pin34_text',type=TEXT,label='请输入hellow'),None,
            put_buttons([dict(label='返回结果', value='s', color='success')],lambda _: Question_34(
                pin.pin34_text
                )).style('padding-top:30px'),
            ])


def Question35_app():
    put_scope('Q1',content=style(put_text(Q_data['Question35']['B1']),'color:red'))
    with use_scope('Q1', clear=False):
        from question.Question_35 import Question_35
        put_markdown(Q_data['Question35']['C1'])
        put_row([
            put_input('pin35_text',type=NUMBER,label='请输入列表'),None,
            put_buttons([dict(label='返回结果', value='s', color='success')],lambda _: Question_35(
                pin.pin35_text
                )).style('padding-top:30px'),
            ])
def Question36_app():  
    put_scope('Q1',content=style(put_text(Q_data['Question36']['B1']),'color:red'))
    with use_scope('Q1', clear=False):
        from question.Question_36 import Question_36
        put_markdown(Q_data['Question36']['C1'])
        put_row([
            put_input('pin36_text',type=NUMBER,label='请输入一个整数X'),None,
             put_buttons([dict(label='返回结果', value='s', color='success')],lambda _: Question_36(
                pin.pin36_text
                )).style('padding-top:30px'),
            ])

Main_app=[index,Question31_app,Question32_app,Question33_app,Question34_app,Question35_app,Question36_app,
]
# 标题名称
# set_env(title='python 100练',output_max_width='1000px', output_animation=True)

if __name__ == '__main__':
    # start_server(put_table,cdn=False, debug=True, port=8084)
    start_server(Main_app)






