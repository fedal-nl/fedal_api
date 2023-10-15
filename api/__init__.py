from .celery import app as celery_app
# import celery every time the application starts

__all__ = ['celery_app']