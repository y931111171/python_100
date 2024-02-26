#!/usr/bin/python
# -*- coding: UTF-8 _*_

import pytest
import json
import sys
import os
from common import Shell
from common.Request import RequestsHandler
from common.Logs import Log
from common.Yaml_Data import HandleYaml
from common.Retrun_Response import dict_style
from Conf.conf import *
import allure
from common import Assert
from common import Consts

handleyaml = HandleYaml()
yamldict = handleyaml.get_data()

# log = Log(__name__)
# logger = log.Logger

file = os.path.basename(sys.argv[0])
print(file)
log = Log(file)
logger = log.Logger


@allure.description("测试http://calapi.51jirili.com/feedBack/add接口")
@allure.testcase("http://calapi.51jirili.com/feedBack/add", "测试用例地址👇")
def test_rl_add():
    def_name = sys._getframe().f_code.co_name
    test_Assert = Assert.Assertions(def_name)
    logger.info("开始执行脚本%s:\n", def_name)
    # url = 'http://testcalapi.hellogeek.com/feedBack/add'
    url = server_ip('realse') + yamldict['test_rl_add']['url']
    r = RequestsHandler().post_Req(url=url, json=yamldict['test_rl_add']['json'],
                                   headers=yamldict['test_rl_add']['headers'])
    sting_response = r.content.decode()
    # json_response = dict_style(sting_response)
    # assert json_response['code'] == 0
    # try:
    #     assert json_response['code'] == 0
    #     logger.info("code状态码返回正确：%s ----> PASS", json_response['code'])
    # except Exception:
    #     logger.info("code状态码返回错误：%s ----> FAIL", json_response['code'])
    #
    # assert json_response['msg'] == '执行成功'
    # try:
    #     assert json_response['msg'] == '执行成功'
    #     logger.info("msg信息返回正确：%s ----> PASS", json_response['msg'])
    # except Exception:
    #     logger.info("msg信息返回错误：%s ----> FAIL", json_response['msg'])

    json_response = dict_style(sting_response)
    # json_response = json.loads(sting_response)
    test_Assert.assert_code(json_response['code'], 0)
    test_Assert.assert_body(json_response, 'msg', '执行成功')
    Consts.RESULT_LIST.append('pass')

