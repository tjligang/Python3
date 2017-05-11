#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 不可变对象的赋值和修改

# 变量赋值的过程：在内存中创建了一个'abc'的字符串，在内存中创建了一个名为s1的变量，并把它指向'abc'
s1 = 'abc'
print(id(s1), type(s1))  # id()查看对象的内存地址，type()查看对象的类型
# 把一个变量s1赋值给另一个变量s2，共享引用
# 这个操作实际上是把变量s2指向变量s1所指向的数据，即两个变量指向同一个对象
s2 = s1
print(id(s2), type(s2))  # 指向同一对象
# 对于不可变对象，可利用共享引用节省内存
s1 = 'def'
s2 = 'def'
print(id(s1), id(s2))  # 指向同一对象，节省内存

# 对于不可变对象，对其赋值或调用方法修改，都会导致变量指向新的copy，原对象不变
s1 = 'xyz'  # 或者s1 = s1 + 'xyz'
print(id(s1), id(s2))  # 赋值会导致变量指向新的对象
s2 = s1.replace('x', 'xx')  # 返回copy，原对象不变
print(s1, s2, id(s1), id(s2))


# 可变对象的赋值和修改
l1 = ['a', 'b']
print(id(l1), type(l1))
l2 = l1  # 共享引用，指向同一对象
print(id(l2), type(l2))
l1[0] = 'aa'  # 通过一个变量改变对象的值，另一个变量也可以看到变化
print(l1, l2, id(l1), id(l2))
# 对于可变对象，两个变量被赋予相同的值，不使用共享引用
l1 = ['a', 'b']
l2 = ['a', 'b']
print(id(l1), id(l2))
# 可以使用list的方法或copy模块进行快速复制
l1 = ['a', 'b']
l2 = l1[:]
print(l1, l2, id(l1), id(l2))
import copy
l2 = copy.copy(l1)
print(l1, l2, id(l1), id(l2))
# 如果list中的元素还有可变对象，可使用deepcopy保证所有对象不产生共享引用
# l2 = copy.deepcopy(l1)

l1 = ['a', 'b']
print(id(l1))
l2 = l1.append('c')  # 现场修改，原对象改变，返回None
print(l1, l2, id(l1), type(l1), id(l2), type(l2))


# 对象的比较
# 不可变对象使用共享引用，==和is结果相同
x = 42
y = 42
print(x == y, x is y)
# 可变对象不使用共享引用，==和is结果不同
l1 = [1, 2, 3]
l2 = [1, 2, 3]
print(l1 == l2, l1 is l2)
