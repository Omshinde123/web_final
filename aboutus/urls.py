from django.urls import path

from home.views import aboutus
from . import views

urlpatterns = [
   path('',views.aboutus,name='aboutus'),
   path("home/",views.home,name='home'),
   path("contacts/",views.contacts,name='contacts'),
   path("blog/",views.blog,name='blog'),
   path("photos/",views.photos,name='photos'),

]
 

