#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 通用的序列操作：
# 适用于所有序列：list、tuple和string，不改变序列
# 索引indexing、分片slicing、加adding、乘multiply ing、成员资格、长度、最大值/最小值
# 以下实例以list为例，也适用于tuple和string

# 通过索引获取序列元素
l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(l, len(l))
print(l[0], l[1], l[2])
print(l[-1], l[-2], l[-3])
# print(l[10], l[-11])索引超出了范围，最后一个元素的索引可使用len(l) - 1

# 字符串是一个由字符组成的序列，能直接使用索引，无需变量引用
print('hello'[1], str(2005)[1])

# 分片3中方式：[][:][::]
# [n]获取单个元素
print(l[1], l[-1])
# [n:m]从n开始，到m-1结束，不包括m，n<m，不能逆序
print(l[1:5], l[-3:-1])
# m=-1时分片不包含最后一个元素，如果包含最后一个元素，m=len(l)+1，或空着不写
# 默认n=0,m=len(l)+1
print(l[1:-1], l[1:11], l[1:], l[:3], l[:])
# [n:m:i]i是步长
# i>0，从左向右扫描列表，n起始元素的索引（相对左边），m是结束元素的索引（相对右边），n<m
# i<0，从右向左扫描列表，n起始元素的索引（相对右边），m是结束元素的索引（相对左边），n>m
print(l[1:9:1], l[1:9:2])
print(l[9:1:-1], l[9:1:-2], l[-1:-9:-2])
# 所有偶数位、奇数位元素，逆序输出列表
print(l[::2], l[1::2], l[::-1])

# 序列相加
l1 = [1, 2, 3]
l2 = [4, 5, 6]
l3 = ['a', 'b', 'c']
# 相同类型的序列（都是列表list）才能相加，l1和l3包含的元素类型不一致，会给出警告，但可以相加
print(l1+l2, l1+l3)
# print(l3+'aaa')列表list和字符串不能相加，虽然都是序列，但不是相同类型
print(l3+list('aaa'))

# 序列相乘
print(l*3)
# 空序列初始化的陷阱
# l是一个包含一个元素的非空列表，这个元素是一个空列表，元素是一个变量，指向一个列表list，list当前没有元素，是空列表list
l = [[]]
print(l)
# l1序列被重复3次，即这个元素被重复3次，这3个元素是3个变量，都指向一个内存区域
l = [[]]*3
print(l)
# 通过一个元素变量向内存中的list对象赋值，因为3个变量都指向同一个list，所有的元素值都被改变
l[0].append(1)
print(l)
# 序列相乘是复制多个变量，但都指向同一个内存区域，通过一个变量修改内存区域，会影响其他变量，类似unix的硬指针
l = [[1], [2], [3]]*3
print(l)
l[0].append(1)
print(l)
# 避免序列相乘导致指向同一内存区域的效果
l = [[] for i in range(3)]
l[0].append(3)
l[1].append(5)
l[2].append(7)
print(l)

# 成员资格
l = [1, 2, 3]
print(1 in l)
l = ['Michael', 'Bob', 'Tracy']
print('bob' in l)
# 字符串是序列，也可使用in进行判断
print('ll' in 'hello')

# 长度、最大值、最小值
l = [7, -3, 10]
print(len(l), max(l), min(l))
# min/max可以直接将多个数字作为参数，并不一定使用list
print(max(7, -3, 10))
# count返回元素出现的次数
print('hello, world'.count('l'))


# 可变序列操作：
# 适用于可变序列list，list是可变对象，所有可变序列操作都会导致list本身改变
# list是一种有序的集合，可以随时添加和删除其中的元素,list用[]定义
# list()函数进行类型转换
l = list('hello')
print(l)
l[0] = 'H'  # 元素赋值
print(l)
del l[2]  # 删除元素
print(l)
l[2:2] = 'l'  # 分片赋值
print(l)
l[4:] = ', world'
print(l)

# list是一个可变的有序表，各种操作方法：
l = ['a', 'b', 'c']
l.append('c')  # 追加元素到末尾
print(l)
print(l.count('c'))  # 统计元素出现的次数
l2 = ['d', 'e', 'f']
l.extend(l2)  # 追加新的list
print(l)
print(l.index('c'))  # 查找元素第一个匹配项的index值
l.insert(1, 'x')  # 把元素插入到指定的位置，可读性比分片操作好
print(l)
l.pop()  # 删除list末尾的元素
print(l)
l.pop(1)  # 删除指定位置的元素
print(l)
l.remove('c')  # 删除该值的第一个匹配项
print(l)
l.reverse()  # 逆序输出，list被改变
print(l)

# 排序
l = ['b', 'a', 'c']
l.sort()  # 原位排序，list被改变
print(l)
l.sort(reverse=True)  # 逆序排序，list被改变
print(l)
# 原list不变，需要一个排好序的list副本
l1 = l.sort()  # 错误。原位排序，方法正常运行后，返回None
print(l1)
l = ['b', 'a', 'c']
# 不能写成l1 = l，会导致两个变量l和l1都指向同一个list，对l1排序，l也改变
# 可以写成l1 = sorted(l)，获取已排序列表的副本
l1 = l[:]
l1.sort()
print(l, l1)

# list里面的元素的数据类型可以不同
l = ['Apple', 123, True]
# list元素也可以是另一个list
l = ['python', 'java', ['asp', 'php'], 'scheme']
print(len(l))  # s只有4个元素，其中s[2]又是一个list
# 二维list更好理解的写法：
p = ['asp', 'php']
l = ['python', 'java', p, 'scheme']
print(p[1], l[2][1])


# 元组tuple一旦初始化就不能修改，是不可变对象，支持所有通用序列操作
# 用逗号分隔的一组值就是tuple，tuple的关键是逗号，()可以不用。查看方法和list一样。
t = ('Michael', 'Bob', 'Tracy')  # 也可写成t = 'Michael', 'Bob', 'Tracy'
print(t)
# tuple()函数进行类型转换，将list和string转换成tuple
print(tuple([1, 2, 3]), tuple('abc'))
# 定义一个tuple时，tuple的元素就必须被确定下来
# 多个元素的tuple
t = (1, 2)  # t = 1, 2
print(t)
# 空tuple
t = ()
print(t)
# 只有1个元素的tuple，如果写成t = (1)的话，()被认为是数学公式中的小括号
t = (1,)  # t = 1,
print(t)

# “可变”的tuple
# tuple的元素确实变了，但其实变的不是tuple的元素，而是list的元素。
# tuple一开始指向的list并没有改成别的list，所以，tuple所谓的“不变”是说，tuple的每个元素，指向永远不变。
# 即指向'a'，就不能改成指向'b'，指向一个list，就不能改成指向其他对象，但指向的这个list本身是可变的！
t = ('a', 'b', ['A', 'B'])
t[2][0] = 'X'
t[2][1] = 'Y'
print(t)


# None和空列表的区别
# None是一个特殊的变量，有自己的数据类型NoneType，指向的内存区域没有被赋值，可理解成空值，但变量本身是存在的
# l1的第一个元素是None，这个元素指向的内存区域没有被赋值
l = [None]
print(len(l))  # len为1，不是空list
# 第二个元素的值为1
l.append(1)
print(l)
# 空列表，一个元素都没有
l = []
print(len(l))  # len为0，空list
# 第一个元素的值为1
l.append(1)
print(l)
# 以下试图定义空列表的语句是错误的，None的数据类型是NoneType，不支持任何运算也没有任何内建方法
# l = None 或者 l = list(None)
# print(len(l))

# 序列相乘中的None和空列表
# l有一个元素[None]，这个元素是一个list，list中包含一个元素None，这个元素指向的内存区域没有被赋值
l = [[None]]
print(l1)
# l序列被重复3次，l中所有元素（就是[None]）被重复3次，l中有个3元素变量都指向同一个list列表（同一个内存区域）
l = [[None]]*3
print(l1)
# 通过一个元素变量向内存中的list对象赋值，因为3个变量都指向同一个list，所有的元素值都被改变
l[0].append(1)
print(l)
l[0][0]=1
print(l)
# l是一个包含一个元素的非空列表，这个元素是一个空列表
# 元素是一个变量，指向一个列表list，list当前没有元素，是空列表list
l = [[]]
print(l1)
# l序列被重复3次，即这个列表中所有元素（[]）重复3次，新的l中这3个元素是3个变量，都指向同一个list（同一个内存区域）
l = [[]]*3
print(l)
# 通过一个元素变量向内存中的list对象赋值，因为3个变量都指向同一个list，所有的元素值都被改变
l[0].append(1)
print(l)
