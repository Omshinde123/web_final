# from email.message import Message
from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from contacts.forms import contactformemail
from django.core.mail import send_mail
# Create your views here.
from http.client import HTTPResponse
from django.shortcuts import render

# from contacts.models import Contacts
# from .forms import Contactsform

# Create your views here.
def contacts(request):

    if request.method == 'GET':
        form = contactformemail()
    else:
        form = contactformemail(request.POST)
        if form.is_valid():
             Name = form.cleaned_data['Name']
             Email = form.cleaned_data['Email']
             Message = form.cleaned_data['Message']
        send_mail(Name,Message,Email,['omshinde190@gmail.com',Email])
        # Name = form.cleaned_data['Name']
        # Email = request.POST['Email']
        # Message = request.POST['Message']

        # send_mail('contacts form',
        # Name,
        # Email,
        # Message,
        # settings.EMAIL_HOST_USER,
        # ['om.shinde9177@gmail.com'],
        # fail_silently=False

        
        


         

    return render(request, 'contacts/contacts.html',{'form':form}
    )

def photos(request):
    return render(request, 'photos/photos.html')

def home(request):
    return render(request, 'home/index.html')

def blog(request):
    return render(request, 'blog/blog.html')

def aboutus(request):
    return render(request, 'aboutus/aboutus.html')



