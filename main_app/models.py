from django.db import models

from django.urls import reverse
# Create your models here.


class Upgrade(models.Model):
    type = models.CharField(max_length=50)
    details = models.CharField(max_length=250)

    def __str__(self):
        return self.type

    def get_absolute_url(self):
        return reverse('upgrades_detail', kwargs={'pk': self.id})


class Car(models.Model):
    make = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    year = models.IntegerField()
    upgrades = models.ManyToManyField(Upgrade)

    def __str__(self):
        return f"The car named {self.make} has id of {self.id}"

    def get_absolute_url(self):
        return reverse('detail', kwargs={'car_id': self.id})


SERVICES = (
    ('A', 'OIL & FILTER'),
    ('B', 'ROTATE TIRES'),
    ('C', 'TRANSMISSION FLUID'),
    ('D', 'AIR FILTER'),
    ('E', 'TIRE PRESSURE AND TREAD DEPTH'),
    ('F', 'BRAKE, AND PARKING LIGHTS'),
    ('G', 'SPARK PLUGS'),
    ('H', 'COOLANT FLUID EXCHANGE'),
    ('I', 'BATTERY SERVICE')

)


class Tunning(models.Model):
    date = models.DateField('Tunning date')
    service = models.CharField(
        max_length=1,
        choices=SERVICES,
        default=SERVICES[0][0]

    )

    car = models.ForeignKey(Car, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.get_service_display()} on {self.date}"

    class Meta:
        ordering = ['-date']


class Story(models.Model):
    year = models.IntegerField()
    month = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
