from django.contrib import admin
from django.urls import path
from .views.home import homepage
from .views.signup import Signup
from .views.login import Login , logout
from .views.rent import create_contract
from contract_app.view.savecontract import ContractSave
from .views.customeraccount import AccountInfo
from car_app.view.carinfo import get_car
from brand_app.view.brandinfo import get_brand
from .views.search import search
from category_app.view.category import category
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

    path('account', auth_middleware(AccountInfo.as_view()), name='account'),
]