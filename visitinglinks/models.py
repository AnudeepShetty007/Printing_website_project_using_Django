from django.db import models
from .validators import validate_file_size
# Create your models here.

class One_side(models.Model):
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