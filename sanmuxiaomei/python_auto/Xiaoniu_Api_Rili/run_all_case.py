#!/usr/bin/python
# -*- coding: UTF-8 _*_

import time
import os
import sys
from common.Logs import Log
import pytest
from common import Shell
import allure
from common.emails import mail


if __name__ == "__main__":
    file = os.path.basename(sys.argv[0])
    log = Log(file)
    logger = log.Logger
    # 运行单个文件 pytest.main(['../test_case/test_login.py']) 运行多个文件 pytest.main(['../test_case/test_login_getVar.py',
    # '../test_case/test_login.py']) 运行整个目录 pytest.main(['../test_case', '--html=../report/report.html'])
    # logger.info("开始执行脚本") >pytest E:\project\Xiaoniu_Api_Rili\Run\run_all_case.py
    # --alluredir=E:\\project\\Xiaoniu_Api_Rili\\allure-results\\ allure generate report -o report\\allure-reports\\
    try:
        print("开始执行脚本")
        logger.info("==================================" + time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()) + "===================================")
        pytest.main(['E:\\project\\Xiaoniu_Api_Rili\\test_case', "--alluredir", "./report/reportallure/"])
        # pytest.main(['E:\\project\\Xiaoniu_Api_Rili\\test_case', '--alluredir',
        # 'E:\\project\\Xiaoniu_Api_Rili\\report\\reportallure'])
        # logger.info("脚本执行完成")
        print("脚本执行完成")
    except Exception as e:
        logger.error("脚本批量执行失败！", e)
        print("脚本批量执行失败！", e)

    try:
        shell = Shell.Shell()
        cmd = 'allure generate %s -o %s --clean' % ('./report/reportallure/', './report//reporthtml/')
        # logger.info("开始执行报告生成")
        print("开始执行报告生成")
        shell.invoke(cmd)
        # logger.info("报告生成完毕")
        print("报告生成完毕")
    except Exception as e:
        print("报告生成失败，请重新执行", e)
        # logger.error("报告生成失败，请重新执行", e)
        # log.error('执行用例失败，请检查环境配置')
        raise

    time.sleep(5)
    mail()
