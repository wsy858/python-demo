# -*- coding: utf-8 -*-
"""
Created on 2016年10月18日
io
@author: evan
"""
import os

'''
标准输入：
raw_input([prompt]) 函数从标准输入读取一个行，并返回一个字符串（去掉结尾的换行符）
input([prompt]) 函数和 raw_input([prompt]) 函数基本类似，但是 input可以接收一个Python表达式作为输入，并将运算结果返回
raw_input() 将所有输入作为字符串看待，返回字符串类型。
input()接收字符串时要带上'或者"
'''
# ss = raw_input('请输入: ')
# print '输入内容是: ', ss, 'type: ', type(ss)

# 请输入: [x * 5 for x in range(2, 10, 2)]
# 输入内容是:  [10, 20, 30, 40]

# ss = input('请输入: ')
# print '输入内容是: ', ss, 'type: ', type(ss)
# print '\n'


'''
open函数, 格式如下：
file object = open(file_name [, access_mode][, buffering])
入口参数: name 文件名
        mode 选项,字符串
        buffering  是否缓冲 (0=不缓冲，1=缓冲, >1的int数=缓冲区大小)
'''
f = open('a.txt', 'wb')
print "文件名: ", f.name
print "是否已关闭 : ", f.closed
print "访问模式 : ", f.mode
print "末尾是否强制加空格 : ", f.softspace
f.close()
print "是否已关闭 : ", f.closed
print '\n'

'''
write()方法
write()方法可将任何字符串写入一个打开的文件。需要重点注意的是，Python字符串可以是二进制数据，而不是仅仅是文字。
write()方法不会在字符串的结尾添加换行符('\n')：
'''
f = open('a.txt', 'wb')
f.write('hello')
f.write('world')
f.writelines('你好')
f.writelines('中国')
f.writelines(['22', '33'])
f.close()

'''
read()方法
read()方法从一个打开的文件中读取一个字符串, 
的参数是要从已打开文件中读取的字节计数。该方法从文件的开头开始读入，如果没有传入count，它会尝试尽可能多地读取更多的内容，很可能是直到文件的末尾。
'''
f = open('a.txt', 'r+')
print f.read()
f.seek(0)
print f.read(16)
print "当前文件位置 : ", f.tell()
f.seek(0)
print f.readline()

'''
文件创建、重命名、删除操作
'''
try:
    f = open('ff.txt', 'w+')
    f.write('bbbbbb')
except Exception, e:
    print e
finally:
    try:
        f.close()
    except:
        pass
# 删除文件
try:
    os.remove('b.txt')
except Exception, e:
    print e
# 重命名文件
os.rename('ff.txt', 'b.txt')

# 清空文件内容
# f.truncate()


'''
目录操作
'''
# 删除目录, 目前里面必须是空的, 否则报错。
os.rmdir("newdir")
# 在当前目录下创建目录
os.mkdir("newdir")
# 更改当前目录
os.chdir("newdir")
os.mkdir("test")
# 显示当前目录
print os.getcwd()

'''
文件打开模式
r    以只读方式打开文件。文件的指针将会放在文件的开头。这是默认模式。
rb   以二进制格式打开一个文件用于只读。文件指针将会放在文件的开头。这是默认模式。
r+   打开一个文件用于读写。文件指针将会放在文件的开头。
rb+  以二进制格式打开一个文件用于读写。文件指针将会放在文件的开头。
w    打开一个文件只用于写入。如果该文件已存在则将其覆盖。如果该文件不存在，创建新文件。
wb   以二进制格式打开一个文件只用于写入。如果该文件已存在则将其覆盖。如果该文件不存在，创建新文件。
w+   打开一个文件用于读写。如果该文件已存在则将其覆盖。如果该文件不存在，创建新文件。
wb+  以二进制格式打开一个文件用于读写。如果该文件已存在则将其覆盖。如果该文件不存在，创建新文件。
a    打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。也就是说，新的内容将会被写入到已有内容之后。如果该文件不存在，创建新文件进行写入。
ab   以二进制格式打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。也就是说，新的内容将会被写入到已有内容之后。如果该文件不存在，创建新文件进行写入。
a+   打开一个文件用于读写。如果该文件已存在，文件指针将会放在文件的结尾。文件打开时会是追加模式。如果该文件不存在，创建新文件用于读写。
ab+  以二进制格式打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。如果该文件不存在，创建新文件用于读写。
'''
