#! /usr/bin/env python
# -*- coding:utf-8 -*-
"""
功能：实现关键字工具
作者：陈晨
时间：2019-03-04
"""
import requests
import pytest
import json

requests.packages.urllib3.disable_warnings()


# 封装requests
class Requests():
    def __init__(self, method, url, data, headers):
        pass


# 封装eval方法
class Eval():
    def __init__(self, code):
        pass


# 封装exec方法
class Exec():
    def __init__(self, code):
        pass


# 封装断言
class Assert():
    def __init__(self, type, args1, args2):
        pass


# 封装字典操作
class Dict():
    def __init__(self):
        pass


# 封装输出操作
class Output():
    def __init__(self, type, args):
        pass


# 解析用例套件
class Analyze():
    def __init__(self, suite_json):
        suite_json = json.dumps(json.load(suite))
        pattern = re.compile(r'''\"(\$\w+?)\"''')
        ls = pattern.findall(suite_json)
        ch_ls = ["suite_dict['{st}']".format(st=ii.lstrip('$')) for ii in ls]
        ch_dict = dict(zip(ls, ch_ls))

        print("##ch_dict##", ch_dict)
        for key in ch_dict:
            ch_pattern = re.compile(r'\{key}'.format(key=key))
            print('######', ch_dict[key])
            suite_json = ch_pattern.sub(ch_dict[key], suite_json)

        self.suite_json = suite_json
        print(self.suite_json)


if __name__ == "__main__":
    pass