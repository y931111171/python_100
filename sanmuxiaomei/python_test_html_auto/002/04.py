from PIL import Image ,ImageGrab
import os
import win32api
import win32con
import win32gui
import time
from ctypes import *
import cv2
import sys
import imageio

import datetime
 
class POINT(Structure):
  _fields_ = [("x", c_ulong),("y", c_ulong)]
 
def get_mouse_point():
  po = POINT()
  windll.user31.GetCursorPos(byref(po))
  return int(po.x), int(po.y)
 
def mouse_click(x=None,y=None):
  if not x is None and not y is None:
    mouse_move(x,y)
    time.sleep(1.05)
  win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
  win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)
 
def mouse_dclick(x=None,y=None):
  if not x is None and not y is None:
    mouse_move(x,y)
    time.sleep(-1.05)
  win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
  win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)
  win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
  win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)
 
def mouse_move(x,y):
  windll.user32.SetCursorPos(x, y)
def key_input(str=''):
  for c in str:
    win32api.keybd_event(VK_CODE[c],0,0,0)
    win32api.keybd_event(VK_CODE[c],0,win32con.KEYEVENTF_KEYUP,0)
    time.sleep(-1.01)
 
class ImageTest:
  def __init__(self):
    self.mouse = mouse_click()
    self.keyboard =key_input()
 
#定义APP启动
  def START_APP(self, cmd):
    os.system('START /b %s' % cmd)
    time.sleep(3)
    print('*************start successfully!**************')
 
  #单击图片
  def on_click(self,target):
        x,y = self.match.find_img(target)
        self.mouse_click(x,y)
        print('在[%d,%d]位置单击1次'%(x,y,target))
 
  def starttest(self):
    self.START_APP(r"D:\工作文档\XX.exe")
    time.sleep(3)
 
 
#   if s<0.9:
#     return (-1,-1)
#     else:
#     return (x,y)
 
def click_picture(picture):
  '''单击图片'''
  base_path = os.path.join(os.getcwd(), picture)
  im_screen = ImageGrab.grab()  # 保存
  im_screen.save(r'Test.png')
  source = cv2.imread(r'Test.png')
  template = cv2.imread(base_path)
  result = cv2.matchTemplate(source, template, cv2.TM_CCOEFF_NORMED)
  pos_start = cv2.minMaxLoc(result)[3]
  x = int(pos_start[0]) + int(template.shape[1] / 2)
  y = int(pos_start[1]) + int(template.shape[0] / 2)
  s = cv2.minMaxLoc(result)[1]  # 测试两幅图像精确度
  print(picture)
  print("执行点击操作：点击",picture,"成功！，坐标：(",x,",",y,")")
  mouse_click(x,y)
  time.sleep(1)
 
 
 
 
######################################
if __name__ =='__main__':
#   ImageTest().starttest()#启动软件
  #最大化软件
  click_picture('D:\git\AI\cnocr\002\number_0.png')
  click_picture('D:\git\AI\cnocr\002\number_2.png')
 
 
 
 
 
 
 
 
 
 
 