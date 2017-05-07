#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 不可变对象的赋值和修改

# 变量赋值的过程：在内存中创建了一个'abc'的字符串，在内存中创建了一个名为s1的变量，并把它指向'abc'
s1 = 'abc'
print(id(s1), type(s1))  # id()查看对象的内存地址，type()查看对象的类型
# 把一个变量s1赋值给另一个变量s2，这个操作实际上是把变量s2指向变量s1所指向的数据，即两个变量指向同一个对象
s2 = s1
print(id(s2), type(s2))  # 指向同一对象

s1 = 'def'
s2 = 'def'
print(id(s1), id(s2))  # 指向同一对象，节省内存

s1 = 'xyz'
print(id(s1), id(s2))  # 赋值会导致变量指向新的对象

s2 = s1.replace('x', 'xx')  # 返回copy，原对象不变
print(s1, s2, id(s1), id(s2))


# 可变对象的赋值和修改
l1 = ['a', 'b']
print(id(l1), type(l1))
l2 = l1  # 指向同一对象
print(id(l2), type(l2))
l1[0] = 'aa'  # 改变一个变量，另一个也变
print(l1, l2, id(l1), id(l2))

l1 = ['a', 'b']
print(id(l1))
l2 = l1.append('c')  # 现场修改，原对象改变，返回None
print(l1, l2, id(l1), type(l1), id(l2), type(l2))
