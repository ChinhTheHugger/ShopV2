from django.shortcuts import render, redirect
from car_app.model.car import Car
from category_app.model.category import Category
from brand_app.model.brand import Brand

def homepage(request):

    cart = request.session.get('cart')
    if not cart:
        request.session['cart'] = {}
        
    carTop3 = Car.objects.raw("SELECT * FROM car ORDER BY RAND() LIMIT 3")
    carMostPopular = Car.objects.select_related('brand').all()[:10]
    brandMostPopular = Brand.objects.raw("SELECT * FROM brand ORDER BY RAND() LIMIT 10")
    carCategory = Category.objects.raw("SELECT * FROM category ORDER BY RAND()")
    context = {'cartopthree': carTop3,'carMostPopular': carMostPopular,'brandMostPopular': brandMostPopular,'carCategory': carCategory}
    return render(request,'homepage.html',context)