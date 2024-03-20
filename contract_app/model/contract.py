from django.db import models
from django.forms import fields
import datetime
from datetime import date

class Contract(models.Model):
    car = models.IntegerField(default=0)
    customer = models.IntegerField(default=0)
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
    
    def __str__(self):
        return self.customer.first_name +" "+ self.customer.last_name +", from "+ str(self.date) +" to "+ str(self.end_date)
    
    class Meta:
        db_table = 'contract'