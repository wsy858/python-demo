# -*- encoding=utf-8 -*-
# for循环迭代字典
d = {
    'Adam': 95,
    'Lisa': 85,
    'Bart': 59
}
for key in d:
    print key + ':', d[key]

s = {'Adam', 'Lisa', 'Paul', "Adam"}
L = ['Adam', 'Lisa', 'Bart', 'Paul']
for i in L:
    if i in s:
        s.remove(i)
    else:
        s.add(i)
print s
print any(s)


# while循环
L = []
i = 1
while i <= 100:
    L.append(i * i)
    i += 1
print sum(L)

# break语句
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
