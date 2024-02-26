# !/usr/bin/env python
# -*-coding:utf-8 -*-
from ast import With
from cProfile import label
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
        Number_list=1
        for i in Question_list[0:10]:
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

def Question1_app():
    from functools import partial
    put_scope('Q1',content=style(put_text(Q_data['Question1']['B1']),'color:red'))
    with use_scope('Q1', clear=False):
        from question.Question_01 import Question_01
        # style(put_text(Q_data['Question1']['B1']),'color:red')
        put_text(Q_data['Question1']['C1'])
        put_text('    ')
        put_button(label ='点击运行结果', onclick=partial(Question_01, TUPLE1=(1,2,3,4)), color='success')


def Question2_app():
    from question.Question_02 import Question_02
    # with use_scope('Q1', clear=False):
    style(put_text(Q_data['Question2']['B1']),'color:red')
    put_markdown(Q_data['Question2']['C1'])
    put_text('    ')
    put_row([
    put_input('pin_name',type=NUMBER,label='请输入缴税金额'),None,
    put_buttons([dict(label='计算', value='s', color='success')],lambda _: Question_02(pin.pin_name)).style('padding-top:30px')
    # put_button(label ='点击运行结果', onclick=partial(Question_02), color='success', position=-1)
            ])

 
def Question3_app():
    # with use_scope('Q1', clear=True):
    from question.Question_03 import Question_03
    style(put_text(Q_data['Question3']['B1']),'color:red')
    put_markdown(Q_data['Question3']['C1'])
    put_text('    ')
    put_row([
        put_input('pin_add',type=NUMBER,label='请输入加数A'),None,
        put_input('pin_multiply',type=NUMBER,label='请输入乘数X'),None,
        put_buttons([dict(label='计算', value='s', color='success')],lambda _: Question_03(pin.pin_add,pin.pin_multiply)).style('padding-top:30px')
])


def Question4_app():  
    # with use_scope('Q4', clear=True):
    from question.Question_04 import Question_04
    style(put_text(Q_data['Question4']['B1']),'color:red')
    put_markdown(Q_data['Question4']['C1'])
    put_text('    ')
    put_row([
        put_input('pin_year',type=NUMBER,label='请输入年份'),None,
        put_input('pin_month',type=NUMBER,label='请输入月份'),None,
        put_input('pin_day',type=NUMBER,label='请输入日期'),None,
        put_buttons([dict(label='计算', value='s', color='success')],lambda _: Question_04(pin.pin_year,pin.pin_month,pin.pin_day)).style('padding-top:30px'),
    ])


def Question5_app():  
    # with use_scope('Q5', clear=True):
    from functools import partial
    from question.Question_05 import Question_05
    style(put_text(Q_data['Question5']['B1']),'color:red')
    put_markdown(Q_data['Question5']['C1'])
    put_text('    ')

    put_row([
        put_input('pin_one',type=NUMBER,label='请输入第一个数'),None,
        put_input('pin_two',type=NUMBER,label='请输入第二个数'),None,
        put_input('pin_three',type=NUMBER,label='请输入第三个数'),None,
        put_buttons([dict(label='排序', value='s', color='success')],lambda _: Question_05(pin.pin_one,pin.pin_two,pin.pin_three)).style('padding-top:30px'),
    ])

def Question6_app():  
    from question.Question_06 import Question_06
    style(put_text(Q_data['Question6']['B1']),'color:red')
    put_markdown(Q_data['Question6']['C1'])
    put_row([
        put_input('pin_number_06',type=NUMBER,label='请输入第一个数'),None,
        put_buttons([dict(label='排序', value='s', color='success')],lambda _: Question_06(pin.pin_number_06)).style('padding-top:30px'),
        ])   

def Question7_app():  
    from question.Question_07 import Question_07
    style(put_text(Q_data['Question7']['B1']),'color:red')
    put_markdown(Q_data['Question7']['C1'])
    put_row([
        put_input('pin_list_07_1',type=TEXT,label='请输入第一个数列'),None,
        put_input('pin_list_07_2',type=TEXT,label='请输入第二个数列'),None,
        put_buttons([dict(label='开始复制', value='s', color='success')],lambda _: Question_07(pin.pin_list_07_1,pin.pin_list_07_2)).style('padding-top:30px'),
        ])  

def Question8_app():  
    from question.Question_08 import Question_08
    style(put_text(Q_data['Question8']['B1']),'color:red')
    put_markdown(Q_data['Question8']['C1'])
    put_row([
        put_input('pin_number_frist',type=NUMBER,label='请输入第一个数'),None,
        put_input('pin_number_end',type=NUMBER,label='请输入第二个数'),None,
        put_buttons([dict(label='生成', value='s', color='success')],lambda _: Question_08(pin.pin_number_frist,pin.pin_number_end)).style('padding-top:30px'),
        ])  

def Question9_app():  
    from question.Question_09 import Question_09
    style(put_text(Q_data['Question9']['B1']),'color:red')
    put_markdown(Q_data['Question9']['C1'])
    put_row([
        put_input('pin9_year',type=NUMBER,label='请输入年'),None,
        put_input('pin9_month',type=NUMBER,label='请输入月'),None,
        put_input('pin9_day',type=NUMBER,label='请输入日'),None,
        put_input('pin9_hour',type=NUMBER,label='请输入时'),None,
        put_input('pin9_minute',type=NUMBER,label='请输入分'),None,
        put_input('pin9_second',type=NUMBER,label='请输入秒'),None,
        put_buttons([dict(label='生成', value='s', color='success')],lambda _: Question_09([
            pin.pin9_hour,pin.pin9_minute,pin.pin9_second,
            pin.pin9_year,pin.pin9_month,pin.pin9_day]
            )).style('padding-top:30px'),
        ])  

def Question10_app():  
    from question.Question_10 import Question_10
    style(put_text(Q_data['Question10']['B1']),'color:red')
    put_markdown(Q_data['Question10']['C1'])
    put_row([
        put_input('pin10_sleep',type=NUMBER,label='请输入需要暂停的秒数'),None,
        put_buttons([dict(label='生成', value='s', color='success')],lambda _: Question_10(
            pin.pin10_sleep
            )).style('padding-top:30px'),
        ])  


# "label":(str) 按钮标签,X``
#    "value":(object) 按钮值,
#    "type":(str, optional) 按钮类型,
#    "disabled":(bool, optional) 是否禁止选择,
#    "color":(str, optional) 按钮颜色


# 多个按钮按钮以及按钮样式put_text
# put_buttons([  
#     dict(label=i, value=i, color=i)  
#     for i in ['primary', 'secondary', 'success', 'danger', 'warning', 'info', 'light', 'dark']  
# ], onclick=put_text) 
# 例子
# put_markdown('**Coding**', scope='Q4', position=0)




Main_app=[index,Question1_app,Question2_app,
Question3_app,Question4_app,
Question5_app,Question6_app,
Question7_app,Question8_app,
Question9_app,Question10_app
]
# 标题名称
# set_env(title='python 100练',output_max_width='1000px', output_animation=True)

if __name__ == '__main__':
    # start_server(put_table,cdn=False, debug=True, port=8084)
    start_server(Main_app)






