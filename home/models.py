import email
from email.message import Message
from operator import mod
from os import name
from pickle import TRUE
from pydoc import describe
from statistics import mode
from tabnanny import verbose
from turtle import update
from venv import create
from django.db import models

from aboutus.views import contacts

# Create your models here.

class Photos(models.Model):
    name = models.CharField(max_length=100,null=True,blank=True)
    description = models.CharField(max_length=100,null=True)
    update_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural= "Photos"


class Blogs(models.Model):
    name = models.CharField(max_length=100,null=True) 
    description = models.CharField(max_length=100,null=True)
    update_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural= "Blogs"    


class Contacts(models.Model):
    Name = models.CharField(max_length=100)
    Email = models.EmailField(max_length=50)
    Message = models.CharField(max_length=100,null=True,blank=True)
    update_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.Name

    class Meta:
        verbose_name_plural= "Contacts"


class Aboutus(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100,null=True)
    update_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural= "About us"



