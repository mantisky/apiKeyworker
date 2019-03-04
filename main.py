#! /usr/bin/env python
# -*- coding:utf-8 -*-
"""
功能：
作者：陈晨
时间：
"""

import os
import re
from tool import TestSuite


# 读取json文件夹中所有用例
class TestGroup():
    def __init__(self, json_dir):
        dir_list = os.listdir(json_dir)
        suite_list = [
            "{dir}/{suite}".format(dir=json_dir, suite=suite) for suite in dir_list if re.match(r'test_.*.json', suite)
        ]
        for sui in suite_list:
            with open(sui, 'r', encoding='utf-8') as suite:
                test_suite = TestSuite(suite)


if __name__ == "__main__":
    json_dir = "./json"
    group = TestGroup(json_dir)