'''字典'''
from platform import libc_ver

# x={"吕布","关羽"}
# print(type(x))#set是集合
# y={"吕布":"口口布","关羽":"关习习"}
# print(type(y))#dict才是字典
# #字典没有索引下标，提供键，获取值
# print(y["吕布"])
# #字典添加键值对，指定不存在的键来创建键值对
# y["刘备"]="刘baby"
# print(y)

# #创建字典：
# #直接创建
# a={"吕布":"口口布","关羽":"关习习","刘备":"刘baby"}
# #使用dict函数，要求键不能加引号
# b=dict(吕布="口口布",关羽="关习习",刘备="刘baby")
# #使用列表作为参数
# c=dict([("吕布","口口布"),("关羽","关习习"),("刘备","刘baby")])
# #将第一种方法作为参数传递给d
# d=dict({"吕布":"口口布","关羽":"关习习","刘备":"刘baby"})
# #混合方法
# e=dict({"吕布":"口口布","关羽":"关习习"},刘备="刘baby")
# #zip方法
# f=dict(zip(["吕布","关羽","刘备"],["口口布","关习习","刘baby"]))
# print(a==b==c==d==e==f)

# # 字典的增
# #.fromkeys()用于批量创建字典键，所有键初始指向同一个值
# d=dict.fromkeys("zeze6",250)
# print(d)
# #修改键的值
# d['e']=70
# #增加一个新键值对
# d["h"]=80
# print(d)
# '''字典一个键对应一个值，不会重复，如果重复就用新的值替换旧的值'''

# #字典的删
# d=dict.fromkeys("zeze6",250)
# #pop
# d.pop('e')
# print(d)
# print(d.pop('g','如果没找到这个键就会抛出异常，可以像这样指定'))
# #popitem():删除最后一个加入字典的键值对
# d.popitem()
# print(d)
# #del():删除一个指定的字典元素
# del d['z']
# print(d)
# try:
#     del d
#     print(d)
# except:
#     print("d被删除，直接消失")
# #清空字典：clear（）
# s=dict.fromkeys("zehuan","love")
# print(s)
# s.clear()
# print(s)

# #字典的改：
# d=dict.fromkeys("zehuan",1314)
# print(d)
# d['z']="love"
# print(d)
# #update:同时改多个值或者字典替换
# d.update({'z':105,'e':20})
# print(d)

# #字典的查：
# d=dict.fromkeys("zehuan",1314)
# #如果直接查找找不到会报错，可以使用get方法
# print(d.get('E',"这里没有E"))
# #setdefault:查找键值对，如果不在，则会直接添加进去
# print(d.setdefault('h',417))
# #因为没有找到H，则会添加一个新的键值对进去
# print(d.setdefault('H',417))
# print(d)

# #分别用于获取键值对，键，值，的视图对象:当字典内容发生带改变，视图对象也会改变
# d=dict.fromkeys("zehua",1314)
# keys=d.keys()
# values=d.values()
# items=d.items()
# print(keys)
# print(values)
# print(items)
# d.pop('z')
# print(keys)
# print(values)
# print(items)
# #浅copy方法
# e=d.copy()
# print(e)

#字典的其他函数
#len获取字典中键值对的数量
d=dict.fromkeys("zehua",1314)
print(len(d))
#in&not in:
print('e'in d)
print('a'in d)
print('a'not in d)
#list字典转换列表
print(list(d))
print(list(d.values()))
print(list(d.items()))
#iter:将字典的键变成一个迭代器
e=iter(d)
for i in range(len(d)):
    print(next(e))
#python3.8之后可以使用reverse函数颠倒字典顺序,字典本身是无序的
print(list(reversed(d.items())))

# #字典的嵌套
# d={"吕布":{"语文":60,"数学":70,"英语":80},"关羽":{"语文":80,"数学":90,"英语":70}}
# print(d)
# #输入两次键来索引
# print(d['吕布']['数学'])
# #字典嵌套列表
# d={"吕布":[60,70,80],"关羽":[80,90,70]}
# print(d['吕布'][1])'


# #字典推导式
# d={'F':70,'i':105,'s':115,'h':104,'C':67}
# # 1. 键值互换：value 作为新 key，key 作为新 value
# b={v:k for k,v in d.items()}
# print(b)
# # 2. 带条件的字典推导式：只保留 value > 100 的项，并进行键值反转
# c={v:k for k,v in d.items() if v>100}
# print(c)
# # 3. 使用函数生成 value：字符作为 key，ord() 生成对应编码
# d={x:ord(x) for x in 'FishC'}
# print(d)
# # 4. 双 for 推导式：同一个 key 会被多次赋值，最终保留最后一次
# d={x:y for x in [1,3,5] for y in [2,4,6]}
# print(d)