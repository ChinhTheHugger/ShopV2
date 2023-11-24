from django.contrib import admin
from django.urls import path
from .views.home import homepage
from .views.signup import Signup
from .views.login import Login , logout
from .views.cart import Cart
from .views.rent import Contract
from .views.contract import ContractView
from .views.carinfo import get_car, Index
from .views.brandinfo import get_brand
from .middleware.auth import  auth_middleware


urlpatterns = [
    path('', homepage, name='homepage'),
    path('homepage', homepage, name='homepage'),

    path('signup', Signup.as_view(), name='signup'),
    path('login', Login.as_view(), name='login'),
    path('logout', logout , name='logout'),

    # path('carinfo-index/<int:pk>', Index.as_view(), name='get-car-index'),
    path('carinfo', Index.as_view(), name='get-car-index'),
    path('carinfo/<int:pk>', get_car, name='get-car'),

    path('brandinfo/<int:pk>', get_brand, name='get-brand'),

    path('cart', auth_middleware(Cart.as_view()) , name='cart'),
    path('check-out', Contract.as_view() , name='checkout'),
    path('orders', auth_middleware(ContractView.as_view()), name='orders'),
]