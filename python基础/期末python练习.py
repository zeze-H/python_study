'''第一章编程题'''
# print("这是我写的第一个python程序！")
# print("*"*30)
# print("这是我的第二个python程序")
# print("*"*30)
# '''第二章编程题'''
# user_name=input("请输入您的姓名：")
# user_age=input("请输入您的年龄:")
# user_address=input("请输入您的地址:")
# print(f"姓名：{user_name}\n年龄：{user_age}\n地址：{user_address}")
#
# print("苹果：8")
# print("橘子：9")
# print("香蕉：10")
# c=float(input("请输入你需要的商品单价："))
# d=int(input("请输入你需要的商品数量:"))
# print(f"商品的总价为:{c*d:.2f}")
# '''第三章编程题'''

# user_id="zeze"
# user_password="123123"
# while True:
#     a=input("请输入账号：")
#     b=input("请输入密码:")
#     if a==user_id and b==user_password:
#         print("Hello Python")
#         break
#     else:
#         print("账号密码输入有误")

# for i in range(1,10):
#     for j in range(1,i+1):
#         print(i,"*",j,"=",i*j,end=' ')
#     print()

# i=1
# while i<10:
#     j=1
#     while j<=i:
#         print(i,"*",j,"=",i*j,end="")
#         j=j+1
#     print("")
#     i=i+1

# i=1
# sum=0
# for i in range(1,101):
#     sum+=i
#     i+=1
# print(sum)
# while i<101:
#     sum+=i
#     i+=1
# print(sum)

# for i in range(2,11):
#     for j in range(2,i):
#         if i%j==0:
#             print(i,"%",j,"=",i//j)
#             break
#     else:
#         print(i,"是一个素数")

# i=2
# while i<10:
#     j=2
#     while j<i:
#         if i%j==0:
#             print(i,end=" ")
#             break
#         else:
#             print(i,end=" ")
#             i=i+1


# for x in range(2,101):
#     for y in range(2,x):
#         if x%y==0:
#             print(x,"不是素数")
#             break
#     else:
#         print(x,"是素数")

# x=2
# while x<101:
#     y=2
#     while y<x:
#         if x%y==0:
#             print(x,"不素数")
#             y=y+1
#             break
# #         else:
# scores=[88,92,75,63,99,85]
# total=0
# for i in scores:
#     total+=i
#
# 学生成绩字典


# for i in range(1,10):
#     for x in range(1,i+1):
#         print(x,'*',i,"=",x*i,end="  ")
#     print("")

# i=2
# while i<101:
#     x=2
#     while x<i:
#         if i%x==0:
#             print(i,"不是素数")
#             break
#         x=x+1
#     else:
#         print(i,"是一个素数")
#     i=i+1
# for i in range(2,10):
#     for j in range(2,i):
#         if i%j==0:
#             print(i,"不是")
#             break
#     else:
#         print(i,"是")
# i=1
# while i<10:
#     n=1
#     while n<=i:
#         print(i,"*",n,"=",i*n,end=" ")
#         n+=1
#     print("")
#     i=i+1
# n =6
# for i in range(1, n + 1):
#     print((n-i)*" ",(2*i-1)*"*")
# a='ABCD'
# print(a[2])
# print(a[:])
# print(a[::])

# a=dict.fromkeys(['ze','huan','fu','da'])
# pirnt()