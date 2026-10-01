from fastapi import Header, HTTPException, status, Depends
from typing import Annotated, Optional

# 模拟数据库里的用户数据
FAKE_USERS_DB = {
    "token_zhangsan": {"user_id": 1001, "username": "张三", "role": "user"},
    "token_admin": {"user_id": 9999, "username": "超管", "role": "admin"}
}


# ---------- 第一级依赖：从请求头提取并验证 Token ----------
def verify_token(x_token: Annotated[Optional[str], Header()] = None):
    if not x_token:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="请求头缺失 X-Token，请先登录！"
        )
    user_info = FAKE_USERS_DB.get(x_token)
    if not user_info:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="无效的 X-Token！"
        )
    return user_info  # 把解析出来的用户信息交出去


# ---------- 第二级依赖：嵌套依赖 verify_token，判别是否是管理员 ----------
def get_current_admin(current_user: Annotated[dict, Depends(verify_token)]):
    # 注意看：这个函数本身也使用了 Depends(verify_token)！
    if current_user.get("role") != "admin":
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="权限不足：只有管理员才能执行此操作！"
        )
    return current_user


# ---------- 第三级依赖：带 yield 的数据库会话生命周期管理 ----------
def get_db_session():
    """
    模拟一个数据库会话的完整生命周期
    """
    print("\n🟢 [DB 准备] 1. 从连接池借出一个数据库连接 (Session 开启)...")
    db_session = {"session_id": "sess_998877", "status": "connected"}
    
    try:
        # yield 把 db_session 借给路由函数使用
        # 此时函数在此暂停，把控制权交给路由函数
        yield db_session
    finally:
        # 路由函数执行完毕后（无论成功还是报错），FastAPI 一定会回到这里！
        print("🔴 [DB 清理] 3. 释放并归还数据库连接回连接池 (Session 关闭)!\n")