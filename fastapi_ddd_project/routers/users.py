from fastapi import APIRouter, Depends, status
from typing import Annotated
# 从 dependencies.py 导入我们做好的依赖工具
from dependencies import verify_token, get_current_admin

router = APIRouter(prefix="/users", tags=["用户管理"])

# ① 普通用户接口：只要有合法 Token 就能查看个人中心
@router.get("/me")
def get_my_profile(user: Annotated[dict, Depends(verify_token)]):
    """
    通过 Depends(verify_token) 自动注入当前登录用户信息
    """
    return {
        "msg": "获取个人信息成功！",
        "current_user": user
    }


# ② 敏感管理接口：只有携带管理员 Token 才能进
@router.get("/admin/dashboard")
def get_admin_dashboard(admin_user: Annotated[dict, Depends(get_current_admin)]):
    """
    通过 Depends(get_current_admin) 多层校验管理员权限
    """
    return {
        "msg": "欢迎进入超级管理后台！",
        "admin_info": admin_user
    }