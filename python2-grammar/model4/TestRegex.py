#-*- coding: utf-8 -*-
'''
Created on 2016年10月18日
正则表达式
@author: evan
'''
import re


'''
'''
# 将正则表达式编译成Pattern对象
pattern = re.compile(r'WWWf', re.I)
# 使用Pattern匹配文本，获得匹配结果，无法匹配时将返回None
match = pattern.match('www.google.com')
print match
if match:
    print match.group()
else:
    print 'not match'
print '\n'



'''
re.match(pattern, string, flags=0)函数
从开始位置匹配，包含了很多关于此次匹配的信息，可以使用Match提供的可读属性或方法来获取这些信息。
pattern  : 匹配的正则表达式.
string   : 要匹配的字符串。
flags    : 标志位，用于控制正则表达式的匹配方式，如：是否区分大小写，多行匹配等等。
re.I(re.IGNORECASE): 忽略大小写（括号内是完整写法，下同）
re.M(re.MULTILINE): 多行模式，改变'^'和'$'的行为
re.S(re.DOTALL): 点任意匹配模式，改变'.'的行为， 使 .匹配包括换行在内的所有字符
re.L(re.LOCALE): 使预定字符类 \w \W \b \B \s \S 取决于当前区域设定
re.U(re.UNICODE): 使预定字符类 \w \W \b \B \s \S \d \D 取决于unicode定义的字符属性
re.X(re.VERBOSE): 详细模式。这个模式下正则表达式可以是多行，忽略空白字符，并可以加入注释。

'''
print re.match(r'www', 'www.google.com')
print re.match(r'com', 'www.google.com')
m = re.match(r'(\w+) (\w+)(?P<sign>.*)', 'hello world!')
print "m.string: ", m.string #匹配时使用的文本。
print "m.re: ", m.re #配时使用的Pattern对象。
print "m.pos: ", m.pos #文本中正则表达式开始搜索的索引。值与Pattern.match()和Pattern.seach()方法的同名参数相同。
print "m.endpos: ", m.endpos #文本中正则表达式结束搜索的索引。值与Pattern.match()和Pattern.seach()方法的同名参数相同。
print "m.lastindex: ", m.lastindex #最后一个被捕获的分组在文本中的索引。如果没有被捕获的分组，将为None。
print "m.lastgroup: ", m.lastgroup #最后一个被捕获的分组的别名。如果这个分组没有别名或者没有被捕获的分组，将为None。
print "m.group(0): ", m.group(0) #返回匹配到的整个字符串
print "m.group(1): ", m.group(1) #返回匹配到的第一个组的字符串
print "m.group(1,2): ", m.group(1, 2) #以元组的形式返回匹配到的第一个和第二个组字符串
print "m.group('sign'): ", m.group('sign') #指定别名组匹配到的字符串
print "m.groups(): ", m.groups() #以元组形式返回全部分组截获的字符串
print "m.groupdict(): ", m.groupdict() #返回以有别名的组的别名为键、以该组截获的子串为值的字典，没有别名的组不包含在内
print "m.start(2): ", m.start(2) #第二个组在字符串中开始索引
print "m.end(2): ", m.end(2)     #第二个组在字符串中结束位置
print "m.span(2): ", m.span(2)   #第二个组在字符串中开始与结束位置
print '\n'


'''
re.search() ： 扫描整个字符串并返回第一个成功的匹配， 匹配成功返回一个匹配的对象，否则返回None。
re.match()只匹配字符串的开始，如果字符串开始不符合正则表达式，则匹配失败，函数返回None；而re.search()匹配整个字符串，直到找到一个匹配。
'''
print re.search(r'www', 'www.google.com')
print re.search(r'com', 'www.google.com')


'''
re.split(pattern, string[, maxsplit])： 按照能够匹配的子串将string分割后返回列表, 
                                       maxsplit用于指定最大分割次数，不指定将全部分割。 
'''
print re.split(r'\d+', 'one1two2three3four4');


'''
re.findall(pattern, string[, flags]): 搜索string，以列表形式返回全部能匹配的子串。 
'''
print re.findall(r'\d+', 'one123two234three345four456')


'''
re.finditer(pattern, string[, flags]): 搜索string，返回一个顺序访问每一个匹配结果（Match对象）的迭代器。 
'''
for m in re.finditer(r'\d+', 'one123two234three345four456'):
    print m.group()
    
'''
re.sub(pattern, repl, string[, count]): 使用repl替换string中每一个匹配的子串后返回替换后的字符串。 
当repl是一个字符串时，可以使用\id或\g<id>、\g<name>引用分组，但不能使用编号0。 
当repl是一个方法时，这个方法应当只接受一个参数（Match对象），并返回一个字符串用于替换（返回的字符串中不能再引用分组）。 
count用于指定最多替换次数，不指定时全部替换。
'''
print re.sub(r'(\w+) (\w+)', r'\2 \1', 'i say, hello world!')
    
def func(m):
    return m.group(1).title() + ' ' + m.group(2).title()
print re.sub(r'(\w+) (\w+)', func, 'i say, hello world!')


'''
re.sub(pattern, repl, string[, count]):
返回(re.sub(pattern, repl, string[, count]), 替换次数)
'''
print re.subn(r'(\w+) (\w+)', func, 'i say, hello world!')
    
 