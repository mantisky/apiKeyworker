#! /usr/bin/env python
# -*- coding:utf-8 -*-
"""
功能：解析测试用例
作者：陈晨
时间：2019-03-04
"""

import re
import json


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



if __name__ == "__main__":
    pass