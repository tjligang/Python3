#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# 局部作用域中，同名的全局变量被屏蔽
def func(x):
    x = 1
    print('Inside func: x=', x)

x = 11
func(x)
print('Outside func: x=', x)


# 不同名的全局变量可以直接引用，不推荐
def func(x):
    x += y
    print('Inside func: x = %s, y = %s' % (x, y))

x, y = 1, 2
func(x)
print('Outside func: x = %s, y = %s' % (x, y))


# 访问全局变量的两种方法，不推荐
# 对比局部变量
def func1():
    x = 1
    print('Inside func1: x =', x)


def func2():
    globals()['x'] = 1
    print('Inside func2: x = ', x)


def func3():
    global x
    x = 1
    print('Inside func3: x = ', x)

x = 2
func1()
print('Outside func1: x = ', x)

x = 2
func2()
print('Outside func2: x = ', x)

x = 2
func3()
print('Outside func3: x = ', x)
