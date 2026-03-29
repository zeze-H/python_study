# # # 99乘法表
# for i in range(1,10):
#     for j in range(1,i+1):
#         print(j,"*",i,"=",j*i,end="\t")
#     print()

# i=1
# while i<10:
#     j=1
#     while j<=i:
#         print(i,"*",j,"=",i*j,end="  ")
#         j=j+1
#     print( )
#     i=i+1

#一百万以内的数字相加
# sum=0
# for i in range(0,1000001):
#     sum+=i
# print(sum)

# sum=0
# i=1
# while i<1000001:
#     sum=sum+i
#     i=i+1
# print(sum)

# # 素数:大于一的数中,除了1和它本身无法被其他自然数整除
# for n in range(2,100):
#     for x in range(2,n):
#         if n%x==0:
#             print(n,"=",x,"*",n//x)
#             break
#     else:
#         print(n,"是一个素数")

# i = 2
# while i < 10:
#     j = 2
#     while j < i:
#         if i % j == 0:
#             print(i, "=", j, "*", i // j)
#             break  # 找到因数就跳出内层循环
#         j += 1  # 没找到因数才增加 j
#     else:
#         print(i, "是一个素数")
#     i += 1  # 外层循环每次都增加 i





