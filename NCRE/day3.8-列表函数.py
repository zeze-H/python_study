# 列表：有序可变
ls = [12, 12, 3.14, "hello", "移动"]
print(ls)
print(len(ls))
print(type(ls))

# 索引取值
print(ls[0])
print(ls[-1])
print(ls[::-1])
print(ls[0:4:2])

# 二维列表
ls2 = [123, 3.14, [55, 66], 11]
print(ls2[2])
print(ls2[2][1])

# 列表函数
nums = [12, 12, 3.14, 45, 50]
print(len(nums))
print(12 in nums)
print(12 not in nums)

# 列表元素比大小，如果一个数字一个字符串则会报错
print(max(nums))
print(min(nums))

ls3 = ["a", "b", "c", "d", "e"]
print(min(ls3))
print(max(ls3))

ls4 = ["aa", "ab", "ac", "ad", "ae"]
print(min(ls4))
print(max(ls4))
