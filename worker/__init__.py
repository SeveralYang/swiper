import os
from celery import Celery

# 加载DJANGO 的 settings.py
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "swiper.settings")

# class Config:
#     broker_url = 'redis://127.0.0.1:6379/0'
#     broker_pool_limit = 1000
#     timezone = 'Asia/Shanghai'
#     accept_content = ['pickle','json']
#     task_serializer = 'pickle'
#     result_backend = 'redis://127.0.0.1:6379/0'
#     result_serializer = 'pickle'
#     result_cache_max = 10000 # 任务的过期时间   
#     result_expires = 3600  # 任务结果的过期时间
#     worker_redirect_stdouts_level = 'INFO'

celery_app = Celery("swiper")
celery_app.config_from_object("worker.config")
# celery_app.config_from_object(Config)
celery_app.autodiscover_tasks(None) # 自动加载


def call_by_worker(func):
    """自定义修饰器"""
    task = celery_app.task(func)
    return task.delay