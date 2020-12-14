from django.http.response import HttpResponse
from django.shortcuts import render
from .tasks import email_me

# Create your views here.


def index(request):
    return render(request, "index.html")

def mail(request):
    email_me.delay()
    return HttpResponse("Email sent have a nice day :)")
