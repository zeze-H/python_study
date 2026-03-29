from random import *

# randint() 生成一个 a, b 之间的整数
print(randint(1, 10))

# getrandbits(k) 生成一个 k 比特长度的随机整数（以十进制形式输出）
print(getrandbits(10))

# randrange(start, end, step)：生成一个指定范围和步长的整数
print(randrange(1, 100, 2))

# uniform(a, b)：生成一个 a, b 之间的随机小数
print(uniform(1, 10))

# choice() 从序列类型（列表）中随机返回一个元素
ls = [1, 2, 3, 4, 5, 6]
print(choice(ls))

# shuffle() 将序列类型中元素随机打乱（原地修改）
shuffle(ls)
print(ls)

# sample(pop, k)：从 pop 中随机选取 k 个元素，以列表类型返回
print(sample(ls, 4))
