# '''集合set'''
# print(type({}))
# print(type({'one'}))
# print(type({'one':1}))

# #创建集合
# #直接创建
# {"one","two","three"}
# #集合推导式:集合是无序的
# print({s for s in "zehuan"})
# #类型构造器：set
# print(set('zehuan'))

# #集合无序，不能用下标索引，但是可以用in not in检测是否存在
# s=set("zehuan")
# print('z'in s)
# print('z' not in s)
# #访问集合元素：
# for i in s:
#     print(i)

# #集合的唯一性
# #集合的去重:将列表中的重复元素去除
# a=set([1,1,2,3,5])
# print(a)
# #判断元素唯一性
# s=[1,1,2,3,5]
# print(len(s)==len(set(s)))

# #集合的方法合集
#
# #浅copy
# a=set([1,1,2,3,5])
# b=a.copy()
# print(b)

# #isdisjiont:检测两个集合是否相关
# s=set("zehuan")
# print(s.isdisjoint(set("python")))#有相同点h,所以相关
# print(s.isdisjoint(set('bb')))
# #也可以不用set变成集合类型，直接传入可迭代对象也可以
# print(s.isdisjoint('bb'))
#
# #issubset检测该集合是否是另一个集合的子集
# print(s.issubset('zezehuanhuan'))
# #issuperset检测该集合是否是另一个集合的超集
# print(s.issuperset('ze'))

# #计算当前集合与其他集合的：
# s=set("zehuan")
# '''并集'''
# print(s.union({1,2,3}))
# '''交集'''
# print(s.intersection({'z','e'}))
# '''差集'''
# print(s.difference({'z','e'},{'h','u','a','n'}))
# '''以上三个均支持多参数'''
# '''求对称差集，只支持一个参数'''
# # symmetric_difference：返回两个集合中只存在于其中一个集合的元素
# print(s.symmetric_difference({'z','e'}))
'''注意：由于集合会自动去重，所以括号里写重复的字母会先被去重然后再使用
所以可能会出现结果与想象不符'''
# #已上方法相应的运算符
# s=set("zehuan")
# #检测子集
# print(s<=set('zezehuanhuan'))
# #检测真子集:
#
# print(s<set('zehuan6'))
# print(s<set('zehuanze'))
# #检测超集
# print(s>=set('zehuan'))
# #检测真超集
# print(s>set('ze'))
# #检测并集：所有元素合并，去重
# print(s|{1,2,3}|set("python"))
# #检测交集：同时出现在所有集合中的元素
# print(s&set({'z'})&set("zeze"))
# #检测差集:s里减去后面的
# print(s-set({'z'})-set('huan'))
# #检测对称差集：同时属于两边的全部扔掉
# print(s^set({'z','e','6','6'}))

'''使用运算符，符号两边必须是集合类型的数据，否则会报错，但是方法可以使用任何可迭代对象'''
# print(s<='zeze')#set不能直接用运算符比较字符串
