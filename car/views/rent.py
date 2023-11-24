from django.shortcuts import render, redirect

from django.contrib.auth.hashers import check_password
from car.models.customer import Customer
from django.views import View

from car.models.car import Car
from car.models.contract import Contract


class Contract(View):
    def post(self, request):
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        customer = request.session.get('customer')
        cart = request.session.get('cart')
        cars = Car.get_cars_by_id(list(cart.keys()))
        print(address, phone, customer, cart, cars)

        for car in cars:
            print(cart.get(str(car.id)))
            contract = Contract(customer=Customer(id=customer),
                          car=car,
                          price=car.price,
                          address=address,
                          phone=phone,
                          quantity=cart.get(str(car.id)))
            contract.save()
        request.session['cart'] = {}

        return redirect('cart')