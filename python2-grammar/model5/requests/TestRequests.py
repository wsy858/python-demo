# -*- coding: utf-8 -*-
"""
http库requests使用
Created on 2016年11月9日
@author: evan
"""
import requests

# 请求和响应
r = requests.get("https://github.com/timeline.json")
print "r.status_code: ", r.status_code
print "r.encoding: ", r.encoding
print "r.text: ", r.text
print "r.json(): ", r.json()
print "r.content: ", r.content
print '\n'

# 二进制响应内容, 下载图片文件
r = requests.get("https://avatars3.githubusercontent.com/u/1089146?v=3&s=160")
f = open("d:/11.png", "wb+")
f.write(r.content)

# get请求, 传递参数
params = {"key1": "value1", "key2": "value2"}
r = requests.get("http://httpbin.org/get", params=params)
print r.url
print r.text
print "\n"

# post请求，传递表单参数
r = requests.post("http://httpbin.org/post", data=params)
print r.url
print r.text
