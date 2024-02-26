# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : 20220407_urllib_1.py
# Time       ：2022/4/4 16:40
# Author     ：sanmuxiaomei 
# version    ：python 3.7
# email      ：349258449@qq.com 
"""





# from pywebio.input import input, FLOAT
# from pywebio.output import put_text

# def bmi():
#     height = input("请输入你的身高(cm)：", type=FLOAT)
#     weight = input("请输入你的体重(kg)：", type=FLOAT)

#     BMI = weight / (height / 100) ** 2

#     top_status = [(14.9, '极瘦'), (18.4, '偏瘦'),
#                   (22.9, '正常'), (27.5, '过重'),
#                   (40.0, '肥胖'), (float('inf'), '非常肥胖')]

#     for top, status in top_status:
#         if BMI <= top:
#             put_text('你的 BMI 值: %.1f，身体状态：%s' % (BMI, status))
#             break

# if __name__ == '__main__':
#     bmi()




# from pywebio import start_server
# from pywebio.input import input, FLOAT
# from pywebio.output import put_text

# def bmi():  # bmi() 函数内容不变
#     height = input("请输入你的身高(cm)：", type=FLOAT)
#     weight = input("请输入你的体重(kg)：", type=FLOAT)

#     BMI = weight / (height / 100) ** 2

#     top_status = [(14.9, '极瘦'), (18.4, '偏瘦'),
#                   (22.9, '正常'), (27.5, '过重'),
#                   (40.0, '肥胖'), (float('inf'), '非常肥胖')]

#     for top, status in top_status:
#         if BMI <= top:
#             put_text('你的 BMI 值: %.1f，身体状态：%s' % (BMI, status))
#             break


# import tornado.ioloop
# import tornado.web
# from pywebio.platform.tornado import webio_handler
# from pywebio import start_server
# from pywebio.input import input, FLOAT
# from pywebio.output import put_text



# class MainHandler(tornado.web.RequestHandler):
#     def get(self):
#         self.write("Hello, world")

# def bmi():  # bmi() 函数内容不变
#     height = input("请输入你的身高(cm)：", type=FLOAT)
#     weight = input("请输入你的体重(kg)：", type=FLOAT)

#     BMI = weight / (height / 100) ** 2

#     top_status = [(14.9, '极瘦'), (18.4, '偏瘦'),
#                   (22.9, '正常'), (27.5, '过重'),
#                   (40.0, '肥胖'), (float('inf'), '非常肥胖')]

#     for top, status in top_status:
#         if BMI <= top:
#             put_text('你的 BMI 值: %.1f，身体状态：%s' % (BMI, status))
#             break




# if __name__ == "__main__":
#     application = tornado.web.Application([
#         (r"/", MainHandler),
#         (r"/bmi", webio_handler(bmi)),  # bmi 即为上文计算BMI指数的函数
#     ])
#     application.listen(port=80, address='localhost')
#     tornado.ioloop.IOLoop.current().start()





# if __name__ == '__main__':
#     start_server(bmi, port=80)

# import yaml
# import beyond

# from Q_class.get_yaml import get_yaml_data
# Q_data = get_yaml_data("sanmuxiaomei\python_study\question\config.yal")

# print(Q_data['Question1']['A1'])
# print(Q_data['Question1']["B1"])
# print(Q_data['Question1']["C1"])




'''
from ast import With
import json
from cv2 import putText
from matplotlib.pyplot import pink

from pywebio import start_server
from pywebio.input import *
from pywebio.output import *
from pywebio.pin import *
from pywebio.session import set_env, info as session_info
from datetime import datetime
from sqlalchemy import collate
from Question_01 import Question_01


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
table_1 =[
    [span(put_markdown('## Section A'), col=4)],
    ['标题2', put_scope('A2', content=put_text('A2'))],  # hobby is initialized to coding
    ['标题3', put_scope('A3', content=put_text('A3'))],
    ['标题4', put_scope('A4', content=put_text('A4'))],
    ['标题5', put_scope('A5', content=put_text('A5'))],
    ['标题6', put_scope('A6', content=put_text('A6'))],
    ['标题7', put_scope('A7', content=put_text('A7'))]      
]

put_table(table_1)



with use_scope('A2', clear=True):
    put_text('A2-2')  # hobby is reset to Movie

# append Music, Drama to hobby
with use_scope('A3'):
    put_text('A3-1')
    put_text('Drama')

with use_scope('A4', clear=True):
    put_select('A4_1', options=['A4_2', 'B4_2', 'C_2'])



# insert the Coding into the top of the hobby
put_markdown('**加粗标题**', #名称加粗
 scope='A4',#指定域 
 position=0)



with use_scope('A5', clear=True):
    put_collapse('A5', style([
        put_text('text'),
        put_markdown('~~del这个长度有点长~~'),
    ], 'margin-left:20px'))



# 单个按钮
#put_button("click me", onclick=lambda: toast("Clicked"), color='success', outline=True)
# onclick= 可连接对应函数比如：partial(row_action, id=1)

def row_action(choice, id):
    put_text("你点击了某个按钮: %s,%s" % (choice,id))

def row_action2(id):
    put_text("你点击了某个按钮:,%s" % (id))

with use_scope('A6', clear=False):
    from functools import partial
    put_button(label ='这是一个按钮', onclick=partial(row_action2, id=2), color='dark', small=None, link_style=False, outline=False, scope=None, position=- 1)
    put_button(label ='Question_01', onclick=partial(Question_01, id=2), color='dark', small=None, link_style=False, outline=False, scope=None, position=- 1)

# "label":(str) 按钮标签,
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
with use_scope('A7', clear=False):
    # def row_action(choice, id):
    #     put_text("You click %s button with id: %s" % (choice, id))
    from functools import partial
    put_buttons([  
    dict(label=i, value=i, color=i)  
    for i in ['primary', 'secondary', 'success', 'danger', 'warning', 'info', 'light', 'dark']  
], onclick=partial(row_action, id=1))


if __name__ == '__main__':
    start_server(put_table, debug=True, port=9999)


'''

# !/usr/bin/env python
# -*-coding:utf-8 -*-
from ast import Return, With
from itertools import count
import json
from pickle import LIST
from tokenize import Number
from turtle import color
from cv2 import putText
from matplotlib.pyplot import pink

from pywebio import start_server
from pywebio.input import *
from pywebio.output import *
from pywebio.pin import *
from pywebio.session import set_env, info as session_info
from datetime import datetime
from sqlalchemy import collate
from functools import partial

# # 日志打印
# LOG_FORMAT = "%(asctime)s - %(levelname)s - %(filename)s"
# DATE_FORMAT = "%Y-%m-%d %H:%M:%S"
# formatter = logging.Formatter(fmt=LOG_FORMAT, datefmt=DATE_FORMAT)
# # 输出到控制台
# stream_handler = logging.StreamHandler()
# stream_handler.setFormatter(formatter)

# logger = logging.getLogger()
# logger.addHandler(stream_handler)




# @use_scope('time', clear=True)
# def show_time():
#     put_text(datetime.now())


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
# from Q_class.get_yaml import get_yaml_data
# Q_data = get_yaml_data("sanmuxiaomei\python_study\question\config.yaml")

# #生成一个问题列表
# Question_list= []
# for i in Q_data:
#     #g1 = [i.replace('"', '') for i in g1]  清除废弃字段
#     Question_list.append(Q_data[i]['B1'])
#     Question_list=[j.replace('_', '') for j in Question_list]
# print(Question_list)


# #获取问题配置文件
# from Q_class.get_yaml import get_yaml_data
# Q_data = get_yaml_data("sanmuxiaomei\python_study\question\config.yaml")

# #生成一个问题列表
# Question_list= []
# for i in Q_data:
#     #g1 = [i.replace('"', '') for i in g1]  清除废弃字段
#     Question_list.append(Q_data[i]['B1'])
#     Question_list=[j.replace('_', '') for j in Question_list]
# # print(Question_list)

# def task_1():
#     put_text('task_1')
#     put_buttons(['Go task 2'], [lambda: go_app('task_2')])

# def task_2():
#     put_text('task_2')
#     put_buttons(['Go task 1'], [lambda: go_app('task_1')])

# def index():
#     put_link('Go task 1', app='task_1')  # Use `app` parameter to specify the task name
#     put_link('Go task 2', app='task_2')

# # equal to `start_server({'index': index, 'task_1': task_1, 'task_2': task_2})`
# start_server([index, task_1, task_2])


# from pywebio import start_server
# from fastapi import FastAPI
# from pywebio.platform.fastapi import webio_routes
# import python_100_html

# app = FastAPI()

# @app.get("/app")
# def read_main():
#    return {"message": "Hello World from main app"}

# # `task_func` is PyWebIO task function
# app.mount("/tool", FastAPI(routes=webio_routes(python_100_html.index)))


# def Replace_list(list1):
#     str_list = ''
#     for i in list1:
#         if i =='[' or i == ']' or i=='\'':
#             continue
#         else:
#             str_list +=i
#     print(str_list)
#     print(type(str_list))  
#     str_list0= []
#     number = 0
#     count = 0
#     print(len(str_list))
#     for k  in str_list:
#         number +=1
#         if k == ',' or number== len(str_list):
#             str_list0.append(str_list[count:number])
#             count = number
#             continue
#         elif number == len(str_list):
#             str_list0.append(str_list[count:number])
#     return str_list0
#     # print(str_list0)
#     # print(type(str_list0))    





# if __name__ == '__main__':
#     Question_list1= "[12,222,333,'ssa','sdasda']"
#     Replace_list(Question_list1)


Question_list1= "['111','222',333,'aaa''bbb']"
Question_list2=[22,233,41,1]

# LIST1=eval(Question_list1)
# print(LIST1)
# LIST2=list2.extend(LIST1)

# print(LIST2)
from Q_class.Str_replace_list import Replace_list
list1 = Replace_list(Question_list1)
list2 = Replace_list(Question_list2)
list2=list2.extend(Question_list1)
print(list2)