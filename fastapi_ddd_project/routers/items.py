from fastapi import APIRouter, Depends, status
from pydantic import BaseModel
from typing import Annotated
# 导入刚刚写好的 yield 依赖
from dependencies import get_db_session

router = APIRouter(prefix="/items", tags=["商品/任务管理"])

class ItemCreate(BaseModel):
    title: str
    price: float

@router.get("/")
def get_all_items(db: Annotated[dict, Depends(get_db_session)]):
    """
    演示 yield 依赖：观察终端控制台里的日志打印顺序！
    """
    print(f"🟡 [业务处理] 2. 路由正在使用 {db['session_id']} 查询所有商品数据...")
    return {
        "msg": "获取商品列表成功！",
        "used_session": db["session_id"]
    }