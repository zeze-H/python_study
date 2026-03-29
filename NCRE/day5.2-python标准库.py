import random

print(random.random())

from random import *  # 调用 random 内的所有函数，不需要再使用 random. 前缀
print(randint(1, 10))  # 产生整数随机数
