from django.shortcuts import render, redirect
from django.contrib.auth.hashers import check_password
from car.models.customer import Customer
from django.views import View
from car.models.car import Car
from car.models.contract import Contract
from car.models.customer import Customer
from car.middleware.auth import auth_middleware
from django.db import connection

class ContractView(View):


    def get(self , request ):
        customer = request.session.get('customer')

        dict = {'customer': customer}
        contracts = Contract.objects.raw('''SELECT contract.*, car.model AS cmodel, car.year AS cyear, brand.name AS bname 
                                            FROM contract 
                                            INNER JOIN car 
                                            ON contract.car_id = car.id 
                                            INNER JOIN brand 
                                            ON car.brand_id = brand.id 
                                            WHERE contract.customer_id = %(customer)s 
                                            ORDER BY contract.end_date DESC''', dict)
        
        customerinfo = Customer.get_customer_by_id(customer)
        return render(request , 'account.html'  , {'contracts' : contracts,'customerinfo': customerinfo})