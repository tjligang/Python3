#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# list是顺序查找，list越大，查找越慢
names = ['Michael', 'Bob', 'Tracy']
scores = [95, 75, 85]
print(scores[names.index('Michael')])
# dict使用键-值（key-value）存储，通过key找value，具有极快的查找速度
# dict使用{}定义
d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
print(d['Michael'])

# dict中的value可以在初始化之后，通过key放入，并可以被修改
d['Adam'] = 67
print(d['Adam'])
d['Jack'] = 90
print(d['Jack'])
d['Jack'] = 88
print(d['Jack'])

# print(d['Thomas'])不存在的key会报错
# 通过in判断key是否存在
print('Thomas' in d)
# get方法：如果key不存在，可以返回None，或者返回指定的value
print(d.get('Thomas'), d.get('Thomas', -1))
# 删除一个key，用pop(key)方法，对应的value也会从dict中删除：
d.pop('Bob')
print(d)

# dict的key必须是不可变对象
# 字符串、整数等都是不可变的，可以放心地作为key。而list是可变的，就不能作为key
# key = [1, 2, 3]
# d[key] = 'a list'     报错

# set和dict类似，也是一组key的集合，但不存储value。由于key不能重复，所以，在set中，没有重复的key
# set使用()定义
# 创建一个set，需要提供一个list作为输入集合
s = set([1, 2, 3])
# 显示的顺序不表示set是有序的
print(s)
# 重复元素在set中自动被过滤
s = set([1, 1, 2, 2, 3, 3])
print(s)
# add(key)方法可以添加元素到set中，可以重复添加，但不会有效果
s.add(4)
print(s)
s.add(4)
print(s)
# remove(key)方法可以删除元素
s.remove(4)
print(s)

# set可以看成数学意义上的无序和无重复元素的集合，因此，两个set可以做数学意义上的交集、并集等操作
s1 = set([1, 2, 3])
s2 = set([2, 3, 4])
print(s1 & s2)
print(s1 | s2)

# dict和set的key只能放入不可变对象
# list是可变对象
a = ['c', 'b', 'a']
a.sort()
print(a)
# str是不变对象
a = 'abc'
a.replace('a', 'A')
print(a)
'abc'
# a本身是一个变量，它指向的对象的内容才是'abc'
a = 'abc'
b = a.replace('a', 'A')
print(b)
print(a)

# 在dict中加入（1，2，3）不会报错，
# 因为"(1,2,3)"是一个元组，同时元组内的“1”“2”“3”是整数，也就是不可更改对象。
# 而插入"(1,[2,3])"会报错返回报错“TypeError: unhashable type: 'list'”
# 因为"(1,[2,3])"虽然是元组，但是“[2,3]”是list，所以不符合不可更改对象。
# 同理，set中加入(1,2,3)不会报错，而加入(1,[2,3])会出现上述相同的报错

#将tuple（1，2，3）放入dict中
d={'Michael': 95, 'Bob': 75, 'Tracy': 85}
key=(1,2,3)
d[key]=78
print(d)
#result:{'Tracy': 85, 'Michael': 95, 'Bob': 75, (1, 2, 3): 78}

#将tuple（1，[2,3]）放入dict中
d={'Michael': 95, 'Bob': 75, 'Tracy': 85}
key=(1,[2,3])
# d[key]=78
print(d)
#result:TypeError: unhashable type: 'list'  不hash
#explain: 虽然是不可变的元组，但是元组中key有可变的列表，所以导致不hash。报错。

#将tuple（1，2，3）放入set中
s=set(['Michael', 'Bob', 'Tracy'])
key=(1,2,3)
s.add(key)
print(s)
#result:{'Tracy', 'Michael', 'Bob', (1, 2, 3)}

#将tuple（1，[2,3]）放入dict中
s=set(['Michael', 'Bob', 'Tracy'])
key=(1,[2,3])
# s.add(key)
print(s)
#result:TypeError: unhashable type: 'list'  不hash
#explain: 虽然是不可变的元组，但是元组中key有可变的列表，所以导致不hash。报错。
