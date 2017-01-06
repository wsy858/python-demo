# _*_ coding:UTF-8 _*_

"""
DOM解析XML
Created on 2017/1/6 19:48
@author: evan
"""

from xml.dom.minidom import parse


def dom_parse_xml():
    tree = parse("movies.xml")
    collection = tree.documentElement
    if collection.hasAttribute("shelf"):
        print "Root element : %s " % collection.getAttribute("shelf")

    # 在集合中获取所有电影
    movies = collection.getElementsByTagName("movie")

    # 打印每部电影的详细信息
    for movie in movies:
        print "*****Movie*****"
        if movie.hasAttribute("title"):
            print "Title: %s" % movie.getAttribute("title")
        type = movie.getElementsByTagName('type')[0]
        print "Type: %s" % type.childNodes[0].data
        format = movie.getElementsByTagName('format')[0]
        print "Format: %s" % format.childNodes[0].data
        rating = movie.getElementsByTagName('rating')[0]
        print "Rating: %s" % rating.childNodes[0].data
        description = movie.getElementsByTagName('description')[0]
        print "Description: %s" % description.childNodes[0].data


if __name__ == "__main__":
    dom_parse_xml()