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

# with use_scope('C'):
#     put_text('Text in scope C')
#获取问题配置文件
from Q_class.get_yaml import get_yaml_data
Q_data = get_yaml_data("question\config.yaml")

#生成一个问题列表
Question_list= []
for i in Q_data:
    #g1 = [i.replace('"', '') for i in g1]  清除废弃字段
    Question_list.append(Q_data[i]['B1'])
    Question_list=[j.replace('_', '') for j in Question_list]
# print(Question_list)



# table_1 =[
#     [span(put_markdown('## Question_100'), col=4)],
#     [span(put_scope('left_scope'), row=100)],
#     # [Q_data['Question1']['A1'], put_scope('Q1', content=style(put_text('___实例002：“个税计算”___','color:red')))],  # hobby is initialized to coding 
#     [Q_data['Question1']['A1'], put_scope('Q1',content=style(put_text(Q_data['Question1']['B1']),'color:red'))],
#     # [Q_data['Question2']['A1'], put_scope('Q2', content=style(put_text(Q_data['Question2']['B1']),'color:red'))],
#     # [Q_data['Question3']['A1'], put_scope('Q3', content=style(put_text(Q_data['Question3']['B1']),'color:red'))],
#     # [Q_data['Question4']['A1'], put_scope('Q4', content=style(put_text(Q_data['Question4']['B1']),'color:red'))],
#     # [Q_data['Question5']['A1'], put_scope('Q5', content=style(put_text(Q_data['Question5']['B1']),'color:red'))],   
#  ]
# put_table(table_1)

# span(put_markdown('## Question_100'))
# span(put_scope('left_scope'))
# 将生成列表输出
def index():
    # put_table(table_1)
    put_markdown('## 三木 python_100 web练习列表')
    # put_scope('left_scope')
    with use_scope("left_scope",clear=False):
        # put_table(table_1)
        Number_list=21
        for i in Question_list[20:30]:
            link_app = 'Question'+ str(Number_list) +'_app'
            put_link(i,app=link_app)
            Number_list = Number_list + 1
            put_text('    ')#换行

# with use_scope("left_scope",clear=False):
#     for i in Question_list:
#         Number_list=1
#         link_app = 'Question0'+ str(Number_list) +'_app' 
#         put_link(i,app=link_app)
#         Number_list+=1
#         put_text('    ')#换行


# with use_scope('Q1', clear=False):
#     from question.Question_01 import Question_01
#     style(put_text(Q_data['Question1']['B1']),'color:red')
#     put_text(Q_data['Question1']['C1'])
#     put_text('    ')
#     put_button(label ='点击运行结果', onclick=partial(Question_01, TUPLE1=(1,2,3,4)), color='success')

def Question21_app():
    put_scope('Q1',content=style(put_text(Q_data['Question21']['B1']),'color:red'))
    with use_scope('Q1', clear=False):
        from question.Question_21 import Question_21
        put_markdown(Q_data['Question21']['C1'])
        put_row([
            put_input('pin21_day',type=NUMBER,label='请输入天数'),None,
            put_input('pin21_num',type=NUMBER,label='请输入当天剩余个数'),None,
            put_buttons([dict(label='计算结果', value='s', color='success')],lambda _: Question_21(
                pin.pin21_day,pin.pin21_num
                )).style('padding-top:30px'),
            ])  


def Question22_app():
    put_scope('Q1',content=style(put_text(Q_data['Question22']['B1']),'color:red'))
    with use_scope('Q1', clear=False):
        from question.Question_22 import Question_22
        put_markdown(Q_data['Question22']['C1'])
        put_row([
            put_buttons([dict(label='请求结果', value='s', color='success')],lambda _: Question_22(
            
                )).style('padding-top:30px'),
            ])  

def Question23_app():
    put_scope('Q1',content=style(put_text(Q_data['Question23']['B1']),'color:red'))
    with use_scope('Q1', clear=False):
        from question.Question_23 import Question_23
        put_markdown(Q_data['Question23']['C1'])
        put_row([
            put_input('pin23_num',type=NUMBER,label='请输入最大*号数量,请使用单数'),None,
            put_buttons([dict(label='请求结果', value='s', color='success')],lambda _: Question_23(
            pin.pin23_num
                )).style('padding-top:30px'),
            ])  

def Question24_app():
    put_scope('Q1',content=style(put_text(Q_data['Question24']['B1']),'color:red'))
    with use_scope('Q1', clear=False):
        from question.Question_24 import Question_24
        put_markdown(Q_data['Question24']['C1'])
        put_row([
            put_input('pin24_num',type=NUMBER,label='请输入最大*号数量,请使用单数'),None,
            put_buttons([dict(label='请求结果', value='s', color='success')],lambda _: Question_24(
            pin.pin24_num
                )).style('padding-top:30px'),
            ])  

def Question25_app():
    put_scope('Q1',content=style(put_text(Q_data['Question25']['B1']),'color:red'))
    with use_scope('Q1', clear=False):
        from question.Question_25 import Question_25
        put_markdown(Q_data['Question25']['C1'])
        put_row([
            put_input('pin25_num',type=NUMBER,label='请输入最大阶乘数值'),None,
            put_buttons([dict(label='请求结果', value='s', color='success')],lambda _: Question_25(
            pin.pin25_num
                )).style('padding-top:30px'),
            ])  

def Question26_app():
    put_scope('Q1',content=style(put_text(Q_data['Question26']['B1']),'color:red'))
    with use_scope('Q1', clear=False):
        from question.Question_26 import Question_26
        put_markdown(Q_data['Question26']['C1'])
        put_row([
            put_input('pin26_num',type=NUMBER,label='请输入需要进行阶乘的数'),None,
            put_buttons([dict(label='请求结果', value='s', color='success')],lambda _: Question_26(
            pin.pin26_num
                )).style('padding-top:30px'),
            ])  

def Question27_app():
    put_scope('Q1',content=style(put_text(Q_data['Question27']['B1']),'color:red'))
    with use_scope('Q1', clear=False):
        from question.Question_27 import Question_27
        put_markdown(Q_data['Question27']['C1'])
        put_row([
            put_input('pin27_num',type=TEXT,label='请输入需要进行阶乘的数'),None,
            put_buttons([dict(label='请求结果', value='s', color='success')],lambda _: Question_27(
            pin.pin27_num
                )).style('padding-top:30px'),
            ])  

def Question28_app():
    put_scope('Q1',content=style(put_text(Q_data['Question28']['B1']),'color:red'))
    with use_scope('Q1', clear=False):
        from question.Question_28 import Question_28
        put_markdown(Q_data['Question28']['C1'])
        put_row([
            put_input('pin28_num',type=TEXT,label='请输入需要进行阶乘的数'),None,
            put_input('pin28_age',type=NUMBER,label='请输入年龄'),None,
            put_buttons([dict(label='请求结果', value='s', color='success')],lambda _: Question_28(
            pin.pin28_num,pin.pin28_age
                )).style('padding-top:30px'),
            ])  

def Question29_app():
    put_scope('Q1',content=style(put_text(Q_data['Question29']['B1']),'color:red'))
    with use_scope('Q1', clear=False):
        from question.Question_29 import Question_29
        put_markdown(Q_data['Question29']['C1'])
        put_row([
            put_input('pin29_num',type=NUMBER,label='请输入需要处理的数'),None,
            put_input('pin29_len',type=NUMBER,label='请输入限制长度n,不输入默认为5'),None,
            put_buttons([dict(label='请求结果', value='s', color='success')],lambda _: Question_29(
            pin.pin29_num,pin.pin29_len
                )).style('padding-top:30px'),
            ])  

def Question30_app():
    put_scope('Q1',content=style(put_text(Q_data['Question30']['B1']),'color:red'))
    with use_scope('Q1', clear=False):
        from question.Question_30 import Question_30
        put_markdown(Q_data['Question30']['C1'])
        put_row([
            put_input('pin30_num',type=NUMBER,label='请输入需要处理的数'),None,
            put_input('pin30_len',type=NUMBER,label='请输入限制长度n,不输入默认为5'),None,
            put_buttons([dict(label='请求结果', value='s', color='success')],lambda _: Question_30(
            pin.pin30_num,pin.pin30_len
                )).style('padding-top:30px'),
            ])  

Main_app=[index,Question21_app,Question22_app,Question23_app,Question24_app,Question25_app,
Question26_app,Question27_app,Question28_app,Question29_app,Question30_app,]
# 标题名称
# set_env(title='python 100练',output_max_width='1000px', output_animation=True)

if __name__ == '__main__':
    # start_server(put_table,cdn=False, debug=True, port=8084)
    start_server(Main_app)






