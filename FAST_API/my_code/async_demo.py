# async_demo.py —— 用生活实验讲明白 async/await
import asyncio
import time

# ============ 例 1：同步（傻等） ============
def slow_sync(name, seconds):
    print(f"  {name}: 开始干活")
    time.sleep(seconds)           # 干等，期间什么都做不了
    print(f"  {name}: 干完了")
    return name

# ============ 例 2：异步（不等） ============
async def slow_async(name, seconds):
    print(f"  {name}: 开始干活")
    await asyncio.sleep(seconds)  # 不傻等，把控制权让出去
    print(f"  {name}: 干完了")
    return name

async def main():
    print("【同步版】3 个人排队干活，每人 1 秒：")
    t0 = time.time()
    slow_sync("A", 1); slow_sync("B", 1); slow_sync("C", 1)
    print(f"  同步总耗时: {time.time() - t0:.2f} 秒\n")

    print("【异步版】3 个人同时干活，每人 1 秒：")
    t0 = time.time()
    await asyncio.gather(slow_async("A", 1), slow_async("B", 1), slow_async("C", 1))
    print(f"  异步总耗时: {time.time() - t0:.2f} 秒")

asyncio.run(main())
