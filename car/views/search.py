from django.shortcuts import render, redirect, HttpResponseRedirect
from car.models.car import Car
from car.models.brand import Brand
from car.models.category import Category
from django.views import View

def search(request):
    model_in = request.POST.get('model')
    brand_in = request.POST.get('brand')
    category_in = request.POST.get('category')
    year_in = request.POST.get('year')

    carsearch = Car.objects.select_related('brand').all()
    brand_opt = Brand.objects.all()
    category_opt = Category.objects.all()
    if model_in != "All":
        carsearch = carsearch.filter(model=model_in)
    if brand_in != "0":
        carsearch = carsearch.filter(brand=brand_in)
    if category_in != "0":
        carsearch = carsearch.filter(category=category_in)
    if year_in != "All":
        carsearch = carsearch.filter(year=year_in)

    context = {'carsearch': carsearch,'brand_opt': brand_opt,'category_opt': category_opt}
    return render(request,'search.html',context)