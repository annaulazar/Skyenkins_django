import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Skyenkins_django.settings')

app = Celery('Skyenkins_django')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()


app.conf.beat_schedule = {
    'verify-file-every-five-minutes': {
        'task': 'files.tasks.verify_file',
        'schedule': crontab(minute='*/5'),
    },

}