from django.http.response import HttpResponse
from django.shortcuts import render
import requests
from .tasks import email_me
from .forms import ContactForm
# Create your views here.


def mail(request):
    if request.Method == 'POST':
        form = ContactForm
        if form.is_valid:
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            email_me.delay(message)

  
    return HttpResponse("Email sent have a nice day :)")
