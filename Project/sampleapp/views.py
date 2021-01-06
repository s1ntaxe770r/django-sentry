from django.http.response import HttpResponse
from django.shortcuts import render
import requests
from .tasks import email_me
from .forms import ContactForm
# Create your views here.


def mail(request):
    if request.method == 'POST':
        form = ContactForm
        if form.is_valid:
            subject = "Someone has something to say"
            message = form.cleaned_data['message']
            email_me.delay(message,subject)
            return HttpResponse("Email sent have a nice day :)")
    else:
        form = ContactForm
    return render(request,'index.html',{'form':form})


        
    