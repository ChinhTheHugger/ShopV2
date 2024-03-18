from django.shortcuts import render, redirect

from django.contrib.auth.hashers import check_password
from car.models.customer import Customer
from django.views import View

from car.models.car import Car
from car.models.contract import Contract

from car.forms.contract import ContractForm

import datetime

import json

class ContractSave(View):
    def post(self, request):
        postData = request.POST
        car_in = postData.get('car')
        customer_in = request.session.get('customer')
        quantity_in = postData.get('quantity')
        price = (Car.objects.get(id=car_in)).price
        date_in = datetime.datetime.now()
        end_date_in = postData.get('enddate')

        value = {
            'car': car_in,
            'quantity': quantity_in,
            'date': date_in,
            'end_date': end_date_in
        }
        error_message = None

        contract = Contract(car=Car.objects.get(id=car_in),customer=Customer.objects.get(id=customer_in),quantity=quantity_in,price=price,date=date_in,end_date=end_date_in)

        if int((datetime.datetime.strptime(end_date_in, '%Y-%m-%d')-date_in).days) < 1:
            contract.price = (Car.objects.get(id=car_in)).price * 1 * int(contract.quantity)
        else:
            contract.price = (Car.objects.get(id=car_in)).price * (int((datetime.datetime.strptime(end_date_in, '%Y-%m-%d')-date_in).days)+1) * int(contract.quantity)
        print(contract.price)

        contract.placeOrder()
        
        return redirect ('account')
    