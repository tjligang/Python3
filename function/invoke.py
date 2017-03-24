#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# 正确的说法是：传对象引用
# 不可变对象作为参数：传值，对象不变
def test(c):
    print("test before ")
    print(id(c))  # c和a指向同一对象
    c += 2  # 不可变对象被修改，会导致变量指向新内存地址中的对象
    print("test after +")
    print(id(c))
    return c

a = 2
print("main before invoke test")
print(id(a))
n = test(a)
print("main after invoke test")
print(a)  # 不可变对象不会被改变
print(id(a))


# 可变对象作为参数：传引用，对象改变
def test(list2):
    print("test before ")
    print(id(list2))  # list1和list2指向同一对象
    list2[1] = 30  # 现场修改，list1和list2都被改变
    print("test after +")
    print(id(list2))  # 指向不变
    return list2

list1 = ['alice', 25, 'female']
print("main before invoke test")
print(id(list1))
list3 = test(list1)
print("main after invoke test")
print(list1)  # list1被修改
print(id(list1))
