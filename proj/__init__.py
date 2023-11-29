'''
By Importing celery app here ensures 
the celery app is always ready to be used
whenever we start the project.
'''
from .celery import app as celery_app

__all__ = ('celery_app')
