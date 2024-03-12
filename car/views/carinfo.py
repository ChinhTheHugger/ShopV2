from django.shortcuts import render, redirect, HttpResponseRedirect
from car.models.car import Car
from car.models.category import Category
from django.views import View

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework import status
from rest_framework import permissions
from sqlalchemy import func

from car.serializers.car import CarSerializer
from car.serializers.brand import BrandSerializer
from car.serializers.category import CategorySerializer

# Create your views here.
# class Index(View):

#     def post(self , request):
#         car = request.POST.get('car')
#         remove = request.POST.get('remove')
#         cart = request.session.get('cart')
#         if cart:
#             quantity = cart.get(car)
#             if quantity:
#                 if remove:
#                     if quantity<=1:
#                         cart.pop(car)
#                     else:
#                         cart[car]  = quantity-1
#                 else:
#                     cart[car]  = quantity+1

#             else:
#                 cart[car] = 1
#         else:
#             cart = {}
#             cart[car] = 1

#         request.session['cart'] = cart
#         print('cart' , request.session['cart'])
#         return redirect('get-car-index')



#     def get(self , request):
#         # print()
#         return HttpResponseRedirect(f'/carinfo/{request.get_full_path()[1:]}')

def get_car(request,pk):

    # cart = request.session.get('cart')
    # if not cart:
    #     request.session['cart'] = {}
    
    # cars = None
    # categories = Category.get_all_categories()
    # categoryID = request.GET.get('category')
    # if categoryID:
    #     cars = Car.get_all_cars_by_categoryid(categoryID)
    # else:
    #     cars = Car.get_all_cars()

    # data = {}
    # data['cars'] = cars
    # data['categories'] = categories

    carinfo_r = Car.objects.select_related().filter(id=pk)
    for c in carinfo:
        carbrand_r = Car.objects.select_related('brand').filter(brand=c.brand).order_by(func.random())[:10]
        carcategory_r = Car.objects.select_related('brand').filter(category=c.category).order_by(func.random())[:10]
    
    carinfo = CarSerializer(carinfo_r, many=True)
    carbrand = BrandSerializer(carbrand_r, many=True)
    carcategory = CategorySerializer(carcategory_r, many=True)
    
    context = {'carinfo': carinfo,'carbrand': carbrand,'carcategory': carcategory}
    return render(request,'carinfo.html',context)