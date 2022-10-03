import celery
from fastapi import FastAPI
import tasks
import time
from celery.result import AsyncResult
from fastapi.responses import JSONResponse

app = FastAPI()

@app.get("/")
def read_root():
    result = tasks.add.delay(2,2)
    result1 = {
        "task_id": result.id,
        "task_status": result.status,
        "task_result": result.result
    }
    time.sleep(5)
    result = {
        "task_id": result.id,
        "task_status": result.status,
        "task_result": result.result
    }

    return JSONResponse({
        "result1":result1,
        "result":result
    })

