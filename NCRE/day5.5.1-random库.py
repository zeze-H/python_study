from random import *

'''
# random(): 生成一个 0.0-1.0 的随机数
print(random())
'''

# seed：初始化随机数种子，默认值为当前系统时间
# 相同随机数种子会产生相同随机数
seed(10)
print(random())
print(random())

seed(10)
print(random())
print(random())
