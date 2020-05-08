# -*- coding: utf-8 -*-

import json


# 将已编码的JSON字符串解码为Python对象
def decode_json():
    str = '["foo", {"bar":["baz", null, 1.0, 2]}]'
    print type(str)
    print str
    obj = json.loads(str)
    print obj
    print type(obj)


# 将Python对象编码成JSON字符串
def encode_json():
    obj = ["foo", {"bar": ["baz", None, 1.0, 2]}]
    print type(obj)
    print obj
    string_json = json.dumps(obj)
    print type(string_json)
    print string_json


if __name__ == "__main__":
    # decode_json()
    encode_json()
