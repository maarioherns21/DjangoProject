from django.shortcuts import render, redirect

from .forms import TunningForm
from .models import Car, Upgrade
from .models import Story

from django.views.generic.edit import CreateView, UpdateView, DeleteView
# Create your views here.
from django.views.generic import ListView, DetailView


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

    upgrades_car_doesnt_have = Car.objects.exclude(id__in = car.upgrades.all().values_list('id'))

    tunning_form = TunningForm()
    return render(request, 'cars/detail.html', {'car': car, 'tunning_form': tunning_form, 'upgrades': upgrades_car_doesnt_have})


def add_tunning(request, car_id):
    form = TunningForm(request.POST)

    if form.is_valid():

        new_tunning = form.save(commit=False)
        new_tunning.car_id = car_id
        new_tunning.save()
    return redirect('detail', car_id=car_id)


def assoc_upgrade(request, car_id, upgrade_id):
    # Note that you can pass a id instead of the whole object
    Car.objects.get(id=car_id).upgrades.add(upgrade_id)
    return redirect('detail', car_id=car_id)


class UpgradeList(ListView):
    model = Upgrade


class UpgradeDetail(DetailView):
    model = Upgrade


class UpgradeCreate(CreateView):
    model = Upgrade
    fields = '__all__'


class UpgradeUpdate(UpdateView):
    model = Upgrade
    fields = ['type', 'details']


class UpgradeDelete(DeleteView):
    model = Upgrade
    success_url = '/upgrades/'
