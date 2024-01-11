from datetime import datetime
from django.db import models  
from ckeditor.fields import RichTextField

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.FloatField(max_length=10)
    message = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Banner(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='uploads/')
    
      
    def __str__(self):
        return self.name
    
class About(models.Model):
    discription = models.CharField(max_length=500)
    
    def __str__(self):
        return self.discription
    
class Portfolio(models.Model):
    id = models.AutoField(primary_key=True)
    title= models.CharField(max_length=20,default=' ')
    image = models.ImageField(upload_to='uploads/')
    
    def __int__(self):
        return self.id

class Artical(models.Model):
    title = models.CharField(max_length=50,default=' ')
    img = models.ImageField(upload_to='artical/')
    Short_Discription = models.CharField(max_length=200,default=' ')
    Large_Discription = RichTextField()
    createdName = models.CharField(max_length=20,default='')
    createdAt = models.DateTimeField(default=datetime.now)
    
    def __str__(self):
        return self.title

class Comment(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.CharField(max_length=100)
    createdAt = models.DateTimeField(default=datetime.now)
    def __str__(self):
        return self.name

class WhatIDo(models.Model):
    image = models.ImageField(upload_to='uploads/')
    title= models.CharField(max_length=20,default=' ')
    discription = models.CharField(max_length=200,default=' ')
    def __str__(self):
        return self.title
    
    
    
        