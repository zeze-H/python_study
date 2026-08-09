#AI生成程序
# 1. 导入 FastAPI 和 uvicorn
# FastAPI 是 Web 框架类，Uvicorn 是 ASGI 服务器，用于运行 FastAPI 应用
from fastapi import FastAPI
import uvicorn

# 2. 创建 FastAPI 应用实例
# 这个 app 实例是整个 Web 应用的核心，所有路由和中间件都挂载在它上面
app = FastAPI(
    title="Hello World API",       # OpenAPI 文档中显示的项目名称
    description="第一个 FastAPI 示例程序",  # 项目描述
    version="1.0.0",               # 版本号
)

# 3. 定义根路径路由
# @app.get("/") 是一个装饰器，告诉 FastAPI 当收到 GET 请求且路径为 "/" 时，
# 调用下面这个函数来处理请求
@app.get("/")
def hello_world():
    """
    根路径的请求处理函数
    访问 http://127.0.0.1:8000/ 时会执行此函数
    返回一个 JSON 格式的响应
    """
    return {"message": "Hello, World!", "status": "ok"}

# 4. 定义带路径参数的路由
# {name} 是一个路径参数，FastAPI 会自动从 URL 中提取并传给函数
@app.get("/hello/{name}")
def hello_name(name: str):
    """
    接收路径参数 name，返回个性化问候
    例如访问 http://127.0.0.1:8000/hello/小明 会返回 "你好，小明!"
    name 的类型注解 str 会被 FastAPI 用于数据校验和自动生成文档
    """
    return {"message": f"你好，{name}!"}

# 5. 定义带查询参数的路由
# 不在路径中的参数默认为查询参数，如 ?times=3
@app.get("/repeat")
def repeat_message(message: str = "Hello", times: int = 1):
    """
    查询参数示例
    访问 http://127.0.0.1:8000/repeat?message=Hi&times=3 会把 "Hi" 重复 3 次
    message 和 times 都有默认值，所以不传参也可以访问
    """
    return {"result": message * times}

# 6. 程序入口
# __name__ == "__main__" 确保脚本被直接运行时才执行下面的代码
# reload=True 表示开启热重载，代码修改后自动重启服务器（开发时很有用）
if __name__ == "__main__":
    uvicorn.run(
        "main02:app",         # 导入字符串，reload 模式要求用此格式
        host="127.0.0.1",     # 绑定本机地址，仅本地可访问
        port=8000,            # 监听 8000 端口
        reload=True,          # 开发模式热重载
    )

# ============ 运行方式 ============
# 方式一：直接运行本脚本
#   python main.py
#
# 方式二：命令行运行（推荐，不需要 if __name__ == "__main__" 部分）
#   uvicorn main:app --host 127.0.0.1 --port 8000 --reload
#
# 方式三：启动后用浏览器访问
#   http://127.0.0.1:8000/              → {"message": "Hello, World!", "status": "ok"}
#   http://127.0.0.1:8000/hello/小明     → {"message": "你好，小明!"}
#   http://127.0.0.1:8000/repeat?message=Hi&times=3 → {"result": "HiHiHi"}
#   http://127.0.0.1:8000/docs          → 自动生成的 Swagger UI 交互文档
#   http://127.0.0.1:8000/redoc         → 自动生成的 ReDoc 文档