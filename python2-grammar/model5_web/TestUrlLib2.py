# _*_ coding:UTF-8 _*_

"""
Created on 2017/3/10 20:30
@author: evan
"""
import cookielib
import urllib2

# 简单请求
url = "http://www.baidu.com/s?f=8&rsv_bp=1&rsv_idx=1&word=aa&tn=92751549_hao_pg";
response = urllib2.urlopen(url)
code = response.getcode()
content = response.read()
print  code
print  len(content)


request = urllib2.Request(url)
request.add_header('User-Agent', 'Mozilla/5.0')
response = urllib2.urlopen(request)
print  code
print  len(content)

cj = cookielib.CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
urllib2.install_opener(opener)
response = urllib2.urlopen(request)
print cj

