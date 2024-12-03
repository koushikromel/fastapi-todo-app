from fastapi import FastAPI
from datetime import datetime


app = FastAPI()


@app.get("/")
def home():
    # add log here
    return {"timestamp": datetime.now()}
