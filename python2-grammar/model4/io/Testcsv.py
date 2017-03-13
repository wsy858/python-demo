# _*_ coding:UTF-8 _*_

"""
python操作csv
Created on 2017/3/8 15:52
@author: evan
"""
import os
import csv


# 合并csv文件
def combine():
    csvfileto = file('G:/tt/result.csv', 'wb')
    writer = csv.writer(csvfileto, delimiter='|')

    # 遍历文档树
    for path, dirs, fileNames in os.walk("g:/tt"):
        # print path, dirs, fileNames
        for fileName in fileNames:
            if fileName != 'result.csv':
                csvfilefrom = file(path + "/" + fileName, 'rb')
                # QUOTE_NONE读的时候都认为内容是不被默认引用符(")包围的
                reader = csv.reader(csvfilefrom, delimiter='|', quoting=csv.QUOTE_ALL, quotechar="|")
                i = 0
                for line in reader:
                    print line
                    # print "********", fileName, "********",  i
                    writer.writerow(line)
                    i += 1
                csvfilefrom.close()
    csvfileto.close()


if __name__ == '__main__':
    combine()
