#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 内置函数的使用
x = abs(100)
y = abs(-20)
print(x, y)
print('max(1, 2, 3) =', max(1, 2, 3))
print('min(1, 2, 3) =', min(1, 2, 3))
print('sum([1, 2, 3]) =', sum([1, 2, 3]))
# 函数名其实就是指向一个函数对象的引用，完全可以把函数名赋给一个变量，相当于给这个函数起了一个“别名”
a = abs  # 变量a指向abs函数
print(a(-1))

# 定义函数
import math


def my_abs(x):
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x


print(my_abs(123), my_abs(-123), my_abs('123'))

# 返回多值的函数，返回的是一个tuple，可以通过序列解包进行赋值
import math


def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny


x, y = move(100, 100, 60, math.pi / 6)
print(x, y)
t = move(100, 100, 60, math.pi / 6)
print(t)


# 没有return或只写return的函数，返回None
def func():
    print('hello, world')
    return

print(func())
