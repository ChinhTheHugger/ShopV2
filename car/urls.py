from django.contrib import admin
from django.urls import path
from .views.home import homepage
from .views.signup import Signup
from .views.login import Login , logout
from .views.cart import Cart
from .views.rent import create_contract
from .views.savecontract import ContractSave
from .views.contract import ContractView
from .views.carinfo import get_car
from .views.brandinfo import get_brand
from .views.search import search
from .views.category import category
from .middleware.auth import  auth_middleware


urlpatterns = [
    path('', homepage, name='homepage'),

    path('homepage', homepage, name='homepage'),

    path('signup', Signup.as_view(), name='signup'),

    path('login', Login.as_view(), name='login'),
    
    path('logout', logout , name='logout'),


    path('search', search , name='search'),
    
    path('category/<int:pk>', category , name='category'),

    path('carinfo/<int:pk>', get_car, name='get-car'),

    path('brandinfo/<int:pk>', get_brand, name='get-brand'),

    path('rentcar', auth_middleware(create_contract), name='rent-car'),

    path('processcontract', auth_middleware(ContractSave.as_view()), name='process-contract'),

    path('account', auth_middleware(ContractView.as_view()), name='account'),
]