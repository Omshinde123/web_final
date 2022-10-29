
from email.message import Message
from django import forms

class contactformemail(forms.Form):
        Name=forms.CharField(required=True)
        Email=forms.EmailField(required=True)
        Message=forms.CharField(required=True)


