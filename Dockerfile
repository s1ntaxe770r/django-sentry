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

RUN python manage.py makemigrations && python manage.py migrate --noinput

ADD entrypoint.sh .

RUN chmod +x entrypoint.sh

CMD [ "./entrypoint.sh" ]