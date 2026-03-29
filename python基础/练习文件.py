# ##班级成绩统计
# list1=[]
# win=0
# notwin=0
# x=int(input("请输入考试学生总人数（正整数）："))
# while len(list1)<x:
#     y=eval(input("请输入考试成绩："))
#     if y>100 or y<0:
#         print("请输入0-100以内的成绩！")
#         continue
#     if y>=60:
#         win+=1
#     else:
#         notwin+=1
#     list1.append(y)
# sum=0
# for i in list1:
#     sum+=i
# list1.sort(reverse=True)
# print("本班及格人数为",win,"本班不及格人数为：",notwin)
# print(f"本班总成绩为：{sum},本班平均成绩为：{sum/len(list1):.2f}")
# print("本班成绩最高分为:",list1[0],"本班最低成绩为：",list1[-1])



##简易超市购物车小程序
products=[("苹果",3),("橘子",4),("香蕉",5),("梨子",2)]
for i in range(len(products)):
    print(i,products[i][0],"价格：",products[i][1])
cart=[]
while True:
    choice=int(input("请输入你想购买的商品序号购买（输入-1结账退出）"))
    if choice == -1:
        break
    elif choice<0 or choice>=len(products) :
        print("你所输入的商品序号不存在！请重新输入！")
        continue
    else:
        cart.append(products[choice])
print("————————————————————------结账清单------————————————————————")
total_price=0
for i in range(len(cart)):
    total_price+=cart[i][1]
print("您的购物车现在有",cart,"共消费",total_price,"元。")

