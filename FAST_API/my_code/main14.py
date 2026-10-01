#响应列表
from fastapi import FastAPI,Query
from pydantic import BaseModel
from typing import List,Optional

app = FastAPI()


class Item(BaseModel):
    id:int
    name:str
    price:float
    category:str
class Paginaton(BaseModel):
    total:int
    page:int
    page_size:int
    total_pages:int
class ListResponse(BaseModel):
    status:str='success'
    data:List[Item]
    Paginaton:Paginaton


DB = [Item(id=i,name=f'apple{i}',
           price=100.0*i,
           category= 'ipad'
           if i%2==0 else 'iphone')
      for i in range(1,101)]

@app.get('/items1')
async def get_items1():
    return['apple1','apple2','apple3']

@app.get("/items2")
async def get_items2():
    return DB

#数据过滤与分页

@app.get('/item3')
async def get_items3(category:Optional[str]=Query(None,description='分类')):
    filtered_items = DB
    if category:
        filtered_items = [item for item in DB if item.category == category]

    return filtered_items

@app.get('/item4')
async def get_items4(page:int=Query(1,ge=1,description="页码"),
                     page_size:int=Query(10,gt=1,le=100,description="数量"),
                     category:Optional[str]=Query(None,description="分类")):
#对数据进行过滤
    filtered_items=DB
    if category:
        filtered_items = [item for item in DB if item.category == category]
#对数据进行分页
    total = len(filtered_items)
    #计算总页数
    total_pages=(total+page_size-1)//page_size
    '''total//page_size=count'''
    '''total%page_size = remain if remain > 0 count+=1'''
    
    # 计算这一页从第几条数据开始取
    # 例：第2页、每页10条 → start = (2-1)*10 = 10，从下标10开始（即第11条）
    start = (page - 1) * page_size

    # 计算这一页取到第几条结束（不含这条）
    # 例：start=10、每页10条 → end = 10+10 = 20，取下标 10~19
    end = start + page_size

    return filtered_items[start:end]


@app.get('/item5')
async def get_items5(page:int=Query(1,ge=1,description="页码"),
                     page_size:int=Query(10,gt=1,le=100,description="数量"),
                     category:Optional[str]=Query(None,description="分类")):
#对数据进行过滤
    filtered_items=DB
    if category:
        filtered_items = [item for item in DB if item.category == category]
#对数据进行分页
    total = len(filtered_items)
    #计算总页数
    total_pages=(total+page_size-1)//page_size
    '''total//page_size=count'''
    '''total%page_size = remain if remain > 0 count+=1'''
    start = (page - 1) * page_size
    end = start + page_size

    return ListResponse(data=filtered_items[start:end],
                        Paginaton=Paginaton(total=total,
                                            page=page,
                                            page_size=page_size,
                                            total_pages=total_pages))

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app="main14:app",host='127.0.0.1',port=8000,reload= True)