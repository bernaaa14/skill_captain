from django.db import models

class Profile(models.Model):
    name = models.CharField(max_length=255)
    age = models.IntegerField()
    occupation = models.CharField(max_length=255)
    email= models.CharField(max_length=255)

    
# Create your models here.
