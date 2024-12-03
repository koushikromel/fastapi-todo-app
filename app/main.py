from fastapi import FastAPI
from datetime import datetime


app = FastAPI()


@app.get("/")
def home():
    return {"timestamp": datetime.now()}
