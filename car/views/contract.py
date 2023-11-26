from django.shortcuts import render, redirect
from django.contrib.auth.hashers import check_password
from car.models.customer import Customer
from django.views import View
from car.models.car import Car
from car.models.contract import Contract
from car.models.customer import Customer
from car.middleware.auth import auth_middleware

class ContractView(View):


    def get(self , request ):
        customer = request.session.get('customer')
        contracts = Contract.get_contracts_by_customer(customer_id=customer)
        contracts = contracts.select_related('car').order_by('-end_date')
        customerinfo = Customer.get_customer_by_id(customer)
        return render(request , 'account.html'  , {'contracts' : contracts,'customerinfo': customerinfo})