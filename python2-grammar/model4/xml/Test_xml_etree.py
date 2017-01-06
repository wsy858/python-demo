# _*_ coding:UTF-8 _*_

"""
Created on 2017/1/6 20:08
@author: evan
"""

import xml.etree.ElementTree as ET

tree = ET.parse('movies.xml')
root = tree.getroot()

print "Root element : %s " % root.tag
print "Root element attribute: %s " % root.attrib['shelf']

# for child in root:
movies = root.findall("movie")
# movie类型为 xml.etree.ElementTree.Element
for movie in movies:
    print "*****Movie*****"
    # 获取Element属性, 不存在会报错
    print "Title: %s" % movie.attrib['title']
    # 获取Element属性, 不存在为None
    print "Title: %s" % movie.get('title')
    # 获取Element的文本子内容
    print "Type: %s" % movie.find("type").text
    print "format: %s" % movie.find("format").text
    if movie.find("year") is not None:
        print "year: %s" % movie.find("year").text
    print "rating: %s" % movie.find("rating").text
    print "stars: %s" % movie.find("stars").text
    print "description: %s" % movie.find("description").text
    print " "

for movie in root.iter('movie'):
    print movie.attrib
