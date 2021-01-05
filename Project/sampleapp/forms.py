from django import forms 


class ContactForm(forms.Form):
    """
    contact form 
    """
    message  = forms.CharField(max_length=200)
    