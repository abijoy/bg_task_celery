import os
from celery import Celery

# set the default Django seetings module for the 'calery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'proj.settings')

app = Celery('proj')

'''
Using a string here means the worker doesn't have to 
serialize the configuaration object to child processes.
'''

'''
-namecpace=Celery means all celery-related configurarion keys
should have a `CELERY_` prefix.
'''
app.config_from_object('django.conf:settings', namespace='CELERY')


# Load the task modules from all the registered Django apps
app.autodiscover_tasks()

@app.task(bind=True, ignore_result=True)
def debug_task(self):
    print(f'Request: {self.request!r}')


