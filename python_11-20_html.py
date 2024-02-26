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


# # Checkbox
# with use_scope('scope1'):  # 创建并进入scope 'scope1'
#     put_text('text1 in scope1')  # 输出内容到 scope1

# put_text('text in parent scope of scope1')  # 输出内容到 ROOT scope

# with use_scope('scope1'):  # 进入之前创建的scope 'scope1'
#     put_text('text2 in scope1')  # 输出内容到 scope1



# with use_scope('A'):
#     put_text('Text in scope A')

#     with use_scope('B'):
#         put_text('Text in scope B')

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
        Number_list=11
        for i in Question_list[10::]:
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

def Question11_app():
    put_scope('Q1',content=style(put_text(Q_data['Question11']['B1']),'color:red'))
    with use_scope('Q1', clear=False):
        from question.Question_11 import Question_11
        put_markdown(Q_data['Question11']['C1'])
        put_row([
            put_input('pin11_NUM_rabbit',type=NUMBER,label='请输入兔子有A对'),None,
            put_input('pin11_time_month',type=NUMBER,label='请输入月份X'),None,
            put_buttons([dict(label='计算结果', value='s', color='success')],lambda _: Question_11(
                pin.pin11_NUM_rabbit,pin.pin11_time_month
                )).style('padding-top:30px'),
            ])  

def Question12_app():
    # Questionzero = Question_12
    put_scope('Q1',content=style(put_text(Q_data['Question12']['B1']),'color:red')) #不能使用双引号
    with use_scope('Q1', clear=False):
        from question.Question_12 import Question_12
        put_markdown(Q_data['Question12']['C1'])
        put_row([
            put_input('pin12_number_x',type=NUMBER,label='请输入第一个数字'),None,
            put_input('pin12_number_y',type=NUMBER,label='请输入第二个数字'),None,
            put_buttons([dict(label='提交', value='s', color='success')],lambda _: Question_12(
                pin.pin12_number_x,pin.pin12_number_y
                )).style('padding-top:30px'),
            ])  



def Question13_app():
    put_scope('Q1',content=style(put_text(Q_data['Question13']['B1']),'color:red')) #不能使用双引号
    with use_scope('Q1', clear=False):
        from question.Question_13 import Question_13
        put_markdown(Q_data['Question13']['C1'])
        put_row([
            put_input('pin13_number_x',type=NUMBER,label='请输入第一个数字'),None,
            put_input('pin13_number_y',type=NUMBER,label='请输入第二个数字'),None,
            put_buttons([dict(label='获取数据', value='s', color='success')],lambda _: Question_13(
                pin.pin13_number_x,pin.pin13_number_y
                )).style('padding-top:30px'),
            ])  

def Question14_app():
    put_scope('Q1',content=style(put_text(Q_data['Question14']['B1']),'color:red')) #不能使用双引号
    with use_scope('Q1', clear=False):
        from question.Question_14 import Question_14
        put_markdown(Q_data['Question14']['C1'])
        put_row([
        put_input('pin14_number',type=NUMBER,label='请输入一个数字'),None,
        put_buttons([dict(label='提交', value='s', color='success')],lambda _: Question_14(
            pin.pin14_number
            )).style('padding-top:30px'),
        ])  

def Question15_app():
    put_scope('Q1',content=style(put_text(Q_data['Question15']['B1']),'color:red')) #不能使用双引号
    with use_scope('Q1', clear=False):
        from question.Question_15 import Question_15
        put_markdown(Q_data['Question15']['C1'])
        put_row([
        put_input('pin15_number',type=NUMBER,label='请输入分数'),None,
        put_buttons([dict(label='提交', value='s', color='success')],lambda _: Question_15(
            pin.pin15_number
            )).style('padding-top:30px'),
        ])  


def Question16_app():
    put_scope('Q1',content=style(put_text(Q_data['Question16']['B1']),'color:red')) #不能使用双引号
    with use_scope('Q1', clear=False):
        from question.Question_16 import Question_16
        put_markdown(Q_data['Question16']['C1'])
        put_row([
        put_input('pin16_year',type=NUMBER,label='请输入年份'),
        put_input('pin16_month',type=NUMBER,label='请输入月份'),
        put_input('pin16_day',type=NUMBER,label='请输入日期'),
        put_buttons([dict(label='提交', value='s', color='success')],lambda _: Question_16(
            pin.pin16_year,pin.pin16_month,pin.pin16_day
            )).style('padding-top:30px'),
        ])  


def Question17_app():
    put_scope('Q1',content=style(put_text(Q_data['Question17']['B1']),'color:red')) #不能使用双引号
    with use_scope('Q1', clear=False):
        from question.Question_17 import Question_17
        put_markdown(Q_data['Question17']['C1'])
        put_row([
        put_input('pin17_text',type=TEXT,label='请输入一段文字'),None,
        put_buttons([dict(label='提交', value='s', color='success')],lambda _: Question_17(
            pin.pin17_text
            )).style('padding-top:30px'),
        ])  



def Question18_app():
    put_scope('Q1',content=style(put_text(Q_data['Question18']['B1']),'color:red')) #不能使用双引号
    with use_scope('Q1', clear=False):
        from question.Question_18 import Question_18
        put_markdown(Q_data['Question18']['C1'])
        put_row([
        put_input('pin18_number',type=NUMBER,label='请输入数值'),
        put_input('pin18_count',type=NUMBER,label='请输入复读的次数'),
        put_buttons([dict(label='求和', value='s', color='success')],lambda _: Question_18(
            pin.pin18_number,pin.pin18_count
            )).style('padding-top:30px'),
        ])  

def Question19_app():
    put_scope('Q1',content=style(put_text(Q_data['Question19']['B1']),'color:red')) #不能使用双引号
    with use_scope('Q1', clear=False):
        from question.Question_19 import Question_19
        put_markdown(Q_data['Question19']['C1'])
        put_row([
        put_input('pin19_number',type=NUMBER,label='请输入数值'),
       
        put_buttons([dict(label='求和', value='s', color='success')],lambda _: Question_19(
            pin.pin19_number
            )).style('padding-top:30px'),
        ])


def Question20_app():
    put_scope('Q1',content=style(put_text(Q_data['Question20']['B1']),'color:red')) #不能使用双引号
    with use_scope('Q1', clear=False):
        from question.Question_20 import Question_20
        put_markdown(Q_data['Question20']['C1'])
        put_row([
        put_input('pin20_number',type=NUMBER,label='请输入起点高度'),
        put_input('pin20_count',type=NUMBER,label='请输入反弹的次数'),
        put_buttons([dict(label='求和', value='s', color='success')],lambda _: Question_20(
            pin.pin20_number,pin.pin20_count
            )).style('padding-top:30px'),
        ])




Main_app=[index,Question11_app,Question12_app,Question13_app,Question14_app,
Question15_app,Question16_app,Question17_app,Question18_app,Question19_app,Question20_app
]
# 标题名称
# set_env(title='python 100练',output_max_width='1000px', output_animation=True)

if __name__ == '__main__':
    # start_server(put_table,cdn=False, debug=True, port=8084)
    start_server(Main_app)






