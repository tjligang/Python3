Python基础

[TOC]

> 
 - 条件与循环
 - 字典dict和集合set

# 输入/输出

> 
 - [廖雪峰python教程-输入和输出][1]

# 数据类型和变量

# 列表list和元组tuple

Python中常用的序列有：list、tuple、range和str。

##  通用序列操作

通用序列操作不会改变序列，适用于所有序列类型。

> 
 - [Python Doc : Common Sequence Operations][2]
 
## 可变序列操作
 
 可变序列操作会改变序列中的值，适用于可读写的序列，比如list。list在此基础上还增加了排序等操作。
 
 > 
 - [Python Doc : Mutable Sequence Types][3]
 - [Python Doc : Lists][4]

# 字符串

## 编码的背景知识

> 
 - [廖雪峰python教程-字符串和编码][5]
 - [unicode编码简介][6]
 - [学点编码知识又不会死：Unicode的流言终结者和编码大揭秘][7]
 - [从字节理解Unicode（UTF8/UTF16)][8]
 - [utf-8与utf-8(无BOM)的区别][9]
 - [理性看待utf-8 BOM][10]

windows记事本会在文件开始的地方加上几个特殊字符（UTF-8 BOM），结果会导致程序运行出现莫名其妙的错误。

## 字符串方法

> 
 - [Python doc : string method][11]

## 格式化输出

> 
 - [Python doc : printf][12]

# 字典dict和集合set

字典dict和序列list、集合set的比较，对于不可变对象的理解，参考廖雪峰教程：

> 
 - [廖雪峰python教程-使用dict和set][13]


  [1]: http://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/001431643484137e38b44e5925440ec8b1e4c70f800b4e2000
  [2]: https://docs.python.org/3/library/stdtypes.html#common-sequence-operations
  [3]: https://docs.python.org/3/library/stdtypes.html#mutable-sequence-types
  [4]: https://docs.python.org/3/library/stdtypes.html#lists
  [5]: http://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/001431664106267f12e9bef7ee14cf6a8776a479bdec9b9000
  [6]: http://www.cnblogs.com/hongfei/p/3648794.html
  [7]: http://www.freebuf.com/articles/web/25623.html
  [8]: http://www.cnblogs.com/zizifn/p/4716712.html
  [9]: http://afericazebra.blog.163.com/blog/static/30050408201211199298711/
  [10]: https://www.zhihu.com/question/20167122
  [11]: https://docs.python.org/3/library/stdtypes.html#string-methods
  [12]: https://docs.python.org/3/library/stdtypes.html#printf-style-string-formatting
  [13]: http://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/00143167793538255adf33371774853a0ef943280573f4d000