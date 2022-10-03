import celery
from fastapi import FastAPI
import tasks
import time
from celery.result import AsyncResult
from fastapi.responses import JSONResponse

app = FastAPI()

#root endpoint
@app.get("/")
def root():
    return JSONResponse({
        "FastAPI+Celery":"Server is running"
    })

#create your task -- !! This should be a post request
@app.get("/create_task")
def create_task():
    result = tasks.add.delay(2,2)
    return JSONResponse({
        "task_id":result.id,
        "task_status":result.status
    })

# get the status of your tasks by providing the id
@app.get("/get_status/{task_id}")
def get_status(task_id):
    result = AsyncResult(task_id)
    print(result.status)
    return JSONResponse({
        "task_id":task_id,
        "status":result.status
    })
