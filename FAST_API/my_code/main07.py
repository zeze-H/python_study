#查询参数query:参数验证
from fastapi import FastAPI,Query

app = FastAPI()

@app.get("/items1")
def read_item1(item_id:str=Query(123)):
    return {'item_id':item_id}
'''默认可以空值'''

@app.get("/items2")
def read_item2(item_id:str=Query(...)):
    return {'item_id':item_id}
'''必须传递'''

@app.get("/items3")
def read_item3(item_id:str=Query(...,min_length=3,max_length=10)):
    return {'item_id':item_id}
'''必须传递,限制内容长度'''

@app.get("/items4")
def read_item4(item_id:int=Query(...,gt=0,lt=100)):
    return {'item_id':item_id}
'''必须传递,限制数字大小'''


@app.get("/items5")
def read_item5(item_id:int=Query(...,alias='id')):
    return {'item_id':item_id}
'''必须传递,修改名称'''

@app.get("/items6")
def read_item6(item_id:int=Query(...,description="这个字段是用来筛选产品的ID")):
    return {'item_id':item_id}
'''必须传递,修改名称'''

@app.get("/items7")
def read_item7(item_id:int=Query(...,deprecated=True)):
    return {'item_id':item_id}
'''必须传递,被抛弃了'''

@app.get("/items8")
def read_item8(item_id:str=Query(...,regex='^a\d{2}$')):
    return {'item_id':item_id}
'''必须传递,通过正则表达式进行匹配,pattern,regex'''

if __name__ == '__main__':
    import uvicorn
    uvicorn.run('main07:app',host='127.0.0.1',port=8000,reload=True)