# -*- coding: utf-8 -*-
"""
清除包含以lastUpdated结尾文件的目录
Created on 2016年11月4日
@author: evan
"""
import os
import shutil


def clearMaven():
    # 遍历文档树
    for path, dirs, fileNames in os.walk("e:/maven/repository"):
        print path, dirs, fileNames
        for fileName in fileNames:
            if fileName.endswith("lastUpdated"):
                shutil.rmtree(path)


if __name__ == '__main__':
    clearMaven()
