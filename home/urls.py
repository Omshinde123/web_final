from django.urls import path
from . import views

urlpatterns = [
   path("",views.home,name='home'),
    path("blog/",views.blog,name='blog'),
   path("photos/",views.photos,name='photos'),
   path("aboutus/",views.aboutus,name='aboutus'),
   path("contacts/",views.contacts,name='contacts'),
]
 
