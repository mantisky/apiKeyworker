#! /usr/bin/env python
# -*- coding:utf-8 -*-
"""
功能：
作者：陈晨
时间：
"""
import json
import os
import re


# 读取json文件夹中所有用例
class TestGroup():
    def runner(self, json_dir):
        dir_list = os.listdir(json_dir)
        suite_list = [
            "{dir}/{suite}".format(dir=json_dir, suite=suite) for suite in dir_list if re.match(r'test_.*.json', suite)
        ]
        for sui in suite_list:
            with open(sui, 'r', encoding='utf-8') as suite:
                suite_json = json.dumps(json.load(suite))
                pattern = re.compile(r'''\"(\$\w+?)\"''')
                ls = pattern.findall(suite_json)
                ch_ls = ['suite_dict[{st}]'.format(st=ii.lstrip('$')) for ii in ls]
                ch_dict = dict(zip(ls, ch_ls))

                for key in ch_dict:
                    ch_pattern = re.compile(r'\{key}'.format(key=key))
                    ch_pattern.sub(ch_dict[key], suite_json)
                    print(suite_json)




if __name__ == "__main__":
    json_dir = "./json"
    group = TestGroup()
    group.runner(json_dir)