from celery import Celery , shared_task
from django.core.mail import send_mail
from dotenv import load_dotenv
import requests
import os

envfile = os.getenv("ENVPATH")
load_dotenv(envfile)


from_email  = os.getenv("EMAIL_HOST_USER")

@shared_task
def email_me(subject,message):
    send_mail(
        subject,
        message,
        from_email,
        ['petejo7398@hmnmw.com'],
        fail_silently=False,)
    return None

