import os
from celery import Celery


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'first_work_in_django.settings')

app = Celery('work_django')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
