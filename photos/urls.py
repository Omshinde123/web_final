from django.urls import path
from . import views

urlpatterns = [
   path("",views.photos,name='photos'),
   path('blog/',views.blog,name='blog'),
   path('aboutus/',views.aboutus,name='aboutus'),
   path("home/",views.home,name='home'),
   path("contacts/",views.contacts,name='contacts'),
]
