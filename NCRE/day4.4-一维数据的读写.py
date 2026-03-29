ls = ["北京", "上海", "深圳", "广州"]

# 读列表 ls，然后创建一个 city.csv 文件
f = open("city.csv", "w", encoding="UTF-8")
print("初始数据：", ls)

s = ",".join(ls)
print("join 添加后的数据：", s)

# 将 ls 写入创建的文件
f.write(s)
f.close()

# 将文件读取
f = open("city.csv", "r", encoding="UTF-8")
info = f.read()
print(info)

ls = info.split(",")
print(ls)

f.close()
