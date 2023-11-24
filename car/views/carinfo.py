from django.shortcuts import render, redirect, HttpResponseRedirect
from car.models.car import Car
from car.models.category import Category
from django.views import View

# Create your views here.
class Index(View):

    def post(self , request):
        car = request.POST.get('car')
        remove = request.POST.get('remove')
        cart = request.session.get('cart')
        if cart:
            quantity = cart.get(car)
            if quantity:
                if remove:
                    if quantity<=1:
                        cart.pop(car)
                    else:
                        cart[car]  = quantity-1
                else:
                    cart[car]  = quantity+1

            else:
                cart[car] = 1
        else:
            cart = {}
            cart[car] = 1

        request.session['cart'] = cart
        print('cart' , request.session['cart'])
        return redirect('get-car')



    def get(self , request):
        # print()
        return HttpResponseRedirect(f'/carinfo/{request.get_full_path()[1:]}')

def get_car(request,pk):

    cart = request.session.get('cart')
    if not cart:
        request.session['cart'] = {}
    
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

    carinfo = Car.objects.select_related('brand').filter(id=pk)
    context = {'carinfo': carinfo}
    return render(request,'carinfo.html',context)