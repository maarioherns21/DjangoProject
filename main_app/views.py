
from django.shortcuts import render

from .models import Car

from .models import Story

# Create your views here.

def home(request):
    return render(request, 'home.html')


def about(request):
    stories = Story.objects.all()
    return render(request, 'about.html', {'stories': stories})


def cars_index(request):
    cars = Car.objects.all()
    return render(request, 'cars/index.html', {'cars': cars})

def cars_details(request, car_id): # path 'cars/<int:cat_id>/' < this is where car_id comes from 
    car = Car.objects.get(id=car_id)
    return render(request, 'cars/detail.html' , {'car': car})
