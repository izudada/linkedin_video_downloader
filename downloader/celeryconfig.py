from celery import Celery
from celery.schedules import crontab


CELERY_BROKER_URL = 'amqp://guest:guest@localhost:5672//',  
CELERY_RESULT_BACKEND = 'rpc://'  
CELERY_TIMEZONE = 'UTC'
CELERY_IMPORTS = ('main',)  # Replace with your actual module name

# Define the task schedule (run at midnight)
CELERYBEAT_SCHEDULE = {
    'daily-task': {
        'task': 'main.scheduled_delete_videos',
        'schedule': crontab(hour=0, minute=0),  # Midnight
        # 'schedule': crontab(minute='*'),
    },
}

