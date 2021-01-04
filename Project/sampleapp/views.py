from django.http.response import HttpResponse
from django.shortcuts import render
import requests
from .tasks import email_me

# Create your views here.


def index(request):
    return render(request, "index.html")

def mail(request):
    raise requests.exceptions.HTTPError
    email_me.delay()
    return HttpResponse("Email sent have a nice day :)")
