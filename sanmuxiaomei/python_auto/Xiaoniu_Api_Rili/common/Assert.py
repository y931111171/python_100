# -*- coding: utf-8 -*-
# @Time    : 2020/3/21 下午10:14
# @Author  : Danny
# @File    : Assert.py


"""
封装Assert方法

"""
from common.Logs import Log
from common import Consts
import json


class Assertions:
    def __init__(self, def_name):
        # self.log = Log.MyLog()
        self.def_name = def_name
        log = Log(def_name)
        self.logger = log.Logger

    def assert_code(self, code, expected_code):
        """
        验证response状态码
        :param code:
        :param expected_code:
        :return:
        """
        try:
            assert code == expected_code
            self.logger.info("statusCode true, expected_code is %s, statusCode is %s " % (expected_code, code))
            # return True
        except:
            self.logger.error("statusCode error, expected_code is %s, statusCode is %s " % (expected_code, code))
            Consts.RESULT_LIST.append('fail')
            raise

    def assert_body(self, body, body_msg, expected_msg):
        """
        验证response body中任意属性的值
        :param body:
        :param body_msg:
        :param expected_msg:
        :return:
        """
        try:
            msg = body[body_msg]
            assert msg == expected_msg
            self.logger.info(
                "Response body msg == expected_msg, expected_msg is %s, body_msg is %s" % (expected_msg, body[body_msg]))
            # return True

        except:
            self.logger.error(
                "Response body msg != expected_msg, expected_msg is %s, body_msg is %s" % (expected_msg, body[body_msg]))
            Consts.RESULT_LIST.append('fail')

            raise

    def assert_in_text(self, body, expected_msg):
        """
        验证response body中是否包含预期字符串
        :param body:
        :param expected_msg:
        :return:
        """
        try:
            text = json.dumps(body, ensure_ascii=False)
            # print(text)
            assert expected_msg in text
            # return True

        except:
            self.logger.error("Response body Does not contain expected_msg, expected_msg is %s" % expected_msg)
            Consts.RESULT_LIST.append('fail')

            raise

    def assert_text(self, body, expected_msg):
        """
        验证response body中是否等于预期字符串
        :param body:
        :param expected_msg:
        :return:
        """
        try:
            assert body == expected_msg
            # return True

        except:
            self.logger.error("Response body != expected_msg, expected_msg is %s, body is %s" % (expected_msg, body))
            Consts.RESULT_LIST.append('fail')

            raise

    def assert_time(self, time, expected_time):
        """
        验证response body响应时间小于预期最大响应时间,单位：毫秒
        :param body:
        :param expected_time:
        :return:
        """
        try:
            assert time < expected_time
            # return True

        except:
            self.logger.error("Response time > expected_time, expected_time is %s, time is %s" % (expected_time, time))
            Consts.RESULT_LIST.append('fail')
            raise
