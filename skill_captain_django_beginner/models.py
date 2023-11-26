from django.db import models

class Profile(models.Model):
    name = models.CharField(max_length=255)
    email= models.CharField(max_length=255)
    mobile_number = models.CharField(max_length=15, default='')
    address = models.CharField(max_length = 255, default='')

    
# Create your models here.
