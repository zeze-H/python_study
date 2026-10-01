# 响应数据 json + response_model 用法
from fastapi import FastAPI
from pydantic import BaseModel
from typing import Union, TypeVar, Generic

app = FastAPI()

# ========== 例1：直接返回字典 ==========
@app.get('/items/dict')
async def get_items_dict():
    return {"name": "张三", "age": '18'}


# ========== 定义一个数据模型 ==========
class Item(BaseModel):
    id: int
    name: str
    tags: list[str] = []


# ========== 例2：返回模型对象（没写 response_model）==========
@app.get('/items/model')
async def get_items_model():
    return Item(id=2, name="iphone")


# ========== 例3：返回模型对象 + response_model ==========
@app.get('/items/model2', response_model=Item, response_model_exclude_unset=True)
async def get_items_model2():
    # response_model=Item  ：响应必须符合 Item 结构（多余的字段过滤、类型自动转换）
    # exclude_unset=True   ：没被显式设置的字段（用了默认值的）不出现在响应里
    return Item(id=2, name="iphone")


# ========== 泛型模型：统一响应格式 ==========
# 泛型 = "T 具体是什么类型，由调用方决定"（先占个位置，用的时候再填）
T = TypeVar('T')   # 声明一个类型占位符，名字叫 T（必须传字符串）

class successResponse(BaseModel, Generic[T]):
    status: str = "success"   # 成功时固定的状态
    data: T                   # data 的类型 = 传入的 T

class errorResponse(BaseModel):
    status: str
    message: str
    code: int


# ========== 例4（model3）：根据参数返回成功或失败 ==========
@app.get('/items/{item_id}', response_model=Union[successResponse[Item], errorResponse])
async def get_items_model3(item_id: int):
    # Union[A, B] = 响应要么是 A 这种结构，要么是 B 这种结构
    if item_id == 1:
        item = Item(id=1, name="iphone", tags=["red", "black"])
        return successResponse[Item](data=item)   # 用 Item 填 T，data 就是 Item 类型
    else:
        return errorResponse(status="error", message="Item没有找到", code=404)


if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app="main13:app", host='127.0.0.1', port=8000, reload=True)
