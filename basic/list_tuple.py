#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Python内置的一种数据类型是列表：list。list是一种有序的集合，可以随时添加和删除其中的元素
classmates = ['Michael', 'Bob', 'Tracy']
# list的各种访问方法：
print(classmates, len(classmates))
print(classmates[0], classmates[1], classmates[2], )
print(classmates[-1], classmates[-2], classmates[-3])
# print(classmates[3], classmates[-4])索引超出了范围，最后一个元素的索引可使用len(classmates) - 1

# list是一个可变的有序表，各种操作方法：
classmates.append('Adam')  # 追加元素到末尾
print(classmates)
classmates.insert(1, 'Jack')  # 把元素插入到指定的位置
print(classmates)
classmates.pop()  # 删除list末尾的元素
print(classmates)
classmates.pop(1)  # 删除指定位置的元素
print(classmates)
classmates[1] = 'Sarah'  # 把某个元素替换成别的元素，可以直接赋值给对应的索引位置
print(classmates)

# list里面的元素的数据类型可以不同
L = ['Apple', 123, True]
# list元素也可以是另一个list
s = ['python', 'java', ['asp', 'php'], 'scheme']
print(len(s))  # s只有4个元素，其中s[2]又是一个list
# 二维list更好理解的写法：
p = ['asp', 'php']
s = ['python', 'java', p, 'scheme']
print(p[1], s[2][1])
# 如果一个list中一个元素也没有，就是一个空的list，它的长度为0：
L = []
print(len(L))