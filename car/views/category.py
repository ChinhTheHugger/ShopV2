from django.shortcuts import render, redirect, HttpResponseRedirect
from car.models.car import Car
from car.models.category import Category
from django.views import View

def category(request):
    ctgr = request.POST.get('ctgr')
    category = Category.objects.all()
    if ctgr:
        car = Car.objects.select_related('brand').filter(category=ctgr)
    else:
        car = Car.objects.select_related('brand').all()
    context = {'category': category,'car': car}
    return render(request,'category.html', context)