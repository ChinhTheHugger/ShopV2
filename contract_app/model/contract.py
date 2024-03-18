from django.db import models
from django.forms import fields
from ...car_app.model.car import Car
from ...brand_app.model.brand import Brand
from ...main_app.models.customer import Customer
import datetime
from datetime import date

class Contract(models.Model):
    car = models.ForeignKey(Car,
                                on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer,
                                 on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    price = models.PositiveBigIntegerField()
    date = models.DateField (default=datetime.datetime.today)
    end_date = models.DateField(default=datetime.datetime.today)

    
    def placeOrder(self):
        self.save()

    @staticmethod
    def get_contracts_by_customer(customer_id):
        return Contract.objects.filter(customer=customer_id)
    
    @property
    def is_past_due(self):
        return date.today() <= self.end_date
    
    @property
    def car_name(self):
        car = Car.objects.get(id=self.car)
        brand = Brand.objects.get(id=car.brand)
        return brand.name +" "+ car.model +" "+ str(car.year)
    
    def __str__(self):
        return self.customer.first_name +" "+ self.customer.last_name +", from "+ str(self.date) +" to "+ str(self.end_date)
    
    class Meta:
        db_table = 'contract'