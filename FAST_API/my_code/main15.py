#文件响应
from fastapi import FastAPI
from fastapi.responses import Response, FileResponse

app=FastAPI()

# 方式1: Response 返回自定义内容(字节/字符串)
@app.get('/download_file')
async def get_custom_file():
    info = b'File Content'
    return Response(
        content=info,        # 文本内容
        media_type='text/plain',
        headers={'content-disposition':'attachment;filename=file.txt'}
    )

# 方式2: FileResponse 返回磁盘上的文件
# Response 没有 path 参数, 按路径返回文件必须用 FileResponse
@app.get('/download_pdf')
async def get_custom_pdf():
    return FileResponse(
        path='./data/file.pdf',      # 文件路径(文件必须真实存在)
        media_type='application/pdf',
        filename='file.pdf'          # 下载时显示的文件名
    )
if __name__=='__main__':
    import uvicorn
    uvicorn.run(app='main15:app',host='127.0.0.1',port=8000,reload=True)