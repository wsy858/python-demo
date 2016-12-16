# -*- encoding=utf-8 -*-
# d = {
#     'Adam': 95,
#     'Lisa': 85,
#     'Bart': 59
# }
# for key in d:
#     print key+ ':',  d[key] 
# print '方法'
# s = set([1,2,3,4,5,5])
# print s
# s.add(8)
# print s
# s.remove(5)
# print s
# if 5 in s: 
#     s.remove(5)
# 
# s = set(['Adam', 'Lisa', 'Paul'])
# L = ['Adam', 'Lisa', 'Bart', 'Paul']
# for i in L:
#     if i in s :
#         s.remove(i)
#     else:
#         s.add(i)
# print s
# print any(s)
# 
# L = []
# i=1
# while i <= 100 :
#     L.append(i * i)
#     i = i + 1
# print sum(L)
# 
# import math
# #x = (-b±√(b²-4ac)) / 2a
# def quadratic_equation(a, b, c):
#     x = (-b + math.sqrt(b * b - 4 * a * c) ) / (2 * a)
#     y = (-b - math.sqrt(b * b - 4 * a * c) ) / (2 * a)
#     return x, y
# print quadratic_equation(2, 3, 0)
# print quadratic_equation(1, -6, 5)
# print range(10)

s = [23, 45, 66, 78, 89]
x = 0
for i in s:
    if x == 3:
        break
    x += 1
    print 'this is : ', i
else:
    print 'else '

for x in range(10):
    if x == 5:
        break
    print x
