from django.shortcuts import render, redirect, HttpResponseRedirect
from car_app.model.car import Car
from category_app.model.category import Category
from django.views import View

def category(request,pk):
    category = Category.objects.all()
    car = Car.objects.select_related('brand').all()
    if pk != 0:
        car = car.filter(category=pk)
        
    context = {'category': category,'car': car}
    return render(request,'category.html', context)