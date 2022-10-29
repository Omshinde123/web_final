from django.urls import path
from . import views

urlpatterns = [
   path('',views.contacts,name='contacts'),
   path("blog/",views.blog,name='blog'),
   path('aboutus/',views.aboutus,name='aboutus'),
   path("home/",views.home,name='home'),
   path("photos/",views.photos,name='photos'),

]
 
  