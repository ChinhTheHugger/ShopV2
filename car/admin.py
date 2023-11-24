from django.contrib import admin
from .models.car import Car
from .models.category import Category
from .models.customer import Customer
from .models.contract import Contract
from .models.brand import Brand


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