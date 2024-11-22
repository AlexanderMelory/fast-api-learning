from celery import Celery

from app.settings import settings

celery = Celery('tasks', broker=settings.CELERY_BROKER, include=['app.tasks.tasks'])
