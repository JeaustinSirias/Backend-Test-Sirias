from __future__ import absolute_import
from django.conf import settings
from celery import Celery
import os

# Allow run administrative tasks like manage.py
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "main.settings")

# Celery asynchronous tasks
func = Celery('main', broker='pyamqp://guest@localhost//')

# Setup
func.config_from_object('django.conf:settings', namespace='CELERY')
func.autodiscover_tasks()

'''
func.conf.update(
    BROKER_URL = '//127.0.0.1:8000/',
)
'''


# Debugging
@func.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))