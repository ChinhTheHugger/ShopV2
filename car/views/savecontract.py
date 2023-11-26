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

        # print(date_in)
        # print(end_date_in)
        # print(datetime.datetime.strptime(end_date_in, '%Y-%m-%d'))
        # print(datetime.datetime.strptime(date_in, '%Y-%m-%d'))
        # print(datetime.datetime.strptime(end_date_in, '%Y-%m-%d')-date_in)
        value = {
            'car': car_in,
            'quantity': quantity_in,
            'date': date_in,
            'end_date': end_date_in
        }
        error_message = None

        # contract = Contract()
        contract = Contract(car=Car.objects.get(id=car_in),customer=Customer.objects.get(id=customer_in),quantity=quantity_in,price=price,date=date_in,end_date=end_date_in)

        # startdate = int(date_in.strftime("%Y%m%d%H%M%S"))
        # enddate = int(end_date_in.strftime("%Y%m%d%H%M%S"))
        # contract.price = int(contract.price) * int((datetime.datetime.strptime(contract.end_date, "%Y%m%d").date() - contract.date).days)
        if int((datetime.datetime.strptime(end_date_in, '%Y-%m-%d')-date_in).days) < 1:
            contract.price = (Car.objects.get(id=car_in)).price * 1 * int(contract.quantity)
        else:
            contract.price = (Car.objects.get(id=car_in)).price * (int((datetime.datetime.strptime(end_date_in, '%Y-%m-%d')-date_in).days)+1) * int(contract.quantity)
        print(contract.price)

        contract.placeOrder()

        # contract = Contract("1","1","12","100",datetime.date.today(),datetime.date.today())

        # contract.price = contract.price * (contract.end_date - contract.date).days
        # contract.placeOrder ()
        
        return redirect ('account')
        
        # error_message = self.validateContract(contract)

        # if not error_message:
        #     contract.price = contract.price * (contract.end_date - contract.date).days
        #     contract.create()
        #     return redirect ('account')
        # else:
        #     data = {
        #         'error': error_message,
        #         'values': value
        #     }
        #     return render (request, 'contract.html', data)
        
    # def validateContract(self,contract):
    #     error_message = None
    #     if contract.quantity > (Car.objects.get(id=contract.car)).instock or contract.quantity < 1:
    #         error_message = 'Quantity must be less or equal the number of cars in stock'
    #     elif contract.end_date <= contract.date:
    #         error_message = 'End date cannot be earlier than start date'
    #     # saving

    #     return error_message