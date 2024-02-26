
# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : 20220409_urllib_2.py
# Time       ：2022/7/29 11:12
# Author     ：sanmuxiaomei 
# version    ：python 3.7
# email      ：349258449@qq.com 
"""

'''PyWebIO使用'''

# -*- coding:utf-8 -*-

from importlib.resources import path
import time, os
from pywebio.input import NUMBER, TEXT
from pywebio.input import input, textarea, select, checkbox, radio, slider, actions, file_upload
from pywebio.input import input_group, input_update
from pywebio.output import put_text, put_markdown, put_buttons, put_scope, get_scope, put_info, put_warning, put_error, put_success, put_html, put_link, put_processbar, put_loading, put_code, put_table, put_button, put_buttons, put_image, put_file, put_tabs, put_collapse, put_scrollable, put_widget, put_row, put_column, put_grid
from pywebio.output import popup, toast, span, style
from pywebio import start_server



current_workspace = os.path.join(os.path.dirname(os.path.abspath(__file__)))
out_path = os.path.join(current_workspace, 'output')
'''pywebio中 Input组件介绍:
input(), 输入框
textarea(), 多行文本输入框
select(), 下拉选框
checkbox(), 多(复)选框
radio(), 单选框
slider(), 进度条
file_upload(), 文件上传按钮
actions(), 按钮
input_group(), 是以上几个组件的一个组合，我们可以认为是一个表单：Input group
input_update(), 动态更新组件的内容：Update attributes of input field
input_control(), 发送input命令，监听事件，验证输入项，返回结果

注意事项: 单个标签不能添加name属性，input_group中需要添加name属性。
'''
def user_output_component():
    '''标题测试1'''
    print(get_scope()) #return ROOT
    put_markdown('''# 这是一级标题''') #Output Markdown 
    text1='文本'
    text2='文本'
    put_text(text1, text2, sep='\n') #Output plain text 

    # Drop-down selection
    gift = select('Which gift you want?', ['keyboard', 'ipad'])
    put_text(gift) #输出到浏览器
    print(gift) #后台输出信息   
log_user_output_component = input(label='日志信息', type=TEXT, required=True, action=('Select', user_output_component))
print(log_user_output_component)

# from datetime import date,timedelta
# def select_date(set_value):
#     with popup('Select Date'): #popup 弹框
#         put_buttons(['Today'], onclick=[lambda: set_value(date.today(), 'Today')])
#         put_buttons(['Yesterday'], onclick=[lambda: set_value(date.today() - timedelta(days=1), 'Yesterday')])

# log_date = input(label='日志信息', type=TEXT, required=True, action=('Select', select_date))


    
    # ## 单个组件
    # def check_name(username):
    #     if len(username) < 1 or len(username) > 60:
    #         return 'username is illegality!'
    #     else:
    #         pass
        
    # def set_now_ts(set_value):
    #     set_value(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()))


    # username = input(label='姓名', type=TEXT, validate=check_name, required=True, placeholder='xx xx xx', help_text='输入提示语', action=('按钮', set_now_ts), datalist=['jack','zhangsan','lisi','qianwu'])
    # put_text(username) #输出到浏览器
    # print(username) #后台输出信息





## 单个组件

if __name__=="__main__":
    start_server(user_output_component, debug=True, port=8081)
    