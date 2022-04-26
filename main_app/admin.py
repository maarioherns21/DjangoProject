from django.contrib import admin

# Register your models here.
from django.contrib import admin
# import your models here
from .models import Car, Story, Tunning


# Register your models here
admin.site.register(Car)
admin.site.register(Story)
admin.site.register(Tunning)