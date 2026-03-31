# # 字符串：不可变
# #判断回文数
# while True:
#     x=input("请输入一串数字，例如：12321：")
#     print("是回文数" if x==x[::-1] else "不是回文数")
# from multiprocessing.spawn import import_main_path

# #大小写字母换来换去的方法：
# #capitalize:将首字母变为大写，其余不变
# x="I Love ZEZE"
# print(x.capitalize())
# #casefold:所有字母均改为小写,相较于lower，可以处理更多语言的字符类如德语
# print(x.casefold())
# #title:所有首字母变为大写，其余为小写
# print(x.title())
# #swapcase:所有字母大小写反转
# print(x.swapcase())
# #upper:所有字母变为大写 lower:所有字母变为小写，只能处理英文字母
# print(x.upper())
# print(x.lower())

# #左中右对齐方法：(要求内置width参数，用来指定字符串宽度，如果小于或者等于原字符串，直接输出)
# x="有内鬼，停止交易！"
# #center:字符串居中
# print(x.center(100))
# #ljust,rjust:左右对齐
# print(x.ljust(100))
# print(x.rjust(100))
# #zfill:用0来填充左侧：
# print(x.zfill(100))
# y=("-520")
# print(y.zfill(3))
# #左中右对齐还支持fillchar参数，就是将空格填充改为指定字符填充，如下：
# print(x.center(15,"草"))
# print(x.ljust(10,"草"))
# print(x.rjust(10,"草"))

# ##字符串查找功能
# #.count()支持指定范围查找元素个数
# x="上海自来水来自海上"
# print(x.count("海"))
# print(x.count("海",0,5))
# #.find .rfind :查找元素第一次出现的索引下标值，从左往右找和从右往左找，依旧支持指定范围查找
# print(x.find("海"))
# print(x.rfind("海"))
# #.index() rindex():和find功能一样， 不同点为：如果找不到元素，index会抛出异常，find会报-1
# print(x.find("龟"))
# print(x.index("龟"))

# #字符串替换方法
# #.expandtabs()使用空格替换制表符tab，并返回新字符串
# code="""
#     print("i love zeze")\tprint("i love my wife")"""
# print(code)#这里用的是\t代表tab键 因为pycharm不支持tab键输入会自动替换成空格
# new_code=code.expandtabs(4)
# print(new_code)
# #.repalce(old,new,count=-1)将旧字符串转换成新字符串，count为次数
# a="在吗！我在你家楼下，快点下来！"
# print(a.replace("在吗","想你"))
# #translate，返回一个根据table参数转换后的新字符串
# table=str.maketrans("ABCDEFG","1234567")
# print("I love ZEZE".translate(table))
# #str.maketrans支持忽略指定字符串，例如：
# table2=str.maketrans("ABCDEFG","1234567","love")
# print("I love HUANHUAN".translate(table2))


# #字符串的判断（返回值都为bool类型）
# #.startswith().endswith()判断参数的子字符串是否出现在字符串的起始位置或者结束位置,内置start以及end参数，这两个内置函数也支持元组形式，下面有示例
# x="我爱python"
# print(x.startswith("我"))
# print(x.startswith("我",0,2))
# print(x.startswith("爱",1))
# print(x.startswith("python"))
# #
# print(x.endswith("python"))
# #如果倒着取，一定是false，因为没有设置步长，也不能设置步长，-8，-3一定是空集，所以是false
# print(x.endswith("on",-8,-3))
# print(x.endswith("py",0,4))
# #支持元组
# x="她爱python"
# if x.startswith(("你","我","她")):
#     print("总有人喜欢python")

# x="I love Python"
# #.istitle()验证所有单词均以大写字母开头，其余均为小写
# print(x.istitle())
# #.isupper().islower()验证所有单词均为大写或小写
# print(x.isupper())
# # 从左到右调用，先大写再验证
# print(x.upper().isupper())
# print(x.lower().islower())
#
# #.isalpha()验证所有字符均为字母构成
# print(x.isalpha())#空格不是字母
# #.isspace()验证是否为空字符串
# print(x.isspace())
# #.isprintable()验证是否所有字符均可打印
# print("\n".isprintable())

# #检测数字，各有类别：isdecimal,isdigit,isnumeric
# # #集大成者.isalnum():只要以上三个以及isalpha()其中之一任意返回true，结果就是true
# x="12345"
# y="2²"
# z="ⅠⅡⅢⅣⅤ"
# v="一二三四五"
# print("纯数字：")
# print(x.isdecimal())
# print(x.isdigit())
# print(x.isnumeric())
# print("二的平方：")
# print(y.isdecimal())
# print(y.isdigit())
# print(y.isnumeric())
# print("罗马数字：")
# print(z.isdecimal())
# print(z.isdigit())
# print(z.isnumeric())
# print("中文数字：")
# print(v.isdecimal())
# print(v.isdigit())
# print(v.isnumeric())


# #.isidentifier():判断字符串是否是一个合法的python标志符
# print("I am a good girl".isidentifier())
# print("I_am_a_good_girl".isidentifier())
# print("zeze520".isidentifier())
# print("520zeze".isidentifier())

# #tip:判断一个字符串是否为python的保留标志符：
# import keyword
# print(keyword.iskeyword("if"))
# print(keyword.iskeyword("py"))

# #字符串的截取
# #.lstrip().rstrlp():去除左侧或者右侧的留白,.strip():左右都不留白
# print("   左侧不要留白".lstrip())
# print("右侧不要留白   ".rstrip())
# print("   不要留白   ".strip())
# # 内置函数，去除所有包含在内的单个字符，直到遇到一个不在括号内中的字符为止：
# a="www.zeze.com"
# print(a.lstrip("wcom."))
# print(a.rstrip("wcom."))
# print(a.strip("wcom."))

# #removeprefix(),removesuffix():去除指定的整个字符串，而不是单个字符
# a="www.zeze.com"
# print(a.removeprefix("www."))
# print(a.removesuffix(".com"))

# #拆分&拼接

# #partition(),rpartition(),括号内指定分隔符，在字符串中找到分隔符之后将分隔符左右拆分成三部分的元组
# a="www.ilovezeze.com"
# print(a.partition("."))
# b="www.ilovezeze.com/python"
# print(b.rpartition("/"))

# #.split(),默认情况切分空格，再打包成列表返回，
# c=("苟日新，日日新，又日新")
# print(c.split())
# #指定逗号
# print(c.split("，"))
# print(c.rsplit("，"))
# #指定分割次数
# print(c.split("，",1))
# print(c.rsplit("，",1))\
# #因为各个操作系统换行符不同，所以用splitlines():将字符串按行分割，然后以列表格式返回,内置函数选择是否包含换行符，如果是true则包含，false则不包含
# d=("苟日新\n日日新\n又日新")
# print(d.splitlines())
# print(d.splitlines(True))

# #.join():用一个分隔符，把多个字符串拼接成一个字符串。
# print(".".join(["www","ilovezeze","com"]))
# print(".".join(("zeze","love","huanhuan")))
# #.join字符串拼接
# s="zeze"
# s+=s
# print(s)
# print("".join(("zeze","zeze")))

#字符串的格式化：.format
#
# # .format():
# print("1+2={},2的平方是{},3的立方是{}".format(1+2,2**2,3**3))
# # 花括号内内置函数：可以自定义位置索引值，同一个索引值也可以被引用多次
# print("{1}看到{0}就很激动".format("zeze","haunhuan"))
# print("{0}{0}{1}{1}".format("是","非"))
# #关键字索引
# print("我叫{name},我爱{fav}".format(name="zeze",fav="python"))
# #位置索引和关键字索引，可以一起使用
# print("我叫{name},我爱{0}，喜欢{0}的人运气都不会太差".format("python",name="zeze"))
# #直接输入花括号
# print("{}{}{}".format(1,"{}",2))
# print("{}{{}}{{}}".format(1))


# #内置函数align:指定对齐方式
# # ^ 表示居中对齐，宽度为 10
# print("{0:^10}".format(250))
# # > 右对齐，< 左对齐，使用位置参数
# print("{1:>10},{0:<10}".format("hello","world"))
# # 使用关键字参数进行左 / 右对齐
# print("{left:>10},{right:<10}".format(left="hello",right="world"))
# # 数字宽度为 10，使用 0 填充，默认右对齐
# print("{:010}".format(520))
# print("{:010}".format(-520))
# # 字符串默认左对齐，0 被当作普通填充字符，填在右侧
# print("{:010}".format("zeze"))
# # 指定填充字符 + 对齐方式
# # H 右对齐填充，% 左对齐填充
# print("{1:H>10}{0:%<10}".format(520,250))

# #字符串的格式化，符号选项：仅对数字类型有效
# # +：正数显示 +，负数显示 -
# # -：仅负数显示 -，正数不显示符号（默认）
# print("{:+}{:-}".format(520,-250))
# #做千分位的分隔符,位数不够就不显示
# print("{:,}".format(123))
# print("{:_}".format(1234))
# # 保留 2 位小数（定点浮点格式 f）
# print("{:.2f}".format(3.1415))
# # 保留 2 位有效数字（通用格式 g）
# print("{:.2g}".format(3.1415))
# # 字符串最多保留 6 个字符（超出部分截断）
# print("{:.6}".format("I love zeze"))
#  # ❌ 报错：对整数不能单独使用精度（precision）
# # print("{:.2}".format(520))

# # 整数类型格式化
# print("{:b}".format(80))
# # b：二进制表示
# print("{:c}".format(80))
# # c：将整数转换为对应的 Unicode 字符
# print("{:d}".format(80))
# # d：十进制整数表示
# print("{:o}".format(80))
# # o：八进制表示
# print("{:x}".format(80))
# # x：十六进制表示（小写字母）
# print("{:#b}".format(80))
# # #：为进制数添加前缀
# # 二进制前缀
# print("{:#o}".format(80))
# # #：为进制数添加前缀
# # 八进制前缀
# print("{:#x}".format(80))
# # #：为进制数添加前缀
# # 十六进制前缀0x


# # 浮点数格式化（科学计数法 / 定点 / 通用 / 百分比）
# # e / E：将浮点数转换为科学计数法
# # e 使用小写 e，E 使用大写 E，默认保留 6 位小数
# print("{:e}".format(3.1415))
# print("{:E}".format(3.1415))
# #规定小数点后位数，默认6位
# print("{:f}".format(3.1415))
# # g：通用格式（在定点和科学计数法之间自动选择）
# # 根据数值大小与精度，自动去掉多余的 0
# print("{:g}".format(12345678))
# print("{:g}".format(1234.1234))
# # %：百分比格式，先乘以 100，再加 %
# # 默认保留 6 位小数
# print("{:%}".format(0.98))
# # 指定百分比小数位数
# print("{:.2%}".format(0.98))
#
# # 关键字参数设置选项值
# print("{:.{prec}f}".format(3.1415,prec=2))
# # 使用多个关键字参数动态控制填充、对齐、宽度、精度和类型
# print("{:{fill}{align}{width}.{prec}{ty}}".format(3.1415,fill="+",align="^",width=10,prec=3,ty="g"))

# 字符串的格式化：f-string
# year=2006
# print(f"zeze出生于{year}年")
# print(f"1+2={1+2},2的平方是{2**2},3的立方是{3*3*3}")
# print(f"{-520:010}")
# print(f"{123456789:,}")
# print(f"{3.1415:.2f}")
# fill="+"
# align="^"
# width=10
# prec=3
# ty="g"
# print(f"{3.1415:{fill}{align}{width}.{prec}{ty}}")
