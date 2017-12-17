# -*- coding: utf-8 -*-

# from __future__ import print_function
import re

from bs4 import BeautifulSoup

html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""

soup = BeautifulSoup(html_doc)
# print(soup.prettify())

print '获取全部的连接'
for link in soup.find_all('a'):
    print link.name, link['href'], link.get_text()
    # print link.get('href')

print '获取Elsie的连接'
link_node = soup.find('a', id='link1')
print link_node.name, link_node['href'], link_node.get_text()


print '正则匹配'
link_node = soup.find('a', href=re.compile(r'ill'))
print link_node.name, link_node['href'], link_node.get_text()


print 'p段落文字'
link_node = soup.find('p', class_="title")  # class是关键字，给其添加一个下划线
print link_node.name, link_node.get_text()
