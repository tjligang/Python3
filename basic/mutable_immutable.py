#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 不可变对象的赋值和修改
s1 = 'abc'
print(id(s1))  # id()查看对象的内存地址
s2 = s1  # 指向同一对象
print(id(s2))

s1 = 'def'
s2 = 'def'
print(id(s1), id(s2))

s1 = 'xyz'
s2 = s1.replace('x', 'xx')  # 返回copy，原对象不变
print(s1, s2, id(s1), id(s2))


# 可变对象的赋值和修改
l1 = ['a', 'b']
print(id(l1))
l2 = l1  # 指向同一对象
print(id(l2))
l1[0] = 'aa'  # 改变一个变量，另一个也变
print(l1, l2, id(l1), id(l2))

l1 = ['a', 'b']
print(id(l1))
l2 = l1.append('c')  # 现场修改，原对象改变，返回None
print(l1, l2, id(l1), id(l2))
