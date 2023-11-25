from django.shortcuts import render, redirect
from car.models.brand import Brand
from car.models.car import Car

# Create your views here.

def get_brand(request,pk):
    brand = Brand.objects.filter(id=pk)
    car = Car.objects.select_related("brand").filter(brand=pk)
    context = {'brand': brand, 'car': car}
    return render(request,'brandinfo.html',context)