#路径参数
from fastapi import FastAPI

app = FastAPI()

@app.get("/args/id1")
def path_args():
    return {"message":"id1"}

@app.get("/args1/{id}")
def path_args1(id):
    return {"message":id}
#自上而下去查询路径
@app.get("/args2/{id}")
def path_args2(id):
    return {"message2":id}
#自定义路径参数 以及参数类型
@app.get("/args3/{id}/{name}")
def path_args3(id:int,name:str):
    return {"message":id,"name":name}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run('main03:app',host="127.0.0.1",port=8000,reload=True)
