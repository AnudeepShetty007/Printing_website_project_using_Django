from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Post(models.Model):
    title=models.CharField(max_length=100)
    content= models.TextField()
    date_posted=models.DateTimeField(default = timezone.now)
    author =models.ForeignKey(User, on_delete=models.CASCADE)

    def  __str__(self):
        return self.title

class contactus(models.Model):
    
    name = models.CharField(max_length=100, blank=True,help_text=u"Please enter your name...") 
    mobile=models.CharField(max_length=10,blank=True)
    Email=models.CharField(max_length=100, blank=True)
    Issue=models.CharField(max_length=100,blank=True)
    Query=models.TextField(max_length=500,blank=True)

    def __str__(self):
        return self.name

from django.db import models

# Create your models here.

class Banners(models.Model):
    order_id= models.CharField(max_length=120, blank= True)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    subject = models.CharField(max_length=100)
    message = models.CharField(max_length=100)
    image = models.CharField(max_length=50)
    quantity = models.DecimalField(max_digits=10, decimal_places=0)
    size1 = models.DecimalField(max_digits=10, decimal_places=0)
    size2 = models.DecimalField(max_digits=10, decimal_places=0)
   
    def __str__(self):
        return self.order_id