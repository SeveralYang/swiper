import os
from celery import Celery

# 加载DJANGO 的 settings.py
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "swiper.settings")

celery_app = Celery("swiper")
celery_app.config_from_object("worker.config")
celery_app.autodiscover_tasks() # 自动加载


def call_by_worker(func):
    """自定义修饰器"""
    task = celery_app.task(func)
    return task.delay