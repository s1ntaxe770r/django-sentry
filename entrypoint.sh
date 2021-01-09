#!/bin/bash
celery -A SentryApp worker > celery.log 2>&1 &

gunicorn -b 0.0.0.0:8000 -w 4 SentryApp.wsgi