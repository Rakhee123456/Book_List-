from django.db import models
from rest_framework import serializers, status
from rest_framework.views import APIView
from django.contrib.auth.models import User

# Create your models here.
class Author (models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name
    
class Book (models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    release_date = models.DateField()
    pages = models.IntegerField()
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.title