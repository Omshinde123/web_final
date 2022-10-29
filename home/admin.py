from operator import mod
from django.contrib import admin

# Register your models here.
from . import models

admin.site.register(models.Photos)
admin.site.register(models.Aboutus)
admin.site.register(models.Contacts)
admin.site.register(models.Blogs)
