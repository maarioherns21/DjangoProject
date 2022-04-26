from django.db import models

from django.urls import reverse
# Create your models here.


class Car(models.Model):
    make = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    year = models.IntegerField()

    def get_absolute_url(self):
        return reverse('detail', kwargs={'car_id': self.id})


class Story(models.Model):
    year = models.IntegerField()
    month = models.CharField(max_length=100)
    description = models.CharField(max_length=250)


    
