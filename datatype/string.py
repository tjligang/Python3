#!/usr/bin/env python3
# -*- coding: utf-8 -*-

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
s = 'a\nb\tc'
print(s, len(s))  # 转义符\n算一个字符

# 为了简化，用r''表示''内部的字符串默认不转义，表示文件系统或写正则表达式时非常有用
print(r'\\\t\\')
print('C:\nowhere')
print(r'C:\nowhere')
print('C:\\abc\\def\\xyz')
print(r'C:\abc\def\xyz')
# print(r'C:\abc\def\xyz\')最后一个\被python误认为是跨行标记，会报错
print(r'C:\abc\def\xyz'+'\\')
print('C:\\abc\\def\\xyz\\')
print(r'C:\abc\def\xyz\\'[:-1])

# 用'''...'''的格式表示多行内容（长字符串），代替\n，可以和r配合
print('''line1
line2
line3''')
print(r'''line1's
line2's
line3's''')







# Python 3版本中，字符串是以Unicode编码的，也就是说，Python的字符串支持多语言
print('包含中文的str')
# 对于单个字符的编码，Python提供了ord()函数获取字符的对应unicode十进制整数表示
# chr()函数把unicode十进制整数编码转换为对应的字符
# 还可以用十六进制表示字符
print(ord('A'), ord('中'), chr(66), chr(25991), '\u0041\u0042', '\u4e2d\u6587')

# 由于Python的字符串类型是str，在内存中以Unicode表示，一个字符对应若干个字节
# 如果要在网络上传输，或者保存到磁盘上，就需要把str变为以字节为单位的bytes
# Python对bytes类型的数据用带b前缀的单引号或双引号表示：
x = b'ABC'

# Unicode表示的str通过encode()方法可以编码为指定的bytes
# 把bytes变为str，用decode()方法
print('ABC'.encode('ascii'), 'ABC'.encode('utf-8'), '中文'.encode('utf-8'))
# print('中文'.encode('ascii'))中文unicode编码无法直接转换为ascii码
print(b'ABC'.decode('ascii'), b'ABC'.decode('utf-8'), b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8'))

# len()函数计算的是str的字符数，如果换成bytes，len()函数就计算字节数
# 1个中文字符经过UTF-8编码后通常会占用3个字节
print(len('ABC'), len('中文'), len(b'ABC'), len(b'\xe4\xb8\xad\xe6\x96\x87'), len('中文'.encode('utf-8')))


# 字符串方法：字符串是不可变对象，所有方法不改变自身的值，只返回一个copy
# find返回index，没有则返回-1, 截至到end-1，不包括第二个index
s = 'Python'
print(s.find('on'), s.find('py'), s.find('th', 1, 3))

# split和join
# split将字符串按照指定符号分割成序列
path = '/usr/bin/env'
sep = '/'
print(path.split(sep), path)
path = 'C:\\usr\\bin\\env'
sep = '\\'
print(path.split(sep))
# join使用指定符号将字符串连接序列
dirs = '', 'usr', 'bin', 'env'  # dirs是tuple
sep = '/'
print(sep.join(dirs))  # 在tuple的元素之间用'/'分隔，注意dirs第一个元素是空，不是空格
dirs = 'C:', 'usr', 'bin', 'env'
sep = '\\'
print(sep.join(dirs))
# join只能连接字符串，数字必须加''变为字符串才能join
s = ['1', '2', '3', '4', '5']
sep = '+'
print(sep.join(s))

# 大小写转换
s = 'Hello, world'
print(s.lower(), s.upper(), s.title())
# 替换
print(s.replace('world', 'python'))
# 去除字符串两侧的空格或指定字符
s = '  !**!Hello, !**! world!**!  '
print(s.strip())
print(s.strip(' !*'))


# printf方式格式化：format % values
print('Hello, %s' % 'world')
print('Hi, %s, you have $%d.' % ('Michael', 1000000))
print('%2d-%02d' % (3, 1))
print('%.2f' % 3.1415926)
# 如果你不太确定应该用什么，%s永远起作用，它会把任何数据类型转换为字符串：
print('Age: %s. Gender: %s' % (25, True))
# 正文中出现%，使用转义符%%表示一个%
print('growth rate: %d %%' % 7)
