Python基础

[TOC]

# 输入/输出

> [廖雪峰python教程-输入和输出][1]

# 数据类型和变量

> [廖雪峰：数据类型和变量][2]

# 列表list和元组tuple

Python中常用的序列有：list、tuple、range和str。

##  通用序列操作

通用序列操作不会改变序列，适用于所有序列类型。

> [Doc : Common Sequence Operations][3]

## 可变序列操作

 可变序列操作会改变序列中的值，适用于可读写的序列，比如list。list在此基础上还增加了排序等操作。

> [Doc : Mutable Sequence Types][4]
> [Doc : Lists][5]

# 字符串

## 编码的背景知识

> [廖雪峰python教程-字符串和编码][6]
> [unicode编码简介][7]
> [学点编码知识又不会死：Unicode的流言终结者和编码大揭秘][8]
> [从字节理解Unicode（UTF8/UTF16)][9]
> [utf-8与utf-8(无BOM)的区别][10]
> [理性看待utf-8 BOM][11]

windows记事本会在文件开始的地方加上几个特殊字符（UTF-8 BOM），结果会导致程序运行出现莫名其妙的错误。

## 字符串方法

字符串是不可变对象，支持所有通用序列操作，并提供额外的字符串方法。因为字符串不可改变，所有方法不会改变字符串自身的值，只是返回一个copy。

> [Doc : string method][12]

## 格式化输出

> [Doc : printf][13]

# 条件与循环

列表推导式list comprehension参考以下范例：
> [Doc : list comprehension][14]

# 字典dict和集合set

字典dict和序列list、集合set的比较，对于不可变对象的理解，参考廖雪峰教程：

> [廖雪峰python教程-使用dict和set][15]

# 可变对象/不可变对象

Python中的**变量**和**对象**。 

 - 变量：Python中的变量是没有类型的，我们可以把它看做一个(*void)类型的指针，变量是可以指向任何对象的，而对象才是有类型的。变量中保存的是对象的内存地址。 
 - 对象：Python中的对象是一个内存空间，其中保存数据，根据内存区域是否可以被修改，分为可变对象（list，dict等）和不可变对象（number，string，tuple等）。

## 赋值
 
 - `var = value`

变量的赋值就是将对象的内存地址保存在变量中，即变量指向对象。

 - `var1 = var2`

两个变量之间赋值，`var2`中的对象地址复制给`var1`，结果两个变量指向同一个对象。对于可变对象，这样的赋值会导致通过变量`var1`修改对象，变量`var2`也随之改变。

 - `var1 = value` `var2 = value`

两个变量分别被赋予相同的值，对于
不可变对象：因为对象不会被改变，`var1` `var2`保存同一对象的地址，即指向同一对象。这样能够节省内存。
可变对象：为防止对象通过其它变量修改，内存中有两个对象，值都是`value`，`var1` `var2`分别保存一个对象的地址，即指向不同对象。

## 修改

不可变对象（number，string，tuple）：因为对象不可变，所有修改对象的方法都会创建原始对象的复本，对复本修改，并返回复本的内存地址。这些方法的返回值是一个新对象的地址，即返回不可变对象修改后的copy，而原始对象不变。

可变对象（list，dict）：因为对象可变，所有修改对象的方法都直接对原始对象进行修改，原始对象被改变，即in place现场修改。这些方法返回None。

  [1]: http://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/001431643484137e38b44e5925440ec8b1e4c70f800b4e2000
  [2]: http://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/001431658624177ea4f8fcb06bc4d0e8aab2fd7aa65dd95000
  [3]: https://docs.python.org/3/library/stdtypes.html#common-sequence-operations
  [4]: https://docs.python.org/3/library/stdtypes.html#mutable-sequence-types
  [5]: https://docs.python.org/3/library/stdtypes.html#lists
  [6]: http://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/001431664106267f12e9bef7ee14cf6a8776a479bdec9b9000
  [7]: http://www.cnblogs.com/hongfei/p/3648794.html
  [8]: http://www.freebuf.com/articles/web/25623.html
  [9]: http://www.cnblogs.com/zizifn/p/4716712.html
  [10]: http://afericazebra.blog.163.com/blog/static/30050408201211199298711/
  [11]: https://www.zhihu.com/question/20167122
  [12]: https://docs.python.org/3/library/stdtypes.html#string-methods
  [13]: https://docs.python.org/3/library/stdtypes.html#printf-style-string-formatting
  [14]: https://docs.python.org/3/tutorial/datastructures.html#more-on-lists
  [15]: http://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/00143167793538255adf33371774853a0ef943280573f4d000