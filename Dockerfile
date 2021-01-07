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

# Run migrations 
RUN python Project/manage.py makemigrations && python Project/manage.py migrate --noinput

EXPOSE 8000

