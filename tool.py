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
import re

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
class TestSuite():
    def __init__(self, suite_json):
        suite_json = json.dumps(json.load(suite_json))
        pattern = re.compile(r'''\"(\$\w+?)\"''')
        ls = pattern.findall(suite_json)
        ch_ls = ["self.suite_args['{st}']".format(st=ii.lstrip('$')) for ii in ls]
        ch_dict = dict(zip(ls, ch_ls))

        for key in ch_dict:
            ch_pattern = re.compile(r'\{key}'.format(key=key))
            suite_json = ch_pattern.sub(ch_dict[key], suite_json)

        self.suite_json = json.loads(suite_json)
        print("--suite_json--\n", self.suite_json)

    # 运行用例套件
    def runner(self):
        suite_status = False
        for case in self.suite_json:
            if "config" in case:
                case = case['config']
                suite_status = case['status']
                if suite_status:
                    suite_name = case['name']
                    print("--执行suite--: ", suite_name)
                else:
                    print('--未执行, suite_status：{status}: '.format(status=suite_status))

            if "test" in case and suite_status:
                case = case['test']
                case_status = case['status']
                if case_status:
                    case_name = case['name']
                    print("--执行case--: ", case_name)
                    self.suite_args = case['args']
                    print("###suite_args###", self.suite_args)

                    step = case['step']
                    self.runstep(step)

                    extract = case['extract']
                    self.extract(extract)

                else:
                    print('--未执行case, case_status：{status}: '.format(status=case_status))
            else:
                pass

    # 执行用例步骤
    def runstep(self, casestep):
        i = 1
        for step in casestep:
            print('###step{i}###'.format(i=i), step)
            i += 1
            for ss in step:
                name = step[0]
                type = step[1]
                print('--step{i}: {name}--'.format(i=i, name=name))


                if type == 'Requests':
                    pass
                elif type == 'Eval':
                    pass
                elif type == 'Assert':
                    pass




    # 提取用例间传递的数据
    def extract(self, extract):
        suite_args = {}
        for key, value in extract:
            suite_args['{}'.format(key)] = eval(value)

        self.suite_args = suite_args




if __name__ == "__main__":
    pass