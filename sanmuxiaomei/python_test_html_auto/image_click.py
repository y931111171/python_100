#图片识别点击功能

# _*_ coding:UTF-8 _*_
from PIL import Image ,ImageGrab
import time
from ctypes import *
import cv2
import Date_needed  #获取某个文件夹的文件生成一个列表
import pyautogui
import os

#获取某个文件夹中的文件生成一个列表
filePath = os.path.split(os.path.realpath(__file__))[0]
filePath_1 = '/002/003'
filePath_list = Date_needed.data_needed( filePath + filePath_1 )
#打印获取的列表
print(f'____________获取图片列表成功___________\n{filePath_list}\n____________')


number = 1

for i in filePath_list:
    filePath_0 = filePath+filePath_1 +'/'+i
    print(f'__________________读取文件地址____________\n{filePath_0}\n____________')
    im_screen = ImageGrab.grab() #调用ImageGrab库函数实现对当前主机画面截图并存储至im变量
    im_screen.save(r'SCREEN2.png') #将截图变量im_screen输出保存至工程路径下命名为SCREEN2.PNG
    source = cv2.imread(r'SCREEN2.png')  # 读取当前屏幕截图
    template = cv2.imread(filePath_0)  # 打开要点击的模板图片
    result = cv2.matchTemplate(source, template, cv2.TM_CCOEFF_NORMED)
    print(result)
    pos_start = cv2.minMaxLoc(result)[3]
    x = int(pos_start[0]) + int(template.shape[1] / 2)
    y = int(pos_start[1]) + int(template.shape[0] / 2)

    print(f'坐标点({x}, {y})') #打印返回坐标点
    pyautogui.move(x,y)#鼠标移动
    if number == 1:
        # pyautogui.click(x, y) #鼠标点击返回坐标点
         number = 0
    pyautogui.click(x, y) #鼠标点击返回坐标点
    os.remove("SCREEN2.png") #删除截图文件
    time.sleep(2)




