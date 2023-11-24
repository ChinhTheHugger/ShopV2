from django.shortcuts import render, redirect
from car.models.car import Car
from car.models.category import Category
from car.models.brand import Brand

def homepage(request):
    carTop3 = Car.objects.raw("SELECT * FROM car ORDER BY RAND() LIMIT 3")
    carMostPopular = Car.objects.select_related('brand').all()[:10]
    brandMostPopular = Brand.objects.raw("SELECT * FROM brand LIMIT 10")
    carCategory = Category.objects.raw("SELECT * FROM category")
    context = {'cartopthree': carTop3,'carMostPopular': carMostPopular,'brandMostPopular': brandMostPopular,'carCategory': carCategory}
    return render(request,'homepage.html',context)