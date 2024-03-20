from django.contrib import admin
from car_app.model.car import Car
from category_app.model.category import Category
from .models.customer import Customer
from contract_app.model.contract import Contract
from brand_app.model.brand import Brand


class AdminCar(admin.ModelAdmin):
    list_display = ['name', 'price', 'category']


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['__str__']

class CustomerAdmin(admin.ModelAdmin):
    list_display = ['__str__']

# Register your models here.
admin.site.register(Car,AdminCar)
admin.site.register(Category)
admin.site.register(Customer)
admin.site.register(Contract)
admin.site.register(Brand)