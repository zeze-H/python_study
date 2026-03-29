# 相对路径
# path = "a/text.txt"

# 绝对路径
path = "D:/python work/NCRE/a/text.txt"

f = open(path, "r", encoding="UTF-8")
s = f.read()
f.close()

print(s)

'''
\n  换行
\t  tab
\\  \
'''

# path = "D:\\python work\\NCRE\\a\\text.txt"
# 注意：无论是写绝对路径还是相对路径，反斜杠要么写成 /，要么使用 \\ 进行转义

print("Hello\nworld")
