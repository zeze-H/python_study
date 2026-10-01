# FastAPI & Python 后端核心知识点复盘笔记

> 📅 整理日期：2026-08-14
> 📌 内容来源：FastAPI 学习对话记录（模块 1 ~ 4）
> 🎯 笔记定位：以「是什么 → 有什么用 → 日常例子/代码演示 → 动手测试」的结构，完整沉淀所学知识点、我的思考高光、我的欠缺与新增补充内容。

---

## 0. 学习铁律（对话中确立的要求）

1. **节奏铁律**：不发出指令，绝不推进 —— 学习节奏由学习者掌控。
2. **单块教学结构**：是什么 → 有什么用 → 日常例子/代码演示 → 动手测试。
3. **风格要求**：简洁、高信息密度、切入核心，杜绝废话、过度铺垫与无意义赞美。

---

## 1. 学习进度总览

| 模块 | 主题 | 状态 |
|---|---|---|
| 模块 1 | 类型提示（Optional / Union / List / Dict / 默认值） | ✅ 已掌握 |
| 模块 2 | 面向对象 + Pydantic 数据模型 | ✅ 已掌握 |
| 模块 3 | 装饰器（底层本质 + FastAPI 路由绑定） | ✅ 已掌握 |
| 模块 4 | 异步编程（同步vs异步 / async+await / 何时用哪个） | ✅ 已掌握 |

**当前坐标**：模块 4 完结。下一步候选方向：
1. 🛠 **项目实战** —— 把四大基石拼起来，写一个能真正在浏览器里运行的「增删改查」微型后端；
2. 🗄 **数据库模块** —— 学习 FastAPI 如何连接 MySQL / PostgreSQL 并存取数据。

---

## 2. 模块 1：类型提示（Type Hints）

### 2.1 是什么
类型提示是在变量、参数、返回值上标注「预期类型」的语法，例如 `name: str`、`-> int`。它**不会**改变程序运行逻辑，主要供编辑器提示和 FastAPI 做前置校验使用。

### 2.2 有什么用
- 让编辑器（VS Code / PyCharm）自动补全、提前标错；
- 让 FastAPI 依据类型自动完成：**请求数据校验 + 自动生成 API 文档**；
- 让代码可读性、可维护性大幅提升。

### 2.3 核心语法与代码演示

```python
from typing import Optional, Union, List, Dict

# ① Optional：可传该类型，也可不传（等价于「该类型 | None」）
def greet(name: Optional[str] = None) -> str:
    return f"你好，{name}" if name else "你好，朋友"

# ② Union：允许在多个类型中取值
def parse_id(value: Union[int, str]) -> str:
    return str(value)

# ③ 复合类型：列表 / 字典
def calc_total(prices: List[float]) -> float:
    return sum(prices)

def find_score(score_map: Dict[str, int], name: str) -> Optional[int]:
    return score_map.get(name)

# ④ 默认值：不传参时使用默认值
def repeat(message: str = "Hello", times: int = 1) -> str:
    return message * times
```

> 💡 Python 3.10+ 简化写法：`Optional[str]` 可写成 `str | None`；`Union[int, str]` 可写成 `int | str`。

### 2.4 动手测试（自测）
1. 如何声明一个「可空」的字符串参数？ → `Optional[str]`（或 `str | None`），配合默认值 `= None` 即变为选填。
2. 一个参数既能是 int 又能是 float，怎么写？ → `Union[int, float]`（或 `int | float`）。
3. 函数返回「字符串列表」怎么写？ → `-> List[str]`。

### 2.5 我的思考与欠缺
- ✅ **高光**：理解了 FastAPI 如何利用类型提示做前置校验 —— **类型即校验规则**。
- ⚠️ **欠缺**：早期混淆字符串 `"20"` 与整数 `20`；只看到「类型可以自动转换」，忽略了「缺失必填项会直接报错拦截」（详见模块 2）。

---

## 3. 模块 2：面向对象（OOP）与 Pydantic 数据模型

### 3.1 类与实例
- **类（Class）**：设计图，定义有哪些属性 / 行为。
- **实例（Instance）**：按设计图造出来的具体实体。
- **关键**：给实例属性赋值必须用 `.`（例如 `user_1.username = "小明"`）。

```python
class User:
    def __init__(self, username: str, age: int):
        self.username = username   # 用 . 把属性绑定到实例
        self.age = age

user_1 = User("小明", 20)   # user_1 是实例
print(user_1.username)      # 小明
user_1.age = 21             # 修改实例属性必须用 .
```

### 3.2 继承
- 子类继承父类的所有属性 / 方法，并可以添加自己独有的属性；
- 核心目的：**代码复用**。

```python
class Admin(User):                       # Admin 继承 User
    def __init__(self, username: str, age: int, level: int = 1):
        super().__init__(username, age)  # 复用父类的初始化逻辑
        self.level = level               # 子类独有的属性
```

### 3.3 Pydantic BaseModel —— FastAPI 的「数据安检员」
- 只要类继承 `BaseModel` 并写好类型提示，FastAPI 就会自动校验前端传来的数据；
- `Optional` + 默认值（`= None`）可实现「必填 / 选填」控制。

```python
from pydantic import BaseModel
from typing import Optional

class Product(BaseModel):
    name: str                          # 必填：缺失会报错拦截
    price: float                       # 必填
    stock: int = 0                     # 选填：有默认值
    description: Optional[str] = None  # 选填

# 校验规则演示：
# {"name": "鼠标", "price": 99.9}                ✅ 合法（stock/description 用默认值）
# {"price": 99.9}                                ❌ 报错：缺少必填项 name
# {"name": "鼠标", "price": "99.9"}              ✅ 类型自动转换 "99.9" → 99.9
```

### 3.4 动手测试（自测）
1. 写一个继承 `BaseModel` 的类，包含必填 `email: str` 和选填 `age: Optional[int] = None`。
2. 传入 `{"email": "a@b.com", "age": "18"}`，Pydantic 会如何处理？ → `age` 自动转成整数 `18`。
3. 传入 `{"age": 18}` 会怎样？ → 报错，缺少必填项 `email`。

### 3.5 我的思考与欠缺
- ✅ **高光**：精准总结出 BaseModel 的本质 = **类型审核器**；在 2.3 实战中一次性完美写出了包含 BaseModel、Optional、类型提示、默认值的 Product 类。
- ⚠️ **欠缺**：
  1. 初期给 `user_1` 赋值时，忘记了用 `.` 进行属性绑定；
  2. 混淆了字符串 `"20"` 与整数 `20`；
  3. 判断请求是否放行时，只关注「类型可以自动转换」，忽略了「缺失必填项（无默认值）会直接导致报错拦截」。

---

## 4. 模块 3：装饰器（Decorators）

### 4.1 是什么（底层本质）
装饰器 = **「接收一个函数，返回一个新函数」的包装器**。它能在**不修改原函数内部代码**的前提下，在函数执行前后追加逻辑。

`@` 只是语法糖：`@decorator` 等价于 `func = decorator(func)`。

### 4.2 有什么用
- 日志记录、权限校验、计时、缓存等「横切逻辑」的复用；
- FastAPI 用它把「网址路径」与「处理函数」绑定（路由）。

### 4.3 代码演示：手写标准装饰器

```python
import time

def log_time(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)    # 执行原函数
        print(f"{func.__name__} 耗时 {time.time() - start:.3f}s")
        return result                     # 把原函数结果原样返回
    return wrapper

@log_time
def add(a, b):
    return a + b

# 等价写法：add = log_time(add)
print(add(1, 2))   # 输出：add 耗时 0.000s / 3
```

**执行顺序**：`wrapper` 先记录开始时间 → 调用原 `add` → 打印耗时 → 返回结果。

### 4.4 FastAPI 中的路由绑定

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/profile")     # 「登记造册」：把路径 /profile 与下面的函数死死绑定
def get_profile():
    return {"name": "小明"}

# 等价于 get_profile = app.get("/profile")(get_profile)
```

收到 `GET /profile` 请求时，FastAPI 自动调用 `get_profile()` 并返回结果。

### 4.5 动手测试（自测）
1. 装饰器在 `@` 语法下的本质是什么？ → `func = decorator(func)`。
2. 为什么 `wrapper` 要 `return result`？ → 保证原函数的返回值能一层层传递出去。
3. 如何在不改原函数的情况下打印日志？ → 用装饰器在 `wrapper` 前后追加 `print`。

### 4.6 我的思考与欠缺
- ✅ **高光**：**主动叫停、拒绝死记硬背**，准确指出原有讲解不够透彻，要求先扒开底层看本质；随后徒手写出了含内部 `wrapper` 函数和正确执行顺序的标准装饰器，证明彻底看透了它的运行机制。

---

## 5. 模块 4：异步编程（Async/Await）

### 5.1 同步 vs 异步（4.1）
- **同步（Sync）**：遇到等待就「死等」，哪怕闲着也不干别的 → 总时间变长。
- **异步（Async）**：把「干等」的时间压榨出来去处理别的任务 → 效率最大化。

**日常类比**：洗衣机洗衣服时 —— 同步 = 站在洗衣机前发呆；异步 = 去扫地 / 拖地，洗完再回来拿。

在 FastAPI 里，「洗衣服」这种耗时动作通常对应 **去数据库查询数据** 或 **向别的网站发送网络请求**。FastAPI 底层会在等待时间里接待千千万万个其他用户的请求 —— 这就是它单机扛高并发的原理。

### 5.2 async def 与 await 基础语法（4.2）
- `async def`：定义**异步函数**，告诉 Python「里面有耗时等待的动作，请按异步模式处理」。
- `await`：标记暂停点，**交出控制权**（把服务器释放出去干别的活）。
- ⚠️ 注意：`await` 只能写在 `async def` 定义的函数内部。

```python
import asyncio

async def get_user_data():
    print("1. 开始连接数据库...")
    await asyncio.sleep(2)      # 暂停 2 秒，但不卡死，控制权交出去
    print("2. 数据库数据获取成功！")
    return {"id": 1}
```

> 💡 补充：`async def` 函数被调用时不会立刻执行，而是返回一个**协程对象**，必须用 `await` 或 `asyncio.run()` 驱动。

**动手练习（我已完成 ✅）**：

```python
import asyncio

async def fetch_data():
    print("正在请求数据")
    await asyncio.sleep(1)
    print("数据请求成功")
```

### 5.3 避坑：什么时候用 async def，什么时候用普通 def（4.3）⚠️ 必须掌握

**核心判别：你的函数在干嘛？**

| 类型 | 特征 | 例子 |
|---|---|---|
| I/O 密集型（需要「等」） | 等待外部资源 | 查数据库、发网络请求、读写硬盘文件 |
| CPU 密集型（需要「算」） | 疯狂计算 | 视频转码、图像压缩、上亿次循环、加解密 |

**FastAPI 终极规则：**

| 场景 | 用哪个 | 原因 |
|---|---|---|
| 代码里有**真实的 await 操作**（异步数据库驱动 / httpx） | `async def` | 交出控制权，高并发 |
| **CPU 密集「死运算」** | 普通 `def` | FastAPI 自动扔进**后台线程池**，绝不卡主服务器 |
| 用**不支持异步的老库**（老版 requests、`time.sleep()`） | 普通 `def` | 同上，线程池兜底 |

**致命踩坑**：做死运算却偏偏写 `async def` → FastAPI 认为「你懂你在干嘛」，强行让主服务器亲自去算 → 主循环被死死卡住，其他用户全部白屏等待。

```python
# ✅ 正确：I/O 等待 + 库支持异步 → async def
@app.get("/ai")
async def call_openai():
    async with httpx.AsyncClient() as client:
        resp = await client.post("https://api.openai.com/v1/...")
    return resp.json()

# ✅ 正确：CPU 密集 → 普通 def（自动进线程池）
@app.post("/transcode")
def transcode_video():
    # 视频转码这种「死运算」
    return {"ok": True}

# ✅ 正确：老库不支持异步 → 普通 def
@app.get("/old-site")
def fetch_with_requests():
    import requests
    return requests.get("https://example.com").text
```

### 5.4 终极判别测试（我已完成 ✅）
1. **接口 A**：接收用户上传的视频，并在服务器本地做**极度耗时的格式转码（视频压缩）** → **普通 def**（CPU 密集，扔进线程池，主服务器不卡死）。
2. **接口 B**：接收查询请求，通过网络**调用 OpenAI API** 等待 AI 回复 → **async def**（网络 I/O，交出控制权，高并发）。

### 5.5 我的思考与欠缺
- ✅ **高光**：
  1. 生活类比嗅觉极其敏锐：瞬间判断「洗衣机 + 扫地」= 异步；
  2. 精准提炼出 await 的灵魂作用 = **交出控制权**；
  3. 终极判别测试全对：视频压缩选 `def`，请求 OpenAI 选 `async def`。
- ⚠️ **欠缺**：知识点本身没有踩坑；但作为学习者非常严格地把控节奏，及时纠正了导师（AI）单方面推进进度的问题 —— 这其实是优点，继续保持。

---

## 6. 新增内容与补充（额外沉淀的知识）

### 6.1 FastAPI 启动的三种方式
1. **命令行**：`uvicorn main01:app --reload`（`--reload` = 热重载，改代码自动重启）；
2. **调试运行**：`fastapi dev main01.py`（需安装 `fastapi[standard]`）；
3. **直接运行脚本**：脚本末尾写：

```python
import uvicorn

if __name__ == "__main__":
    uvicorn.run("main02:app", host="127.0.0.1", port=8000, reload=True)
```

### 6.2 路径参数 vs 查询参数

```python
# 路径参数：访问 /hello/小明 → name = "小明"
@app.get("/hello/{name}")
def hello_name(name: str):
    return {"message": f"你好，{name}!"}

# 查询参数：访问 /repeat?message=Hi&times=3
@app.get("/repeat")
def repeat_message(message: str = "Hello", times: int = 1):
    return {"result": message * times}
```

### 6.3 自动文档（白送的功能）
启动后访问：
- `/docs` → Swagger UI 交互式文档；
- `/redoc` → ReDoc 文档。

**类型提示写得好 → 校验和文档都是白送的。**

### 6.4 Pydantic 校验细节再强调
- 「类型可自动转换」≠「必填项可缺失」；
- 必填项（无默认值的属性）缺失 → 直接报错拦截（422 校验错误）；
- 字符串数字（如 `"99.9"`）传给 float 字段 → 自动转换成功。

### 6.5 线程池底层补充
普通 `def` 路由由 FastAPI 放入**线程池（ThreadPool）**执行，事件循环不会被阻塞；所以即使同步代码很多，只要单个请求不算太久，主服务器依然能同时服务多个用户。而 `async def` 直接跑在事件循环里，靠「交出控制权」实现并发。两者都能处理 I/O，关键看你的**库支不支持异步**。

---

## 7. 总结

已打通 FastAPI 最核心的四大基石：

| 基石 | 一句话记忆 |
|---|---|
| 类型提示 | 类型即校验，文档白送 |
| OOP + Pydantic | BaseModel 是「数据安检员」 |
| 装饰器 | 接收函数、返回函数，`@` 是语法糖 |
| 异步 | I/O 用 async 交出控制权，CPU 用 def 进线程池 |

**下一步两个方向：**
1. 🛠 **项目实战**：把四大基石拼起来，写一个能真正在浏览器里运行的「增删改查」微型后端；
2. 🗄 **数据库模块**：学习 FastAPI 如何连接 MySQL / PostgreSQL 并存取数据。

> 学习铁律继续生效：**不发出指令，绝不推进。** 😄
