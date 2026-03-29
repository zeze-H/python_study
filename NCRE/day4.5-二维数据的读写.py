students = [
    ['学号', '姓名', '性别', '年龄'],
    ['1101', '张三', '男', '24'],
    ['1102', '李四', '男', '18'],
    ['1103', '王五', '男', '23'],
    ['1104', '赵六', '女', '21']
]

f = open("students.csv", "w", encoding="UTF-8")
for row in students:
    print(row)
    f.write(",".join(row) + "\n")
f.close()

f = open("students.csv", "r", encoding="UTF-8")
ls = []

for line in f:
    print(line)
    line = line.strip("\n")  # 去除换行符
    temp = line.split(",")  # 返回一个列表
    ls.append(temp)

print(ls)
f.close()
