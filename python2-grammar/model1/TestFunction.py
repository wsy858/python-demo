# -*- encoding=utf-8 -*-
"""
Created on 2016年9月30日
@author: Administrator
"""


'''
1、我们来计算阶乘 n! = 1 * 2 * 3 * ... * n，用函数 fact(n)表示，可以看出：
fact(n)可以表示为 n * fact(n-1)，只有n=1时需要特殊处理。
'''
def f(n):
    if n == 0 or n == 1:
        return n
    else:
        return f(n - 1) * n
# x = 0
# while x <= 100 :
#     print f(x)
#     x = x + 1
# print f(100) + 1


"""
2、汉诺塔 (http://baike.baidu.com/view/191666.htm) 的移动也可以看做是递归函数。
我们对柱子编号为a, b, c，将所有圆盘从a移到c可以描述为：
如果a只有一个圆盘，可以直接移动到c；
如果a有N个圆盘，可以看成a有1个圆盘（底盘） + (N-1)个圆盘，首先需要把 (N-1) 个圆盘移动到 b，然后，将 a的最后一个圆盘移动到c，再将b的(N-1)个圆盘移动到c。
请编写一个函数，给定输入 n, a, b, c，打印出移动的步骤：
move(n, a, b, c)
例如，输入 move(2, 'A', 'B', 'C')，打印出：
A --> B
A --> C
B --> C
"""
def move(n, a, b, c):
    if n == 1:
        print a, '-->', c
        return
    move(n - 1, a, c, b)  # 把 (N-1)个圆盘从a借助c移动到 b
    print a, '-->', c  # 将 a的最后一个圆盘移动到c
    move(n - 1, b, a, c)  # 把 (N-1)个圆盘从b借助a移动到 c


# 可变长度参数
def average(*args):
    s = 0.0
    x = len(args)
    if x == 0:
        return s
    for i in args:
        s += i
    print 's', s, 'x', x
    return s / x


# 计算最大公约数
def gongyueshu(x, y):
    if x < y:
        x, y = y, x
    u = x % y
    while u != 0:
        x, y = y, u
        u = x % y
    print y

# 结算阶乘s
def jiechen(n):
    if n <= 1:
        return 1
    else:
        return n * jiechen(n-1)

if __name__ == "__main__":
    # move(4, 'A', 'B', 'C')
    # print average()
    # print average(1, 2)
    # print average(1, 2, 2, 3, 4)
    gongyueshu(48, 36)
    print jiechen(10)
    pass
