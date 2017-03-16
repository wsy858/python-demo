# _*_ coding:UTF-8 _*_

"""
Created on 2017/3/10 20:30
@author: evan
"""
import cookielib
import urllib2

url = r"http://www.w3school.com.cn/"

# 简单请求
def test_simple():
    print 'urllib2简单请求'
    response = urllib2.urlopen(url)
    code = response.getcode()
    content = response.read()
    print code
    print len(content)


def test_head():
    print 'urllib2请求头'
    request = urllib2.Request(url)
    request.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.106 Safari/537.36')
    response = urllib2.urlopen(request)
    code = response.getcode()
    content = response.read()
    print code
    print len(content)


def test_cookie():
    print 'urllib2 cookie'
    request = urllib2.Request(url)
    cj = cookielib.CookieJar()
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
    urllib2.install_opener(opener)
    response = urllib2.urlopen(request)
    code = response.getcode()
    content = response.read()
    print code
    print len(content)
    print cj


def test_proxy():
    proxy_handler = urllib2.ProxyHandler({'http': 'http://192.168.1.1:80/'})
    opener = urllib2.build_opener(proxy_handler, urllib2.HTTPHandler)
    request = urllib2.Request(url)
    request.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.106 Safari/537.36')
    f = opener.open(request, timeout=5.0)
    data = f.read()
    print 'data: ', data


if __name__ == "__main__":
    test_proxy()
