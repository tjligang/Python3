#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 如果if语句判断是True，就把缩进的两行print语句执行了，注意冒号：
age = 20
if age >= 18:
    print('your age is', age)
    print('adult')

age = 3
if age >= 18:
    print('your age is', age)
    print('adult')
else:
    print('your age is', age)
    print('teenager')

age = 3
if age >= 18:
    print('adult')
elif age >= 6:
    print('teenager')
else:
    print('kid')

# input()返回的数据类型是str，str不能直接和整数比较，必须先把str转换成整数
s = input('birth: ')
birth = int(s)
if birth < 2000:
    print('00前')
else:
    print('00后')

# for循环
names = ['Michael', 'Bob', 'Tracy']
for name in names:
    print(name)

sum = 0
for x in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
    sum = sum + x
print(sum)
# range()函数，可以生成一个整数序列(0, n-1)，再通过list()函数可以转换为list
print(list(range(5)))
sum = 0
for x in range(101):
    sum = sum + x
print(sum)
# while循环
sum = 0
n = 99
while n > 0:
    sum = sum + n
    n = n - 2
print(sum)
