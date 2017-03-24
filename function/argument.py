#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# 定义函数时，对参数提供默认值，可以简化函数的调用
def hello(s1, s2, sep=',', end='!'):
    return s1+sep+s2+end

# 位置参数法：
print(hello('hello', 'world'))
print(hello('hello', 'world', ':'))
print(hello('hello', 'world', ':', '?'))
# 必选参数必须提供，否则报错
# print(concat('hello'))
# 必须按照参数定义顺序提供值
print(hello('hello', 'world', '?'))

# 关键字参数法：灵活，可读性高
print(hello(s1='hello', s2='world'))
print(hello(s2='hello', s1='world'))
print(hello(s1='hello', sep=':', s2='world', end='?'))
print(hello(s1='hello', s2='world', end='?'))

# 两种调用方法可以混用
# 但位置参数必须在前并且保证顺序，关键字参数在后，忽略顺序
print(hello('hello', 'world', end='?'))
# print(hello('hello', sep=':', 'world'))


# 可变参数
def path(title, sep, *args):
    print(args)
    p = title
    for s in args:
        p += (s+sep)
    return p

# 可变参数被转换为tuple
print(path('The unix path is: ', '/', '', 'usr', 'bin'))
print(path('The windows path is: ', '\\', 'C:', 'windows', 'system32'))

# 解包参数列表
l1 = ['', 'usr', 'bin']
l2 = ['C:', 'windows', 'system32']
print(path('The unix path is: ', '/', l1[0], l1[1], l1[2]))
print(path('The windows path is: ', '\\', l2[0], l2[1], l2[2]))
print(path('The unix path is: ', '/', *l1))
print(path('The windows path is: ', '\\', *l2))

# 错误的调用方法
# 默认值参数不能省略，即使使用的就是默认值
print(path('The unix path is: ', *l1))
# 不可使用关键字参数法
# print(path(sep='/', title='The unix path is: ', *l1))
# print(path('The unix path is: ', *l1, sep='/'))


# 关键字参数
def person(name, phone_no, **kw):
    print(kw)
    print('Personal Info:')
    print('name:', name)
    print('phone_no:', phone_no)
    for key, value in kw.items():
        print(key, ':', value)

# 关键字参数在函数内部被组装成dict，可通过参数名逐一使用
person('Michael', 13912345678)
person('Bob', 1234, city='Beijing')
person('Adam', 5678, gender='M', job='Engineer')

# 位置参数必须保证顺序，关键字参数可打乱顺序
person('Adam', 5678, job='Engineer', gender='M')

# 通过参数序列解包，可以将dict拆解，再传入函数
extra = {'city': 'Beijing', 'job': 'Engineer'}
person('Jack', 1234, city=extra['city'], job=extra['job'])
person('Jack', 5678, **extra)

# 位置参数和关键字参数可以混用，但要保证位置参数在前
# 不建议混用
person('Jack', **extra, phone_no=1234)
person('Jack', phone_no=1234, **extra)

# 错误的调用方法
# person('Jack', **extra, 1234)
# person(phone_no=5678, 'Jack', **extra)

# 关键字参数无法控制错误参数传入
person('Bob', 1234, city='Beijing', wrong_arg='haha')


# 仅关键字参数的第一种方式：不确定的参数+确定的选项
# 使用普通参数+可变参数的解决方案：定义时简单，调用时麻烦
def trans_1(case='lower', sort=True, *args):
    s = list(args)
    if case == 'lower':
        for i in range(len(s)):
            s[i] = s[i].lower()  # lower()返回copy，不改变变量的值
    elif case == 'upper':
        for i in range(len(s)):
            s[i] = s[i].upper()
    elif case == 'capitalize':
        for i in range(len(s)):
            s[i] = s[i].capitalize()
    else:
        raise Exception('wrong input')
    if sort:
        s.sort()  # 现场排序，改变list的值
    return s

# 调用时需要按位置提供所有参数值，即使有默认值也不能省略
l = ['World', 'Hello']
print(trans_1('lower', True, *l))
# 错误的调用
# print(trans_1(*l))
# print(trans_1(sort=True, case='upper', *l))
# print(trans_1('upper', *l))
# print(trans_1(False, *l))


# 使用可变参数+关键字参数的解决方案：定义时复杂，调用时有缺陷
def trans_2(*args, **kwargs):
    s = list(args)
    if 'case' in kwargs:  # 需要逐一检测传入的关键字参数
        if kwargs['case'] == 'lower':
            for i in range(len(s)):
                s[i] = s[i].lower()  # lower()返回copy，不改变变量的值
        elif kwargs['case'] == 'upper':
            for i in range(len(s)):
                s[i] = s[i].upper()
        elif kwargs['case'] == 'capitalize':
            for i in range(len(s)):
                s[i] = s[i].capitalize()
        else:
            raise Exception('wrong input')
    if 'sort' in kwargs:
        if kwargs['sort']:
            s.sort()  # 现场排序，改变list的值
    return s

l = ['World', 'Hello']
print(trans_2(*l))
print(trans_2(*l, sort=True, case='lower'))
# 无法指定参数的默认值
print(trans_2(*l, case='lower'))
print(trans_2(*l, sort=True))
# 无法控制传入的参数
print(trans_2(*l, wrong_arg=True))


# 使用仅关键字参数的解决方案：定义时简单，调用时简单
def trans_3(*args, case='lower', sort=True):
    s = list(args)
    if case == 'lower':
        for i in range(len(s)):
            s[i] = s[i].lower()  # lower()返回copy，不改变变量的值
    elif case == 'upper':
        for i in range(len(s)):
            s[i] = s[i].upper()
    elif case == 'capitalize':
        for i in range(len(s)):
            s[i] = s[i].capitalize()
    else:
        raise Exception('wrong input')
    if sort:
        s.sort()  # 现场排序，改变list的值
    return s

l = ['Hello', 'World']
print(trans_3(*l))
print(trans_3(*l, sort=True, case='lower'))
# 未出现的关键字参数有默认值
print(trans_3(*l, case='lower'))
print(trans_3(*l, sort=True))
# 能避免传入错误的参数
# print(trans_3(*l, wrong_arg=True))


# 仅关键字参数的第二种方式：确定的普通参数+确定的额外选项
def person(name, phone_no, *, city='Beijing', age=0):
    print('Personal Info:')
    print('name:', name)
    print('phone_no:', phone_no)
    print('city:', city)
    print('age:', age)

# 仅关键字参数如果有默认值，调用时可省略
person('Michael', 1391)
person('Michael', 1391, age=11)
# 位置参数在前，保证顺序，仅关键字参数在后，可打乱顺序
person('Bob', 1234, age=22, city='Shanghai')
# 可防止错误参数传入
# person('Adam', 5678, gender='M', job='Engineer')

# 通过参数序列解包，可以将dict拆解，再传入函数
extra = {'city': 'Shanghai', 'age': 11}
person('Jack', 1234, city=extra['city'], age=extra['age'])
person('Jack', 5678, **extra)

# 错误的调用方法
# person('Jack', **extra, 1234)
# person(phone_no=5678, 'Jack', **extra)


# 为什么不能用一个list或tuple表示所有可变参数：
# list可变对象不能作为参数，重复调用会出问题
# 调用之前还需要将要传入的值组装成序列，麻烦
def func(l=[]):
    l.append('end')
    print(l)

l1 = ['a', 'b']
func(l1)
print(l1)
func(l1)
