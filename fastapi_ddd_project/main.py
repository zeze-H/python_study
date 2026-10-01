from fastapi import FastAPI
from contextlib import asynccontextmanager
from routers import users, items

# ======================== 核心：定义全局 Lifespan 生命周期 ========================
@asynccontextmanager
async def lifespan(app: FastAPI):
    # ---------- 1. 服务器开机阶段 (Startup) ----------
    print("\n🟢 [系统开机] 正在初始化全局资源：连接数据库连接池、加载配置...")
    # 模拟在开机时往 app 状态机里存入一个全局共享资源
    app.state.global_config = {"db_status": "ready", "version": "1.0.0"}
    
    # ---------- 2. 维持运行阶段 (Yield) ----------
    # yield 相当于把电闸推上去，此时服务器在 8000 端口持续对外提供服务
    yield
    
    # ---------- 3. 服务器关机阶段 (Shutdown) ----------
    # 当你在终端按下 Ctrl + C 时，程序必定会自动跳到这里执行收尾工作！
    print("🔴 [系统关机] 正在安全释放全局资源：断开数据库连接池、保存日志...\n")


# ---------- 将 lifespan 注册给 FastAPI 实例 ----------
app = FastAPI(title="模块 1.3：Lifespan 生命周期实操", lifespan=lifespan)

# 挂载子路由
app.include_router(users.router)
app.include_router(items.router)

@app.get("/")
def home():
    return {
        "msg": "服务运行中！",
        "global_status": app.state.global_config
    }