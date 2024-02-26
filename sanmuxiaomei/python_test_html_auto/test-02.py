#!/usr/bin/env python
# _*_ coding:utf-8 _*_
 
import unittest
import selenium
import time
from appium import webdriver
 
class MyTestCase(unittest.TestCase):
 
    @classmethod
    def setUp(self):
        # super().setUp()
        print('selenium version = ', selenium.__version__)
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '4.4'
        desired_caps['deviceName'] = '192.168.1.54:5555'
        desired_caps['appPackage'] = 'com. xx'
        #desired_caps['app'] = 'F:// debug.apk'
        desired_caps['appActivity'] = 'com.xx.MainActivity'
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
 
 
    def test_something(self):
        print('test_something click ------ ')
 
        # xpath：
        time.sleep(2)
        self.driver.find_element_by_android_uiautomator("newUiSelector().text(\"测试\")").click()
 
        # uiautomator -UiSelector：
        # name方式在1.5版本后已废除，能找到接口，不可使用，使用new UiSelector().text替代
        # self.driver.find_element_by_android_uiautomator("newUiSelector().text(\"测试\")").click()
 
        # class_name - child：
        # items =self.driver.find_elements_by_class_name('android.widget.TextView')
        # items[1].click()
 
        # id:
        time.sleep(2)
        self.driver.find_element_by_id('com.hisense.vod:id/test_video_resize').click()
 
    @classmethod
    def tearDown(self):
        time.sleep(5)
        print('tearDown ------ ')
        self.driver.quit()
 
 
if __name__ == '__main__':
    unittest.main()