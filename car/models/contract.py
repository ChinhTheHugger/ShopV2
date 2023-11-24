from django.db import models
from .car import Car
from .customer import Customer
import datetime

class Contract(models.Model):
    car = models.ForeignKey(Car,
                                on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer,
                                 on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    price = models.IntegerField()
    phone = models.CharField (max_length=50, default='', blank=True)
    date = models.DateField (default=datetime.datetime.today)
    status = models.BooleanField (default=False)

    def placeOrder(self):
        self.save()

    @staticmethod
    def get_contracts_by_customer(customer_id):
        return Contract.objects.filter(customer=customer_id).order_by('-date')
    
    class Meta:
        db_table = 'contract'