from django.shortcuts import render, redirect

from django.contrib.auth.hashers import check_password
from main_app.models.customer import Customer
from django.views import View

from car_app.model.car import Car
from contract_app.model.contract import Contract

from contract_app.form.contract import ContractForm

import datetime

import json

def create_contract(request):
        carid = request.POST.get('car')
        car = Car.objects.select_related('brand').filter(id=carid)
        customer = Customer.objects.filter(id=request.session.get('customer'))
        context = {'car': car,'customer': customer}
        return render (request, 'contract.html', context)

# class Contract (View):
#     def create_contract(self, request):
#         carid = request.POST.get('car')
#         car = Car.objects.select_related('brand').filter(id=carid)
#         customer = Customer.objects.filter(id=request.session.get('customer'))
#         context = {'car': car,'customer': customer}
#         return render (request, 'contract.html', context)

#     def post(self, request):
#         postData = request.POST
#         car_in = postData.get('car')
#         customer_in = request.session.get('customer')
#         quantity_in = postData.get('quantity')
#         carprice = Car.objects.get(id=car_in)
#         price = (Car.objects.get(id=car_in)).price
#         date_in = datetime.date.today()
#         end_date_in = postData.get('enddate')

#         value = {
#             'car': car_in,
#             'quantity': quantity_in,
#             'date': date_in,
#             'end_date': end_date_in
#         }
#         error_message = None

#         contract = Contract (car=car_in,
#                              customer=customer_in,
#                              quantity=quantity_in,
#                              price=price,
#                              date=date_in,
#                              end_date=end_date_in)
        
#         error_message = self.validateContract(contract)

#         if not error_message:
#             contract.price = contract.price * (contract.end_date - contract.date).days
#             contract.create()
#             return redirect ('account')
#         else:
#             data = {
#                 'error': error_message,
#                 'values': value
#             }
#             return render (request, 'contract.html', data)
        
#     def validateContract(self, contract):
#         error_message = None
#         if contract.quantity > (Car.objects.get(id=contract.car)).instock or contract.quantity < 1:
#             error_message = 'Quantity must be less or equal the number of cars in stock'
#         elif contract.end_date <= contract.date:
#             error_message = 'End date cannot be earlier than start date'
#         # saving

#         return error_message