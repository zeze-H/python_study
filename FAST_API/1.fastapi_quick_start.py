from fastapi import FastAPI


app=FastAPI()

@app.get("/")

def home():
    return {"user_id":1001}
    