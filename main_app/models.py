from django.db import models

# Create your models here.

class Car(models.Model):
    make = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    year = models.IntegerField()



class Story(models.Model):
    year = models.IntegerField()
    month = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    
