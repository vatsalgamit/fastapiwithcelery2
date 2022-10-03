from celery import Celery
import time

app = Celery("tasks", broker='redis://localhost:6379/0', backend='redis://localhost')

@app.task
def add(x, y):
    time.sleep(5)
    return x + y