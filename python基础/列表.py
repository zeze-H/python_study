##列表的增删改

# # 强调一点:
# # 如果原地修改值，返回值是none例如.append.extend.sort.reverse.clear
# # 如果不改原对象，则可以返回新值，例如sorted（）,len（）,sum（a）   .count.index.upper
# # 如果会将原对象改掉，则返回none，如果不会，则有返回值
# # a.append(b)

# #列表的增：append为在列表末尾追加，extend为迭代，可迭代多个
# a=[1,2,3,4,5,"上山打老虎"]
# b=[6,7]
# print(a)
# a.extend(b)
# print(a)
# a.append(a)
##insert代表在列表指定位置添加，案例如下：分别是在列表中，首，末，添加元素
# s=[1,3,4,5]
# s.insert(1,2)
# print(s)
# s.insert(0,0)
# print(s)
# s.insert(len(s),6)
# print(s)

# # 列表的切片
# # 如下，相当于s.append(6)
# s=[1,2,3,4,5]
# s[len(s):]=[6]
# print(s)
# #如下，相当于s.extend(7,8,9)
# s[len(s):]=[7,8,9]
# print(s)

# #列表的删：remove,pop,clear
# #1.在remove中，如果选择被删除的元素有多个，那只会删除第一个
# #2.在remove中，如果并未找到需要被删除的元素，则会报错
# x=[1,2,3,4,5,"上山打老虎"]
# x.remove(2)
# print(x)
# #pop删除:指定元素下标删除
# x=[1,2,3,4,5,"上山打老虎"]
# x.pop(5)
# print(x)
# #clear:清空列表
# x.clear()
# print(x)

# #列表的改：
# heros=["孙悟空","猪八戒","沙悟净","唐僧","浪浪山小妖怪"]
# heros[0]=("zeze")
# print(heros)
# #切片实现多个元素的替换:将列表下标为3，以及之后的元素全部替换
# heros[3:]=["武松","林冲","李逵"]
# print(heros)

# #列表的排序：sort,reverse,[::-1]
# nums=[3,4,1,5,7,8,9,1,3,5,5,6,3]
# nums.sort()
# print(nums)
# #倒序：
# nums.reverse()
# print(nums)
# #sort内置参数reverse
# numms=[3,4,1,5,7,6,5,4,0,9,7]
# numms.sort(reverse=True)
# print(numms)

# #列表的查:count,index
# numms=[3,4,1,5,7,6,5,4,0,9,7]
# print(numms.count(7))
# #index获取索引下标:如果有多个相同元素，也只会返回第一个找到的元素下标
# heros=["孙悟空","猪八戒","沙悟净","唐僧","浪浪山小妖怪"]
# print(heros.index("唐僧"))
# #获取索引下标之后做修改，同样的也只会修改找到的第一个元素
# heros[heros.index("唐僧")]="huanhuan"
# print(heros)
# #index有可选参数，指定start,end,规则是左闭右开[7,11),所以end取不到11，最多到10
# print(numms.index(7))
# print(numms.index(7,7,11))

# # 列表的嵌套
# matrix=[[1,2,3],[4,5,6],[7,8,9]]
# matrix=[
#     [1,2,3],
#     [4,5,6],
#     [7,8,9]]
#
# for i in matrix:
#     for each in i:
#         print(each,end=" ")
#     print()
# print(matrix[0])
# print(matrix[0][2])


# # 二维列表
# A=[0]*3
# for i in range(3):
#     A[i]=[0]*3
# print(A)
# B=[[0]*3]*3
# print(B)
# #二维列表三个元素互不相同
# #二维列表三个元素相同
# A[1][1]=1
# print(A)
# #
# B[1][1]=1
# print(B)

# # 变动x的同时 y就跟着改了
# x=[1,2,3]
# y=x
# print(y)
# x[1]=1
# print(y)

# # 列表的浅copy
# # 直接copy
# a=[1,2,3]
# b=a.copy()
# a[1]=1
# print(a)
# print(b)
# # 切片copy
# c=[1,2,3]
# #注意这里依旧遵循：左闭右开的规则，所以1:1取不到
# d=c[1:1]
# e=c[1:2]
# f=c[:]
# print(d)
# print(e)
# print(f)


# # 列表的深copy
# # 如果是嵌套列表会导致浅copy失效,y会依旧与x共用一个列表
# x=[[1,2,3],[4,5,6],[7,8,9]]
# y=x.copy()
# x[1][1]=0
# print(x)
# print(y)


# # 所以要引入copy模块
# import copy
# x=[[1,2,3],[4,5,6],[7,8,9]]
# y=copy.copy(x)
# x[1][1]=0
# print(x)
# print(y)
# a=[[1,2,3],[4,5,6],[7,8,9]]
# b=copy.deepcopy(a)
# a[1][1]=0
# print(a)
# print(b)


# #!!循环和列表推导式，一个是在原列表直接替换数据，一个是创建新列表
# oho=[1,2,3,4,5]
# for i in range(len(oho)):
#     oho[i]=oho[i]*2
# print(oho)
# x=[]
# for i in range(10):
#     x.append(i+1)
# print(x)

# #将上面两个式子转化为列表推导式，如下：
# oho=[1,2,3,4,5]
# oho=[i*2 for i in oho]
# print(oho)

# x=[i for i in range(10)]
# print(x)
# x=[i+1 for i in range(10)]
# print(x)
# y=[c*2 for c in"zeHUAN"]
# print(y)
# #将字符串转化为编码
# code=[ord(c) for c in "zeHUAN"]
# print(code)

# #二维列表取下标
# matrix=[[1,2,3],
#         [4,5,6],
#         [7,8,9]]
# col2=[row[1] for row in matrix]
# print(col2)
# #取正对角线
# diag=[matrix[i][i] for i in range(len(matrix))]
# print(diag)
# #取反对角线
# n=len(matrix)
# diag2=[matrix[i][n-1-i] for i in range(n)]
# print(diag2)

# ##续论列表推导式

# ##真假二维列表
# ##假
# B=[[0]*3]*3
# print(B)
# B[1][1]=2
# print(B)
# ##真
# A=[0]*3
# for i in range(3):
#     A[i]=[0]*3
# print(A)
# A[1][1]=2
# print(A)
# #利用列表推导式创建真二维列表
# S=[[0]*3 for i in range(3)]
# print(S)

# #列表推导式添加if语句筛选
# even=[i for i in range(10) if i%2==0]
# print(even)
# #列表推导式优先执行for语句 后执行if
# even=[i+1 for i in range(10) if i%2==0]
# print(even)
# words=["Great","FishC","Zeze","Excellent","Fantistic"]
# fwords=[i for i in words if i[0]=="F"]
# print(fwords)
#
# #列表推导式的嵌套
# matrix=[[1,2,3],
#         [4,5,6],
#         [7,8,9]]
#
# flatten=[col for row in matrix for col in row]
# print(flatten)
# #上面的列表推导式等价于下面的循环
# flatten=[]
# for row in matrix:
#     for col in row:
#         flatten.append(col)
# print(flatten)

# # 笛卡尔乘积
# d=[x+y for x in "12" for y in "34"]
# print(d)
# d=[]
# for x in "12":
#     for y in "34":
#         d.append(x+y)
#         print(d)

# #列表推导式终极语法
# d=[[x,y] for x in range(10) if x %2==0 for y in range(10) if y%3==0]
# print(d)
# _=[]
# for x in range(10):
#     if x%2==0:
#         for y in range(10):
#             if y%3==0:
#                 _.append([x,y])
# print(_)

#！！！kiss原则keep it simple & stupid:保证代码简洁，清晰