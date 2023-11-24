from django.shortcuts import render, redirect
from car.models.brand import Brand

# Create your views here.

def get_brand(request,pk):
    brand = Brand.objects.filter(id=pk)
    context = {'brand': brand}
    return render(request,'brandinfo.html',context)