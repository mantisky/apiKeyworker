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
        self.suite_args = {}
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
                    self.suite_args.update(case['args'])
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
                    return_value = step[2]
                    args_name = ['method', 'url', 'data', 'headers']
                    args_value = step[3]
                    quests_dict = dict(zip(args_name, args_value))

                    resp = self.kw_requests(quests_dict)
                    exec('{} = resp'.format(return_value))

                elif type == 'Eval':
                    return_value = step[2]
                    code = step[3]

                    resp = self.kw_eval(code)
                    exec('{} = resp'.format(return_value))

                elif type == 'Exec':
                    return_value = step[2]
                    code = step[3]

                    self.kw_exec(code)

                elif type == 'Assert':
                    return_value = step[2]
                    args_name = ['type', 'key', 'value']
                    args_value = step[3]
                    quests_dict = dict(zip(args_name, args_value))

                    self.kw_assert(quests_dict)

                elif type == 'AddToDict':
                    key = step[3][1]
                    value = step[3][2]

                    resp = self.kw_dict(type, key, value)
                    exec('{} = resp'.format(return_value))

                elif type == 'Print':
                    pass
                elif type == 'Log':
                    pass

    # 提取用例间传递的数据
    def extract(self, extract):
        suite_args = {}
        for key, value in extract:
            suite_args['{}'.format(key)] = eval(value)

        self.suite_args = suite_args



    # 封装requests
    def kw_requests(self, **kwargs):
        # return response
        pass

    # 封装eval方法
    def kw_eval(self, code):
        # return eval_value
        pass

    # 封装exec方法
    def kw_exec(self, code):
        pass

    # 封装断言
    def kw_assert(self, **kwargs):
        pass

    # 封装字典操作
    def kw_dict(self, type, key, value):
        # 返回操作后的字典
        pass

    # 封装输出操作
    def kw_output(self, tyep, value):
        pass


if __name__ == "__main__":
    pass