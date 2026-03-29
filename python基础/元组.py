# #元组 不可变
# # 圆括号的必要性：与其省略圆括号，不如一直加上括号增加代码可读性
# rhyme=(1,2,3,4,5,"上山打老虎")
# print(rhyme)
# rhyme=1,2,3,4,5,"上山打老虎"
# print(rhyme)
# print(rhyme[-1])
#元组不可变，所以不支持 增 删 改 如下：rhyme[1]=10
#
# #元组的切片
# print(rhyme[:3])
# print(rhyme[3:])
# print(rhyme[:])
# print(rhyme[::2])
# print(rhyme[::-1])

# #元组的查 count index
# nums=(3,1,9,6,8,3,5,3)
# print(nums.count(3))
# heros="黑寡妇","绿巨人","黑寡妇"
# print(heros.count("黑寡妇"))
# s=(1,2,3)
# t=(4,5,6)
# print(s+t)
#元组的嵌套
# w=s,t
# print(w)
# #元组的迭代
# for each in s:
#     print(each,end=" ")
# #嵌套元组的迭代
# print()#此处为换行
# for i in w:
#     for j in i:
#         print(j,end=" ")
# #列表推导式
# print()
# s=(1,2,3,4,5)
# a=[each*2 for each in s]
# print(a)
# # 以下为迭代器，不是元组推导式，目前无结果
# b=(each*2 for each in s)
# print(b)

# # 生成只有一个元素的元组
# x=(520)
# print(type(x))
# #上面是数字int,下面才是元组tuple
# x=(520,)
# print(type(x))

# #打包（生成一个元组/列表）和解包(赋值)
# t=(123,"zeze",3.14)
# print(t)
# x,y,z=t
# print(x,y,z)
# t=[123,"zeze",3.14]
# print(t)
# x,y,z=t
# print(x,y,z)
# #！！！赋值左右两边数量要相等,如果不相等，可以在变量名前加‘*’
# a,b,c,d,e="hello"
# print(a,b,c,d,e)
# x,y,*z = (1,2,3,4,5)
# print(x,y,z)
# # z包含的一定是list列表，因为剩余个数不确定，而list可变灵活

# # python多重赋值实现逻辑：
# x,y=1,2
# print(x,y)
# _=(1,2)
# x,y=_
# print(x,y)

# # 元组本身不可变，但是元组内的元素如果可变，元组就可以被修改
# s=[1,2,3]
# t=[4,5,6]
# w=(s,t)
# print(w)
# w[0][0]=0
# print(w)
