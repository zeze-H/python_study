# async_demo2.py —— 协程对象到底是个啥
import asyncio

async def boil_water():
    print("  开始烧水...")
    await asyncio.sleep(1)
    print("  水开了!")
    return "水开了"

async def main():
    print("第 1 步：调用 boil_water()，但【不 await】")
    task = boil_water()
    print("  返回的东西是:", task)
    print("  注意：上面没有打印'开始烧水'——函数体一行都没执行!\n")

    print("第 2 步：现在【await】它")
    result = await task
    print("  拿到结果:", result)

asyncio.run(main())
