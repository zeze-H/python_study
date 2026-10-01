# def make_greeting():
#     return "你好,FastApi"
# fn = make_greeting
# result = make_greeting()
# print("1. fn 是什么:", fn)
# print("2. result 是什么:", result)
# print("3. 执行 fn() 的结果是:", fn())

# def create_waiter(chef):
#     # *args 和 **kwargs 就是两个万能收纳袋，能装下客人传来的任何要求！
#     def dedicated_waiter(*args, **kwargs):
#         print("服务员：记下客人需求，传达给厨房...")
        
#         # 把收纳袋里的要求，原模原样递给厨师！
#         food = chef(*args, **kwargs)
        
#         print("服务员：上菜完毕！")
#         return food
        
#     return dedicated_waiter

# @create_waiter
# def make_steak(doneness, sauce="黑椒汁"):
#     return f"{doneness}熟、加{sauce}的牛排"

# # 客人下单：传了一个顺序值 "七分"，传了一个指定键值对 sauce="蘑菇汁"
# my_dinner = make_steak("七分", sauce="蘑菇汁")

# print("最终拿到:", my_dinner)



# from pydantic import BaseModel, ValidationError
# from typing import Optional

# class UserProfile(BaseModel):
#     username: str                     # 必填
#     age: int                          # 必填（但传 "20" 会自动转为 20）
#     is_vip: bool = False              # 选填（默认 False）
#     email: Optional[str] = None       # 选填（默认 None）

# # ---------- 案例 1：类型自动转换成功 ----------
# data1 = {"username": "张三", "age": "25", "is_vip": "true"}
# user1 = UserProfile(**data1)
# print("1. 转换后的 age 类型:", type(user1.age), user1.age)       # int: 25
# print("2. 转换后的 is_vip 类型:", type(user1.is_vip), user1.is_vip) # bool: True

# # ---------- 案例 2：缺少必填项报错 ----------
# try:
#     data2 = {"age": 20}  # 漏掉了必填的 username
#     user2 = UserProfile(**data2)
# except ValidationError as e:
#     print("3. 成功被拦截报错:", e.errors()[0]["msg"]) # Field required



# import asyncio
# import time

# # 模拟异步任务：用 await 交出控制权
# async def task_a():
#     print("任务 A 开始烧水...")
#     await asyncio.sleep(2)  # await 交出控制权 2 秒
#     print("任务 A 水烧开了！")

# async def task_b():
#     print("任务 B 正在接待其他客人...")

# async def main():
#     # 让 A 和 B 一起跑
#     await asyncio.gather(task_a(), task_b())

# # 启动事件循环
# asyncio.run(main())

# n=0
# def add1():
#     global n
#     n+=1
#     return n
# def make_counter():
#     count = 0
#     def add():
#         nonlocal count
#         count+=1
#         return count
#     return add
# a= make_counter()
# print(a())
# print(a())
# print(add1())
# print(add1())


