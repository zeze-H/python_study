'''
1.列表 元组 字符串 都是有序的
2.第一个元素的索引都是0
3.都可以通过切片的方法获取一个范围
4.都有很多共同的运算符
可变序列：列表
不可变序列：元组，字符串
'''
# 能够作用于序列的运算符和函数

# #+加号*乘号
# print([1,2,3]+[4,5,6])
# print((1,2,3)+(4,5,6))
# print("123"+"456")
# print([1,2,3]*3)
# print((1,2,3)*3)
# print("123"*3)

# # 可变序列：内容可以原地修改，对象本身不变（id 不变）
# # 不可变序列：内容不能原地修改，任何“修改”都会生成新对象（id 改变）
# #id为返回一个代表指定对象唯一标识的整数值
# s=[1,2,3]
# print(id(s))
# s*=2
# #列表是可变序列：对s进行了增量赋值，虽然内容改变了，但是id值为s并未改变，依旧是s
# print(s)
# print(id(s))
# # 元组为不可变序列：对t进行增量赋值，会产生新对象，id会改变
# t=(1,2,3)
# print(id(t))
# t*=2
# print(t)
# print(id(t))

# # is和is not:用于检测对象id值是否想等来检测是否是同一个字符串
# # 字符串是不可变对象，Python 可能对其进行驻留优化
# x="zezehuan"
# y="zezehuan"
# print(x is y)
# # 列表是可变对象，每次创建都会生成新对象
# x=[1,2,3]
# y=[1,2,3]
# print(x is y)

# # in 和not in:是否包含
# print("ze"in"zeze")
# print("huan"not in"huanhuan")


# # del 语句:用于删除一个或多个指定对象
# x="zeze"
# y=[1,2,3]
# del x,y
# #直接找不到x,y
# print(x)
# print(y)

# #del删除部分元素
# x=[1,2,3,4,5]
# del x[1:4]
# print(x)
# #切片删除:
# y=[1,2,3,4,5]
# y[1:4]=[]
# print(y)
# # del 支持对带步长的切片进行删除，而切片赋值不支持步长
# x=[1,2,3,4,5]
# del x[::2]
# print(x)
# #列表支持clear:清空列表
# x=[1,2,3,4,5]
# x.clear()
# print(x)
# y=[1,2,3,4,5]
# del y[:]
# print(y)

# #跟序列相关的一些函数:
#
# #列表list,元组tuple,字符串str相互转换:
# print(list("zeze6"))
# print(list((1,2,3,4,5)))
# print(tuple([1,2,3,4,5]))
# print(str([1,2,3,4,5]))
# print(str((1,2,3,4,5)))
#
# #min.max:对比传入参数并且返回最小/大值
# s=[1,1,2,3,5]
# print(min(s))
# #如果有字母存在,则比较编码值
# t="zeze6"
# print(max(t))
# s=[]
# print(min(s,default="空列表不支持取大取小,不要default会报错"))
# print(min(1,2,3,0,6))
# print(max(1,2,3,0,6))

# # len&sum:测数字和
# # len测长度有限制
# print(len(2**100))

# s=[1,0,0,8,6]
# print(sum(s))
# #sum内置start,相当于100+1+0+0+8+6
# print(sum(s,start=100))

# #sorted&reversed

# s=[1,2,3,0,6]
# #sorted:排从小到大排好序并返回新列表,也支持key和reverse,sort:原列表的修改
# print(sorted(s))
# print(sorted(s,reverse=True))
# #key会使所有元素先调用一遍指定函数,然后再进行排序
# t=["zeze6","apple","book","banana","pen"]
# print(sorted(t,key=len))
# # sort会在原函数上直接做修改,所以直接输出会是none,并且sort只能处理列表,sorted可以接受任何形式的可迭代对象作为参数
# print(t.sort(key=len))
# print(sorted("zeze6"))
# print(sorted((1,2,3,4,5)))

# # reversed:返回结果为迭代器,可以使用list转换
# s=[1,2,5,8,0]
# print(reversed(s))
# print(list(reversed(s)))
# #上面的结果类似于直接调用reverse
# s.reverse()
# print(s)

# #reversed也支持除了列表以外的可迭代对象,但是需要转换成列表,元组或者字符串
# print(list(reversed("zeze6")))
# print(list(reversed((1,2,5,9,3))))
# print(list(reversed(range(0,10))))

# # all()&any():判断可迭代对象中所有元素都为真或者是否存在某个元素的值为真
# x=[1,1,0]
# y=[1,1,9]
# print(all(x))
# print(all(y))
# print(any(x))

# # enumerate：枚举函数，用于将可迭代对象的元素“打包”为 (索引, 元素) 的形式
# seasons=["spring","summer","fall","winter"]
# print(enumerate(seasons))
# print(list(enumerate(seasons)))
# # 内置start函数,固定从几号开始
# print(list(enumerate(seasons,10)))

# # zip：将多个可迭代对象“打包”成元组，每个元组包含对应位置的元素
# x=[1,2,3]
# y=[4,5,6]
# print(list(zip(x,y)))
# z=[7,8,9]
# print(list(zip(x,y,z)))
# #如果位数不匹配,会以最短的为准
# z="zeze6"
# print(list(zip(x,y,z)))
# # 如果不想丢掉后面的e,6,可以使用itertools模块里的zip_longest()函数
# import itertools
# print(list(itertools.zip_longest(x,y,z)))

# # map：将指定函数依次作用到可迭代对象的每个元素上
# # 返回一个 map 对象（可迭代），不会立刻生成结果
# mapped=map(ord,"zeze6")
# print(list(mapped))
# a=map(pow,[1,2,3],[4,5,6])
# print(list(a))
# print(list(map(max,[1,2,3],[4,5,6],[7,8,9])))

# # filter：根据指定的判断函数，对可迭代对象进行筛选
# # 只有使函数返回 True 的元素才会被保留下来
# print(list(filter(str.islower,"zeze6")))

'''
一个迭代器肯定是一个可迭代对象
可迭代对象可以重复使用，迭代器是一次性的，例子如下：
'''
# mapped=map(ord,"zeze6")
# for i in mapped:
#     print(i)
# print(list(mapped))

# #iter使可迭代对象变成迭代器
# x=[1,2,3,4,5]
# y=iter(x)
# print(type(y))#输出结果：列表的迭代器
# print(list(y))#输出第一次
# print(list(y))#输出第二次，变成空集

# #next:逐个将迭代器里的元素提取出来,过多次打印则会报错
# a=[1,2,3,4,5,"上山打老虎"]
# b=(iter(a))
# #我在这里写一个循环，避免多次打印
# #如果想让代码超出限制之后不报错，可以在迭代器后面加提示
# i=0
# while True:
#     print(next(b,"没有了，被用光了"))
#     i+=1
#     if i==len(a)+1:
#         break

