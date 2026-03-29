path = "D:\\python work\\NCRE\\a\\text.txt"

f = open(path, "rt", encoding="UTF-8")
s = f.read(4)
print(s)
f.close()

# 二进制读取，然后转换成字节流，随后以十六进制输入
f = open(path, "rb")
s = f.read(4)
print(s)
f.close()

f = open(path, "r", encoding="UTF-8")

# readline(): 读取一行内容，指针结束后指向第二行开头
s = f.readline()
print(s)

s = f.readline()
print(s)
f.close()

f = open(path, "r", encoding="UTF-8")

# 使用 readlines() 方法读取文件所有行，每行作为列表中的一个元素
# 注意：读取后文件指针会移动到文件末尾
s = f.readlines()
print(s)

# 文件指针已经位于文件末尾，因此返回空列表
s = f.readlines(1)
print(s)

# 重置指针位置：0为文件开头，1为当前位置，2为文件结尾
f.seek(0)
s = f.readlines(1)
print(s)
f.close()

# 文件的写
path = "D:\\python work\\NCRE\\a\\text2.txt"
f = open(path, "w")

f.write("晴空无雨也生春,\n")
f.write("一树繁花照路人。\n")
f.write("风软不沾半点湿，\n")
f.write("只留香色满衣襟。\n")
f.close()

path = "D:\\python work\\NCRE\\a\\text3.txt"
f = open(path, "w")

# writelines() 不会自动添加换行符
ls = ["晴空无雨也生春，\n", "一树繁花照路人，\n", "风软不沾半点湿，\n", "只留香色满衣襟。\n"]
f.writelines(ls)
f.close()

# 追加写
path = "D:\\python work\\NCRE\\a\\text3.txt"
f = open(path, "a")
ls = ["今天非常的开心"]
f.writelines(ls)
f.close()

# 逐行读取（方式1）
fname = input("请输入要打开的文件:")
fi = open(fname, "r")
for line in fi.readlines():
    print(line)
fi.close()

# 逐行读取（方式2）
fname = input("请输入要打开的文件2:")
fi = open(fname, "r")
for line in fi:
    print(line)
fi.close()
