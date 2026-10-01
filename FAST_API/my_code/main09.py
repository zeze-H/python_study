#Field验证方式
from fastapi import FastAPI
from pydantic import BaseModel,Field
from pydantic import field_validator
from enum import Enum

app = FastAPI()

class User(BaseModel):
    name:str=Field(default='吕布')
    age:int=Field(...)#必写字段

@app.post('/users')
def creat_user(user:User):
    return user

#自定义类限制大小
class Product(BaseModel):
    price:float = Field(...,gt=0,le=1000,description='价格')
@app.post('/products')
def create_product(product:Product):
    return product

#控制字符串长度
class Account(BaseModel):
    username:str=Field(...,min_length=3,max_length=20)
    password:str=Field(...,pattern=r'^\w{6,}$')
@app.post('/accounts')
def creat_account(account:Account):
    return account

#增加备注信息
class Item(BaseModel):
    name:str=Field(...,title='商品名称',description='必填,长度不要超过五十字',examples=['手机'])
@app.post('/items')
def creat_items(item:Item):
    return item

#自定义验证规则
class User2(BaseModel):
    email:str

    @field_validator('email')
    def email_validator(cls,v):
        if "@" not in v:
            raise ValueError('邮箱格式错误')
        return v
@app.post('/users2')
def creat_user2(user:User2):
    return user

#传递多个
class Order(BaseModel):
    items:list=Field(...,min_items=1)
    address:str=Field(...,description='配送地址')
@app.post('/orders')
def create_order(order:'Order'):
    return order

#枚举方式限制返回数据
class Status(str,Enum):
    ACTIVE='active'
    INACTIVE='incvtive'

class Task(BaseModel):
    status:Status=Field(default=Status.ACTIVE)

@app.post('/tasks')
def get_task():
    return Task()

if __name__=='__main__':
    import uvicorn
    uvicorn.run(app='main09:app',host='127.0.0.1',port=8000,reload=True)