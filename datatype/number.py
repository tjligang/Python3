#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# Python3的整数支持无限精度
print(2**100, len(str(2**1000000)))
# 整数（十进制、十六进制、八进制、二进制）
# 数值对应一个整数对象，不同的进制仅是不同的表示方式
print(1, 0x00FE, 0o10, 0b1010)  # 不同的进制表示，输出的都是整数
# 把整数转换成3种进制的字符串
print(hex(100), oct(100), bin(100), type(hex(100)))
# 把字符串按照对应进制转换成整数
print(int('100'))
print(int('0x100', 16), int('100', 16))
print(int('0o100', 8), int('100', 8))
print(int('0b100', 2), int('100', 2))


# 浮点数（数学表示、科学计数法）
print(3.14, 1.23e9)
# 浮点数必须有小数点
print(type(1), type(1.0))
# 浮点数是实数的近似表示，所以浮点运算缺乏精确性
print(0.1+0.1-0.2, 0.1+0.1+0.1-0.3)


# 复数
a = 1+5j
print(a, type(a), a*2)


# 自动将简单类型转换为复杂类型，再进行计算
print(1+1.0, type(1+1.0), 1+1.0+(1+5j), type(1+1.0+(1+5j)))
# 手动转换，简单->复杂，通常是不需要的
print(float(1+1.0))
# 手动转换，复杂->简单，丢失精度或报错
print(int(1+1.1), type(int(1+1.1)))
# print(float(1+5j))


# 可以把任意数据类型赋值给变量，同一个变量可以反复赋值，而且可以是不同类型的变量
# 这种变量本身类型不固定的语言称之为动态语言
a = 123
print(a)
a = 'ABC'
print(a)
a = True
print(a)


# 常量就是不能变的变量，通常用全部大写的变量名表示常量
# PI仍然是一个变量，Python根本没有任何机制保证PI不会被改变，所以，用全部大写的变量名表示常量只是一个习惯上的用法
PI = 3.14159265359


# 各种赋值方法
# 序列解包
x, y, z = 1, 2, 3
print(x, y, z)
x, y = y, x
print(x, y)
x, y, z = z, x, y
print(x, y, z)
d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
key, value = d.popitem()
print(key, value)
a, b, *rest = [1, 2, 3, 4]  # 使用list保存剩余的值
print(a, b, rest)
# 链式赋值
x = y = 1
print(x, y)
# 增量赋值
x = 2
x += 1
x *= 2
print(x)
x = 'foot'
x += 'ball'
x *= 2
print(x)


# /真除法计算结果是浮点数，即使是两个整数恰好整除，结果也是浮点数
# //称为地板除，两个整数的除法仍然是整数，可能会显示为整数或浮点数形式
print(5 / 2, 5 / 2.0, -5 / 2, -5 / 2.0)
print(5 // 2, 5 // 2.0, -5 // 2, -5 // 2.0)
print(9 / 3, 9 / 3.0, 9 // 3, 9 // 3.0)
# floor除不是四舍五入或截断，注意round的误差
import math
print(5 / -2, 5 // -2, math.trunc(5 / -2), round(5 / -2))
# 余数运算
print(-10 % 3, 9 % 3)


# decimal用于精确计算
print(0.1 + 0.1 + 0.1 - 0.3)
from decimal import Decimal
print(Decimal('0.1') + Decimal('0.1') + Decimal('0.1') - Decimal('0.3'))
# 设置全局精度
import decimal
print(decimal.Decimal(1) / decimal.Decimal(7))

decimal.getcontext().prec = 4
print(decimal.Decimal(1) / decimal.Decimal(7))
print(1999 + 1.33)

decimal.getcontext().prec = 2
pay = decimal.Decimal(str(1999 + 1.33))
print(pay)
# 上下文管理器
decimal.getcontext().prec = 28
import decimal
print(decimal.Decimal('1.00') / decimal.Decimal('3.00'))

with decimal.localcontext() as ctx:
    ctx.prec = 2
    print(decimal.Decimal('1.00') / decimal.Decimal('3.00'))

print(decimal.Decimal('1.00') / decimal.Decimal('3.00'))


# fractions
# fraction的创建和使用
from fractions import Fraction
x = Fraction(1, 3)                # Numerator, denominator
y = Fraction(4, 6)                # Simplified to 2, 3 by gcd
print(x, y, x + y, x - y, x * y)
# 通过字符串构造
print(Fraction('.25'), Fraction('1.25'), Fraction('.25') + Fraction('1.25'))

# float无法精确表示，fraction和decimal都可以
a = 1 / 3.0       # Only as accurate as floating-point hardware
b = 4 / 6.0       # Can lose precision over calculations
print(a, b, a + b, a - b, a * b)
a = Fraction(1, 3)
b = Fraction(4, 6)
print(a, b, a + b, a - b, a * b)

print(0.1 + 0.1 + 0.1 - 0.3)  # This should be zero (close, but not exact)
from fractions import Fraction
print(Fraction(1, 10) + Fraction(1, 10) + Fraction(1, 10) - Fraction(3, 10))
from decimal import Decimal
print(Decimal('0.1') + Decimal('0.1') + Decimal('0.1') - Decimal('0.3'))

# fraction和decimal通过不同方式保证结果的精准
print(Fraction(1, 3))                    # Numeric accuracy
import decimal
decimal.getcontext().prec = 2  # decimal可以保证在精度范围内的准确
print(decimal.Decimal(1) / decimal.Decimal(3))

print((1 / 3) + (6 / 12))
print(Fraction(1, 3) + Fraction(6, 12))
print(decimal.Decimal(str(1/3)) + decimal.Decimal(str(6/12)))


# 布尔值，注意大小写
print(True, False, 3 > 2, 3 > 5)
# 什么是true和false
if False or None or 0 or "" or () or [] or {}:
    print('True')
else:
    print('All of them are FASLE!')

if True and 1 and 'abc' and (1, 2, 3) and {'x': 1, 'y': 2}:
    print('All of them are TRUE!')

# 与或非
print(True and False, 5 > 3 and 2 > 1, True or False, 5 > 3 or 1 > 3, not True, not 1 > 2)
