from django.shortcuts import render, redirect
from car_app.model.car import Car
from brand_app.model.brand import Brand

# Create your views here.

def get_brand(request,pk):
    brand = Brand.objects.filter(id=pk)
    car = Car.objects.select_related("brand").filter(brand=pk)
    context = {'brand': brand, 'car': car}
    return render(request,'brandinfo.html',context)