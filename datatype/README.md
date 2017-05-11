tags: 数据类型

[TOC]

# 动态类型

> 《Python学习手册》第5章

Python中，数据是以对象的形式出现的，数据类型就是对象的类型。一旦创建对象，就和对应的操作集合绑定了，不同数据类型上的操作就是不同对象类型所对应的操作集合。

## 变量、对象和引用

 - 变量(variable)：Python中的变量是没有类型的，我们可以把它看做一个(*void)类型的指针，变量是可以指向任何对象的，而对象才是有类型的。变量中保存的是对象的内存地址。 
 - 对象(object)：Python中的对象是一个内存空间，其中保存数据。
 - 引用(reference)：一个从变量到对象指针，标明变量当前所关联的对象。
 
每一个对象都有两个标准头部信息：一个类型标志符标明对象的类型，一个引用计数器，标明系统是否可以回收对象。变量和对象的关系类似于linux文件系统中的目录项和inode。Python的对象垃圾回收是基于引用计数器自动完成的。对象根据内存区域是否可以被修改，分为可变对象（list，dict等）和不可变对象（number，string，tuple等）。


## 对象属性

 - identity：对象的唯一标示，通过id()获取（CPython返回的是对象的内存地址）。
 - type：对象的类型，决定对象上支持的操作，通过type()获取。
 - value：在内存中保存的对象的值，根据是否可以被修改，分为可变对象和不可变对象。

> [Doc: objects, types, values][1]


Python所有的数据类型都是对象：

> [Doc: The standard type hierarchy][2]

## 对象操作

### 赋值
 
 - `var = value`

变量的赋值就是将对象的内存地址保存在变量中，即变量指向对象。

 - `var1 = var2`

两个变量之间赋值，`var2`中的对象地址复制给`var1`，结果两个变量指向同一个对象，这被称作**共享引用**。对于可变对象，这样的赋值会导致通过变量`var1`修改对象，变量`var2`的值也随之改变。

 - `var1 = value` `var2 = value`

两个变量分别被赋予相同的值，对于
不可变对象：因为对象不会被改变，`var1` `var2`保存同一对象的地址（指向同一对象）。通过共享引用节省内存（CPython的实现方式）。
可变对象：为防止对象通过其它变量修改，内存中有两个对象，值都是`value`，`var1` `var2`分别保存一个对象的地址，即指向不同对象。如果希望通过`var1`给`var2`快速赋值，但又不想成为共享引用，可以使用对象的内置方法或copy模块。

### 修改

不可变对象（number，string，tuple）：因为对象不可变，所有修改对象的方法都会创建原始对象的复本，对复本修改，并返回复本的内存地址。这些方法的返回值是一个新对象的地址，即返回不可变对象修改后的copy，而原始对象不变。

可变对象（list，dict）：因为对象可变，所有修改对象的方法都直接对原始对象进行修改，原始对象被改变，即in place现场修改。这些方法返回None。

### 比较

 - `var1 == var2` `var1 is var2`

`==`判断两个对象的值是否相同，`is`判断两个变量是否指向同一个对象。因为使用共享引用节省内存资源，不可变对象的值相同，就指向同一个对象（CPython实现），对于可变对象则不是。

# number

## 数字类型

数字类型的背景知识：

> [百度百科：复数][3]
> [百度百科：实数][4]

Python中各种数字类型的继承关系：
Number :> Complex :> Real :> Rational :> Integral
Rational :> fraction
Decimal是独立的类，和Number没有继承关系。

> [PEP 3141][5]

Python支持的所有数字类型：

> [Doc: Numeric Types — int, float, complex][6]
> 《Python学习手册》 P117

## int（整数）

Python3的整数支持无穷精度（由内存决定），可以使用各种进制表示。Python2中的长整数L被废弃。

## float（浮点数）

实数（real）在Python中浮点类型（float）来近似表示，float类型使用64位表示，相当于c++中的双精度类型（double）。

> [计算机组成原理：数据格式][7]
> [百度百科：IEEE754][8]
> [IEEE 754-2008][9]

为什么`0.1+0.1+0.1-0.3 != 0`？

> [Doc: Floating Point Arithmetic: Issues and Limitations][10]
> [为什么说浮点数缺乏精确性？python中浮点数运算问题][11]

## 类型转换

 - 自动类型转换
不同数字类型混合运算时，Python按照类型的复杂度，先将简单类型转换为复杂类型，再进行运算，最终结果为复杂类型。Python复杂度从简单到复杂的顺序为：整数--浮点数--复数。

 - 手动类型转换
通过函数`int()`和`float()`手动进行类型转换。简单->复杂，通常是不需要的。复杂->简单，会丢失精度或报错。

不同数值类型不能自动转换，比如整数和字符串。

## 变量、操作符和表达式

Pyhton的操作符：

> 《Python学习手册》 P120

Pyhton的变量是动态类型，不需提前声明，也不需回收。

> 《Python学习手册》 P125

## 除法

 - 真除法x/y
无论任何类型（整数和浮点数）的除法，计算结果都**保持**小数部分，即结果是浮点数。即使两个整数进行整除，结果也是浮点数。
 - floor除法x//y
无论任何类型（整数和浮点数）的除法，计算结果都**省略**小数部分，只保留小于计算结果的整数值。如果参与计算的都是整数，结果就是整数格式，如果参与计算的有浮点数，结果就用浮点数格式。floor除法相当于对计算结果进行向下取整，不是四舍五入round，也不是截断trunc。

Python2中的传统除法（对整数进行floor除法省略小数，对浮点数进行真除法保持小数）被取消。

> 《Python学习手册》 P129
> [PEP 238 -- Changing the Division Operator][12]
> [Python 为什么不解决四舍五入(round)的“bug”？][13]

## 内置函数与模块

> 《Python学习手册》 P137

## Decimal

float是通过二进制近似表示十进制，不能用于需要精确计算的应用，比如金融。为此IEEE在IEEE 754-2008中定义了以十进制保存数字的decimal格式，可用于精确计算。Python提供了decimal模块来实现。

decimal模块3个概念：

 - the decimal number
包括sign, coefficient digits, and an exponent 3部分。
 - the context for arithmetic
定义decimal类型进行算术计算的上下文环境
 - signals
对特定操作定义信号

> [Doc: decimal][14]

## fraction

fraction分数类型明确保留分子和分母，避免了浮点运算的不精确，对应有理数。

> [Doc: fractions — Rational numbers][15]

fraction与float混合计算：

> 《Python学习手册》 P143

## 布尔类型

布尔类型的True和False是整数1和0不同显示形式。

# 字符串

## 编码的背景知识

> [廖雪峰python教程-字符串和编码][16]
> [unicode编码简介][17]
> [学点编码知识又不会死：Unicode的流言终结者和编码大揭秘][18]
> [从字节理解Unicode（UTF8/UTF16)][19]
> [utf-8与utf-8(无BOM)的区别][20]
> [理性看待utf-8 BOM][21]

windows记事本会在文件开始的地方加上几个特殊字符（UTF-8 BOM），结果会导致程序运行出现莫名其妙的错误。

## 字符串表示

单引号、双引号、三引号、转义符、raw字符串。

三引号可以用来在代码中嵌入html代码，或者将多行语句快速转换为注释。

> 《Python学习手册》 P169
> [Doc: 转义符][22]

## 字符串方法

字符串是不可变对象，支持所有通用序列操作，并提供额外的字符串方法。因为字符串不可改变，所有方法不会改变字符串自身的值，只是返回一个copy。

> [Doc : string method][23]

## 字符串格式化

> [Doc : printf][24]


# 列表list和元组tuple

Python中常用的序列有：list、tuple、range和str。

##  通用序列操作

通用序列操作不会改变序列，适用于所有序列类型。

> [Doc : Common Sequence Operations][25]

## 可变序列操作

 可变序列操作会改变序列中的值，适用于可读写的序列，比如list。list在此基础上还增加了排序等操作。

> [Doc : Mutable Sequence Types][26]
> [Doc : Lists][27]





# 条件与循环

列表推导式list comprehension参考以下范例：
> [Doc : list comprehension][28]

# 字典dict和集合set

字典dict和序列list、集合set的比较，对于不可变对象的理解，参考廖雪峰教程：

> [廖雪峰python教程-使用dict和set][29]


  [1]: https://docs.python.org/3/reference/datamodel.html#objects-values-and-types
  [2]: https://docs.python.org/3/reference/datamodel.html#the-standard-type-hierarchy
  [3]: http://baike.baidu.com/item/%E5%A4%8D%E6%95%B0/254365
  [4]: http://baike.baidu.com/item/%E5%AE%9E%E6%95%B0/296419
  [5]: https://www.python.org/dev/peps/pep-3141/
  [6]: https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex
  [7]: https://wenku.baidu.com/view/1d7a18faff00bed5b8f31d84.html
  [8]: http://baike.baidu.com/item/IEEE%20754
  [9]: http://www.doc88.com/p-379360247751.html
  [10]: https://docs.python.org/3/tutorial/floatingpoint.html#floating-point-arithmetic-issues-and-limitations
  [11]: https://www.zhihu.com/question/25457573
  [12]: https://www.python.org/dev/peps/pep-0238/
  [13]: https://www.zhihu.com/question/20128906
  [14]: https://docs.python.org/3/library/decimal.html#module-decimal
  [15]: https://docs.python.org/3/library/fractions.html#module-fractions
  [16]: http://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/001431664106267f12e9bef7ee14cf6a8776a479bdec9b9000
  [17]: http://www.cnblogs.com/hongfei/p/3648794.html
  [18]: http://www.freebuf.com/articles/web/25623.html
  [19]: http://www.cnblogs.com/zizifn/p/4716712.html
  [20]: http://afericazebra.blog.163.com/blog/static/30050408201211199298711/
  [21]: https://www.zhihu.com/question/20167122
  [22]: https://docs.python.org/3/reference/lexical_analysis.html#string-and-bytes-literals
  [23]: https://docs.python.org/3/library/stdtypes.html#string-methods
  [24]: https://docs.python.org/3/library/stdtypes.html#printf-style-string-formatting
  [25]: https://docs.python.org/3/library/stdtypes.html#common-sequence-operations
  [26]: https://docs.python.org/3/library/stdtypes.html#mutable-sequence-types
  [27]: https://docs.python.org/3/library/stdtypes.html#lists
  [28]: https://docs.python.org/3/tutorial/datastructures.html#more-on-lists
  [29]: http://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/00143167793538255adf33371774853a0ef943280573f4d000