
from django.shortcuts import render


# Create your views here.
class Car:  # Note that parens are optional if not inheriting from another class
    def __init__(self, make, model, description, year):
        self.make = make
        self.model = model
        self.description = description
        self.year = year


cars = [
    Car('Ducati', 'MH900E', 'Designed as a loving homage to Mike Hailwood', 2001),
    Car('Mercedes', 'C215', 'marques handsome luxury coup', 2005),
    Car('Porche', '911', 'Fast car with lots of power', 2014),
    Car('Porche', '944', 'Designed as one of the best looking Car in the World', 1987),
    Car('Volvo', 'P1800ES', 'stunishing luxury car', 1973),
    Car('Audi', 'RS6 AVANT', 'Fast car with lots of power', 2004),
    Car('Toyota', 'CAMRY', 'Slick car', 2022),
    Car('Honda', 'CIVIC', 'Fast car', 2022),
    Car('Honda', 'ACCORD', 'Family car', 2021),
]

class Story:  # Note that parens are optional if not inheriting from another class
    def __init__(self,year, month, description):
        self.year = year
        self.month = month
        self.description = description
       

stories = [
   Story(2018,'October','Car Collector is founded.'),
   Story(2019,'June','First car is Collected: a Range Rover Classic '),
   Story(2020,'June','becoming the highest-grossing collector'),
   Story(2021,'March','Dedicated office opens in Los Angeles, CA.'),
   Story(2021,'August','First managed partner established in North America.'),
   Story(2022,'January','Team reached 60+ people around the world.'),
   Story(2022,'April','Achieved an online-only auction platform world record selling the McLaren P1 for'),
]

def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html', {'stories': stories})


def cars_index(request):
    return render(request, 'cars/index.html', {'cars': cars})
