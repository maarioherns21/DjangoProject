# Register your models here.
from django.contrib import admin
# import your models here
from .models import Car, Story, Tunning, Upgrade


# Register your models here
admin.site.register(Car)
admin.site.register(Story)
admin.site.register(Tunning)
admin.site.register(Upgrade)