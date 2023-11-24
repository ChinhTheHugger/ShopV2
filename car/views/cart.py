from django.shortcuts import render , redirect

from django.contrib.auth.hashers import  check_password
from car.models.customer import Customer
from django.views import  View
from car.models.car import Car

class Cart(View):
    def get(self , request):
        ids = list(request.session.get('cart').keys())
        cars = Car.get_cars_by_id(ids)
        print(cars)
        return render(request , 'cart.html' , {'cars' : cars} )