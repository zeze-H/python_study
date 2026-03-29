# for遍历循环
s = "你好我叫泽泽"
for i in s:
    print(i)

nums = [1, 3, 3, 4, 5]
for i in nums:
    print(i)

x = (1, 2, 3, "openclaw")
for i in x:
    print(i)

# range循环：
# 生成0-9的整数序列
for i in range(10):
    print(i)

print("-" * 10)

# 生成5-9的整数序列
for i in range(5, 10):
    print(i)

print("*" * 10)

# 生成0-9的偶数
for i in range(0, 10, 2):
    print(i)
