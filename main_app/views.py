
from dataclasses import fields
from pyexpat import model
from django.shortcuts import redirect, render
from .forms import TunningForm

from .models import Car

from .models import Story

from django.views.generic.edit import CreateView, UpdateView, DeleteView
# Create your views here.


class CarCreate(CreateView):
    model = Car
    fields = '__all__'


class CarUpdate(UpdateView):
    model = Car
    fields = ['model', 'year', 'description']


class CarDelete(DeleteView):
    model = Car
    success_url = '/cars/'


def home(request):
    return render(request, 'home.html')


def about(request):
    stories = Story.objects.all()
    return render(request, 'about.html', {'stories': stories})


def cars_index(request):
    cars = Car.objects.all()
    return render(request, 'cars/index.html', {'cars': cars})


# path 'cars/<int:cat_id>/' < this is where car_id comes from
def cars_details(request, car_id):
    car = Car.objects.get(id=car_id)

    tunning_form = TunningForm()
    return render(request, 'cars/detail.html', {'car': car, 'tunning_form': tunning_form})


def add_tunning(request, car_id):
    form = TunningForm(request.POST)

    if form.is_valid():

        new_tunning = form.save(commit=False)
        new_tunning.car_id = car_id
        new_tunning.save()
    return redirect('detail', car_id=car_id)
