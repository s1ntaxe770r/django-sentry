from django import forms 


class ContactForm(forms.Form):
    """
    contact form 
    """
    message = forms.CharField(
        max_length=2000,
        widget=forms.Textarea(attrs={'class': 'form-control'}),
    )



