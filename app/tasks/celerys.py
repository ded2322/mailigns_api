from celery import Celery
from celery.beat import crontab
from datetime import timedelta

from app.config import settings

celery = Celery(
    "tasks", broker=f"redis://{settings.REDIS_PORT}", include=["app.tasks.tasks"]
)

celery.conf.beat_schedule = {
    "task-name": {"task": "app.tasks.tasks", "schedule": crontab(minute=0, hour="*")},
}
celery.conf.timezone = "Asia/Barnaul"
