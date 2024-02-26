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


@allure.description("测试http://calapi.51jirili.com/dream/hotDream?num=10接口")
@allure.testcase("http://calapi.51jirili.com/dream/hotDream?num=10", "测试用例地址👇")
def test_dream_hotDream():
    def_name = sys._getframe().f_code.co_name
    test_Assert = Assert.Assertions(def_name)
    logger.info("开始执行脚本%s:\n", def_name)
    url = server_ip('realse') + yamldict['test_dream_hotDream']['url']
    r = RequestsHandler().get_Req(url=url, params=yamldict['test_dream_hotDream']['params'],
                                  headers=yamldict['test_dream_hotDream']['headers'])
    sting_response = r.content.decode()
    json_response = dict_style(sting_response)
    # json_response = json.loads(sting_response)
    test_Assert.assert_code(json_response['code'], 0)
    test_Assert.assert_body(json_response, 'msg', '执行成功')
    Consts.RESULT_LIST.append('pass')