from datetime import timedelta

# Broker settings.
BROKER_URL = 'redis://localhost:6379/0'

# List of modules to import when celery starts.
CELERY_IMPORTS = ('tasks',)

# Using the database to store task state and results.
CELERY_RESULT_BACKEND = 'redis://localhost:6379/1'

# Set Serializers
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'

# Schedule Tasks
CELERYBEAT_SCHEDULE = {
    'every-5-seconds': {
        'task': 'tasks.count_website',
        'schedule': timedelta(seconds=5),
        'args': ('http://google.com',)
    },
}

# Set timezone to UTC
CELERY_TIMEZONE = 'UTC'
