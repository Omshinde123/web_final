from django.shortcuts import render

# Create your views here.
from http.client import HTTPResponse
from django.shortcuts import render


# Create your views here.
def blog(request):
    return render(request, 'blog/blog.html')



def contacts(request):
    return render(request, 'contacts/contacts.html')

def photos(request):
    return render(request, 'photos/photos.html')



def home(request):
    return render(request, 'home/index.html')





def aboutus(request):
    return render(request, 'aboutus/aboutus.html')
