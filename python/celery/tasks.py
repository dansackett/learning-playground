import requests
import json
import celeryconfig
from celery import Celery
from celery.task.base import periodic_task
from datetime import timedelta

app = Celery()
app.config_from_object(celeryconfig)

@app.task
#@periodic_task(run_every=timedelta(seconds=5))
def count(username):
    response = requests.get('https://api.github.com/users/{0}/repos'.format(username))
    print len(json.loads(response.content))
