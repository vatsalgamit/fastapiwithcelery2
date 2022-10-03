import celery
from fastapi import FastAPI
import tasks
import time
from celery.result import AsyncResult
from fastapi.responses import JSONResponse

app = FastAPI()

@app.get("/test")
def test():
    return JSONResponse({
        "PING":"PONG"
    })

@app.get("/create_task")
def create_task():
    result = tasks.add.delay(2,2)

    return JSONResponse({
        "result":result.id
    })

@app.get("/get_status/{task_id}")
def get_status(task_id):
    result = AsyncResult(task_id)
    print(result.status)
    return JSONResponse({
        "status":result.status
    })
