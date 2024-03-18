from django.shortcuts import render, redirect, HttpResponseRedirect
from car_app.model.car import Car
from category_app.model.category import Category
from django.views import View

def get_car(request,pk):
    carinfo = Car.objects.select_related('brand').filter(id=pk)
    for c in carinfo:
        carbrand = Car.objects.select_related('brand').filter(brand=c.brand)[:10]
        carcategory = Car.objects.select_related('brand').filter(category=c.category)[:10]
    context = {'carinfo': carinfo,'carbrand': carbrand,'carcategory': carcategory}
    return render(request,'carinfo.html',context)