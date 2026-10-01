#python原生类型注解:对类型参数的类型进行限制
from fastapi import FastAPI
from typing import Union,Optional,List

app=FastAPI()

@app.get("/items1/{item_id}")
def read_item1(item_id:int):
    return {"item_id":item_id}

@app.get("/items2/{item_id}")
def read_item2(item_id:str):
    return {"item_id":item_id}

@app.get("/items3/{item_id}")
def read_item3(item_id:Union[int,str]):#二选一
    return {"item_id":item_id}
#路径参数添加默认参数
@app.get("/items4/{item_id}")
def read_item4(item_id:Union[int,str]=110):
    '''这个不可用默认参数'''
    return {"item_id":item_id}
#查询参数添加默认参数
@app.get("/items5")
def read_item5(item_id:Union[int,str]=110):
    return {'item_id':item_id}
#查询参数类型添加none
@app.get("/items6")
def read_item6(item_id:Union[int,None]=None):
    return {'item_id':item_id}
#是Union[int,None]的缩写[int,T]
@app.get("/items7")
def read_item7(item_id:Optional[int]=None):
    return {'item_id':item_id}
#多个数据传参,只能用查询参数,不能用路径参数,因为数据太多一个"/"无法存多个数据
@app.get("/items8")
def read_item8(item_id:List):
    return {'item_id':item_id}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main06:app",host="127.0.0.1",port=8000,reload=True)