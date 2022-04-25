from django.contrib import admin

# Register your models here.
from django.contrib import admin
# import your models here
from .models import Car
from .models import Story

# Register your models here
admin.site.register(Car)
admin.site.register(Story)