#文件上传
from fastapi import FastAPI,File,UploadFile,HTTPException,Form
from pathlib import Path

app=FastAPI()
#上传文件
@app.post('/upload1')
def upload_file1(file:bytes = File(...)):
    with open('./data/file.jpg','wb')as f:
        f.write(file)
    return{"msg":"文件上传成功"}
#异步上传大文件
@app.post('/upload2')
async def upload_file2(file:UploadFile):
    with open(f"./data/{file.filename}",'wb')as f:
        f.write(await file.read())
    return {"msg":"文件上传成功"}
#上传多个文件(没写接收)
@app.post("/batch-upload")
def batch_upload(files:list[UploadFile]=File(...)):
    return {"count":len(files),"names":[f.filename for f in files]}
#限制上传格式()
ALLOWED_EXTENSIONS = {'.jpg','.png'}
@app.post('/upload-image/')
def upload_image(file:UploadFile):
    #验证文件格式(提取后缀)
    ext = Path(file.filename).suffix.lower()
    if ext not in ALLOWED_EXTENSIONS:
        raise HTTPException(400,"不支持的文件扩展名")
    #保存文件的逻辑
    return {'msg':'文件上传成功 '}
#表单和图片一起上传
@app.post('/submit-form')
def submit_form(uname:str=Form(...),file:UploadFile=File(...)):
    return {'uname':uname,"filename":file.filename}
if __name__=='__main__':
    import uvicorn
    uvicorn.run('main11:app',host="127.0.0.1",port=8000,reload=True)
