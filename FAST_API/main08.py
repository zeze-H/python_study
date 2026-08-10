#路径参数Path
from typing import Annotated
from fastapi import FastAPI, Path
from enum import Enum
from pydantic import BeforeValidator

app = FastAPI()

@app.get('/items1/{item_id}')
def read_item1(item_id:int):
    return{'item_id':item_id}
#用path方式和默认路径参数写法一样,必须强制输入内容
@app.get('/items2/{item_id}')
def read_item2(item_id:int=Path(...)):
    return{'item_id':item_id}
#限制输入大小:大于gt小于lt
@app.get('/items3/{item_id}')
def read_item3(item_id:int=Path(...,lt=100,gt=18)):
    return{'item_id':item_id}
#正则表达式
@app.get('/items4/{item_id}')
def read_item4(item_id: str = Path(..., pattern=r"^a\d{2}$")):
    return{'item_id':item_id}
'''regex或者pattern'''


#通过枚举设定必须输入指定值
class ModelName(str,Enum):
    alexnet='alexnet'
    resnet='resnet'
    lenet='lenet'

@app.get('/items5/{model}')
def read_item5(model:ModelName):
    return {'model':model}

#创建自定义验证规则,一般规则用正则表达式就可以
def validate(value):
    if not value.startswith('P-'):
        raise ValueError('必须以P-开头')
    return value
#创建带验证的类型别名
Item = Annotated[str,BeforeValidator(validate)]
@app.get('/items6/{item_id}')
def read_item6(item_id:Item):
    return {'item_id':item_id}



if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app='main08:app',host="127.0.0.1",port=8000,reload=True)