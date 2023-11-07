import time
from celery import Celery

broker = 'redis://127.0.0.1:6379'
backend =  'redis://127.0.0.1:6379/0'
custom_task_name = Celery('task_name',broker=broker,backend=backend)

@custom_task_name.task
def add(x,y):
    time.sleep(5)
    return x + y 

if __name__ == "__main__":
    print(add(10,5))