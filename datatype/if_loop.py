#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 什么是true和false
if False or None or 0 or "" or () or [] or {}:
    print('True')
else:
    print('All of them are FASLE!')

if True and 1 and 'abc' and (1, 2, 3) and {'x': 1, 'y': 2}:
    print('All of them are TRUE!')


# 比较操作符
# =是赋值，==是比较
a, b = 1, 2
if a == b:
    print('a is equal to b')
else:
    print('a is not equal to b')

# is同一性运算符，==是判断两个对象的值是否相等，is是判断是否是同一个对象
# x和y是两个变量指向的同一个对象
# x和z是两个变量指向的不同对象，虽然值相同
x = y = [1, 2, 3]
z = [1, 2, 3]
print(x == y, x == z, x is y, x is z, x is not z)

# in成员运算符
print('ll' in 'hello')

# 字符串和序列的比较
# 字符串比较规则：从左向右，诸位按照二进制编码的大小进行比较，和数值比较规则不同
# 序列比较规则：从第一个元素开始，逐个元素比较
print(12 > 3, '12' > '3', 'a' > 'bc', [1, 2] > [2, 1])

# 同类型数值才可进行比较
# input()返回的数据类型是str，str不能直接和整数比较，必须先把str转换成整数
s = input('birth: ')
birth = int(s)
if birth < 2000:
    print('00前')
else:
    print('00后')


# python的逻辑关系是通过缩紧表示的
# 如果if语句判断是True，就把缩进的两行print语句执行了，注意冒号：
age = 20
if age >= 18:
    print('your age is', age)
    print('adult')

age = 3
if age >= 18:
    print('your age is', age)
    print('adult')
else:
    print('your age is', age)
    print('teenager')

age = 3
if age >= 18:
    print('adult')
elif age >= 6:
    print('teenager')
else:
    print('kid')

age = 50
if 0 <= age <= 100:  # 连接比较，相当于其他语言中的between and表示的闭区间
    print('your age is', age)
else:
    print('wrong input')


# assert断言：当某些条件不满足时，直接打断程序的运行
age = -1
assert 0 <= age <= 100, 'the age must be realistic'


# for/while循环
names = ['Michael', 'Bob', 'Tracy']
for name in names:
    print(name)

s = 0
for x in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
    s += x
print(s)

s = 0
n = 99
while n > 0:
    s += n
    n -= 2
print(s)

# range()函数，可以生成一个整数序列(0, n-1)（包含下限，不包含上限），range()函数的下限默认是0
# range()返回可迭代对的对象，只能提供给循环语句使用，通过list()函数可以转换为list
print(list(range(5)))
s = 0
for x in range(101):
    s = s + x
print(s)

# 利用序列解包遍历字典元素，字典是无序的，所以遍历不能保证顺序
# 如果顺序很重要，可以先将key提取出来保存成list，排序后再访问字典中的value
d = {'x': 1, 'y': 2}
for key, value in d.items():
    print('key is: ', key, 'value is:', value)


# 循环中用到的迭代工具
# 并行迭代
names = ['anne', 'bob', 'charles']
ages = [11, 22, 33]
for i in range(len(names)):
    print(names[i], 'is', ages[i])
for name, age in zip(names, ages):
    print(name, 'is', age)

# 在序列中进行查找替换时，使用enumerate()可以将序列变为"索引-值"对，更方便定位
strings = ['aaa', 'bbb', 'ddd', 'ccc']
index = 0
for string in strings:
    if 'bbb' in string:
        strings[index] = 'censord'
    index += 1
print(strings)
# enumerate()返回可迭代对象，只能在循环中使用，可通过list()函数转换成list查看
strings = ['aaa', 'bbb', 'ddd', 'ccc']
print(list(enumerate(strings)))
for index, string in enumerate(strings):
    if 'bbb' in string:
        strings[index] = 'censored'
print(strings)

# sorted返回排序后的序列，不是in place原地修改，原序列不变
# reversed()返回一个逆序的迭代对象，只能在循环中使用
strings = ['aaa', 'bbb', 'ddd', 'ccc']
for string in sorted(strings):
    print(string)
for string in reversed(strings):
    print(string)


# break/continue
# break符合条件跳出循环，continue符合条件开始下一次循环（用得很少）
from math import sqrt
for i in range(99, 0, -1):
    root = sqrt(i)
    if root == int(root):
        print(i)
        break

# while True/break习语
while True:
    word = input('Please input a word: ')
    if not word:
        break
    print('the word is', word)
# 其他低效率的写法
word = input('Please input a word: ')
while word:
    print('the word is', word)
    word = input('Please input a word: ')


# for/else（while/else）结构：
# 当循环语句正常退出时，执行else语句，如果break跳出，则不执行
# 用来代替标志位变量
from math import sqrt
for n in range(99, 81, -1):
    root = sqrt(n)
    if root == int(root):
        print(n)
        break
else:  # 注意缩进，不是if语句的else
    print('not found!')
# 常规写法
broke_out = False
for n in range(99, 81, -1):
    root = sqrt(n)
    if root == int(root):
        broke_out = True
        print(n)
        break
if not broke_out:
    print('not found!')


# 列表表达式
print([x*x for x in range(10)])
print([x*x for x in range(10) if x % 3 == 0])
print([(x, y) for x in range(3) for y in range(3)])
matrix = [[1, 2, 3, 4],
          [5, 6, 7, 8],
          [9, 10, 11, 12]]
print([[row[i] for row in matrix] for i in range(4)])
# 常规写法
transposed = []
for i in range(4):
    # the following 3 lines implement the nested listcomp
    transposed_row = []
    for row in matrix:
        transposed_row.append(row[i])
    transposed.append(transposed_row)
# 使用内置函数
print(list(zip(*matrix)))


# pass表示空语句
age = 11
if age > 0:
    # 未完成
    pass
else:
    print('wrong!')
