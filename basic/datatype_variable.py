#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 整数（十进制、十六进制、八进制）
print(1, 0x00FE, 0o10)
# 浮点数（数学表示、科学计数法）
print(3.14, 1.23e9)

# 字符串使用单引号或双引号，“，”通过空格连接两个字符串
print('abc', "xyz")
# +连接两个字符串，中间没有空格，或者直接将两个字符串写在一起
print('abc' + "xyz", 'abc'"xyz")
# 如果'本身也是一个字符，那就可以用""括起来(相反也可以)
print("I'm OK", '"xyz"')
# 既包含'又包含"可以用转义字符\来标识
print('I\'m \"OK\"!')
# 转义字符\可以转义各种控制字符，\\表示的字符就是\
print('I\'m learning\nPython.')
print('\\\n\\')
# 为了简化，用r''表示''内部的字符串默认不转义，表示dos路径或写正则表达式时非常有用
print(r'\\\t\\')
print('C:\nowhere')
print(r'C:\nowhere')
print('C:\\abc\\def\\xyz')
print(r'C:\abc\def\xyz')
# print(r'C:\abc\def\xyz\')最后一个\被python误认为是跨行标记，会报错
print(r'C:\abc\def\xyz''\\')

# 用'''...'''的格式表示多行内容（长字符串），代替\n，可以和r配合
print('''line1
line2
line3''')
print(r'''line1's
line2's
line3's''')

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

# 空值，None是一个特殊类型的常量，有自己的数据类型NoneType，它只有一个值None，不是0，不是空字符串。
# None不支持任何运算也没有任何内建方法.
# None和任何其他的数据类型比较永远返回False。
# 可以将None复制给任何变量，但是不能创建其他NoneType对象。
a = None
print('a is', a)
print(type(None), type(0), type(''))

# 可以把任意数据类型赋值给变量，同一个变量可以反复赋值，而且可以是不同类型的变量
# 这种变量本身类型不固定的语言称之为动态语言
a = 123
print(a)
a = 'ABC'
print(a)
a = True
print(a)

# 变量赋值的过程：在内存中创建了一个'ABC'的字符串，在内存中创建了一个名为a的变量，并把它指向'ABC'
# 把一个变量a赋值给另一个变量b，这个操作实际上是把变量b指向变量a所指向的数据
a = 'ABC'
b = a
a = 'XYZ'
print(b)

# 常量就是不能变的变量，通常用全部大写的变量名表示常量
# PI仍然是一个变量，Python根本没有任何机制保证PI不会被改变，所以，用全部大写的变量名表示常量只是一个习惯上的用法
PI = 3.14159265359

# /除法计算结果是浮点数，即使是两个整数恰好整除，结果也是浮点数
print(10 / 3, 9 / 3)
# //称为地板除，两个整数的除法仍然是整数
print(10 // 3, 9 // 3)
# 余数运算
print(10 % 3, 9 % 3)

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
