# 表单数据（Form）
# 安装: pip install python-multipart==0.0.32
#
# 表单(form)是一种"请求体编码格式"，和 JSON 是不同的两种格式：
#   JSON 格式:  {"username":"abc","password":"123"}
#   表单格式:   username=abc&password=123    (key=value 用 & 连接)
# 表单是浏览器原生支持的提交格式(传统HTML表单、文件上传都用它)
# 注意: 请求体按什么格式解析由"标注"决定，但"返回"永远是 return 的 JSON
from fastapi import FastAPI,Form
from pydantic import BaseModel, Field
from typing import Annotated# 声明类型
app=FastAPI()

# 方式1: Form(...) 用于"单个字段"
# 每个参数用 Form(...) 单独声明成表单的一个字段
@app.post('/login1')
def login1(username:str=Form(...),password:str=Form(...)):
    return {"username":username,'password':password}

class User1(BaseModel):
    username:str
    password:str

# 方式2: Annotated[模型, Form()] 用于"整个自定义类"
# 模型参数默认会被当成 JSON 请求体(这是FastAPI的默认规则)，
# 必须用 Annotated 贴 Form() 标签，改写成按表单格式解析
# 效果: 模型的每个字段(username/password)都会变成表单的一个字段
@app.post('/login2')
def login2(user:Annotated[User1,Form()]):
    return user

class User2(BaseModel):
    username:str=Field(...)
    password:str=Field(...)

# 方式3: 和方式2一样用 Annotated 声明表单
# 区别: 字段用 Field(...) 强制必填(不传就 422 报错)
@app.post('/login3')
def login3(user:Annotated[User2,Form()]):
    return user

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app='main10:app',host='127.0.0.1',port=8000,reload=True)
