# 打印1-100的数字
for i in range(1, 101):
    print(i)

print("*" * 100)

# 打印1-100之间的偶数
for i in range(2, 101, 2):
    print(i)

print("*" * 100)

# 打印1-100之间的奇数
for i in range(1, 101, 2):
    print(i)

print("*" * 100)

# 判断奇偶数
for i in range(1, 101):
    if i % 2 != 0:
        print(i, "是奇数")
    else:
        print(i, "是偶数")

# 求1-100之间的和
total = 0
for i in range(1, 101):
    total += i
print(total)

# 打印1-100的前三个偶数
import sys

count = 0
for i in range(1, 101):
    if i % 2 == 0:
        print(i)
        count += 1
    if count >= 3:
        # break
        # print("程序正常结束")
        sys.exit()

# 输出不换行，结尾加 end
print("111", end="*")
print("222")

print("*" * 50)

print("111", end="\n")
print("222")
