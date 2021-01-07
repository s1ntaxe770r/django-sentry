FROM python:3.9.1-slim

WORKDIR /app 

COPY requirements.txt . 
COPY .env . 

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV ENVPATH=/app/.env

# install dependencies 
RUN pip install --no-cache-dir  -r  /app/requirements.txt

COPY . .

EXPOSE 8000

WORKDIR /app/Project

RUN celery -A SentryApp worker&

RUN python manage.py makemigrations && python manage.py migrate --noinput

CMD ["gunicorn", "-b 0.0.0.0:8000", "-w 4", "SentryApp.wsgi"]

