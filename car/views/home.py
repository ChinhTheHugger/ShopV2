from django.shortcuts import render, redirect
from car.models.car import Car
from car.models.category import Category
from car.models.brand import Brand

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework import status
from rest_framework import permissions

from car.serializers.car import CarSerializer
from car.serializers.brand import BrandSerializer
from car.serializers.category import CategorySerializer

def homepage(request):

    # cart = request.session.get('cart')
    # if not cart:
    #     request.session['cart'] = {}
        
    # carTop3 = Car.objects.raw("SELECT * FROM car ORDER BY RAND() LIMIT 3")
    # carMostPopular = Car.objects.select_related('brand').all()[:10]
    # brandMostPopular = Brand.objects.raw("SELECT * FROM brand ORDER BY RAND() LIMIT 10")
    # carCategory = Category.objects.raw("SELECT * FROM category ORDER BY RAND()")
    # context = {'cartopthree': carTop3,'carMostPopular': carMostPopular,'brandMostPopular': brandMostPopular,'carCategory': carCategory}
    # return render(request,'homepage.html',context)
    
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'list.html'
    
    carTop3_r = Car.objects.raw("SELECT * FROM car ORDER BY RAND() LIMIT 3")
    carTop3 = CarSerializer(carTop3_r, many=True, )
    
    carMostPopular_r = Car.objects.select_related('brand').all()[:10]
    carMostPopular = CarSerializer(carMostPopular_r, many=True, context={'request': request})
    
    brandMostPopular_r = Brand.objects.raw("SELECT * FROM brand ORDER BY RAND() LIMIT 10")
    brandMostPopular = BrandSerializer(brandMostPopular_r, many=True, context={'request': request})
    
    carCategory_r = Category.objects.raw("SELECT * FROM category ORDER BY RAND()")
    carCategory = CategorySerializer(carCategory_r, many=True, context={'request': request})
    
    context = {'cartopthree': carTop3.data[:],'carMostPopular': carMostPopular.data[:],'brandMostPopular': brandMostPopular.data[:],'carCategory': carCategory.data[:]}
    
    return render(request,'homepage.html',context)