from django.db import models

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
    
    
        