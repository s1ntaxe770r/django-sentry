from django import forms 


class ContactForm(forms.Form):
    """
    contact form 
    """
    subject = forms.CharField(max_length=40)
    message  = forms.CharField(max_length=200)
    