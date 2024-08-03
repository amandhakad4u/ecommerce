from django.contrib import admin

from django.urls import path
from home import views




urlpatterns = [
path("home",views.home, name='home'),  



path("shop-men",views.shopmen, name='shop-men'), 
path("shop-women",views.shopwomen, name='shop-women'), 
path("shop-clearance",views.shopclearance, name='shop-clearance'), 






path("cart",views.cart, name='cart'), 






path("account",views.account, name='account'), 

path("login",views.login, name='login'),  
path("signup",views.signup, name='signup'), 
path("forgotpassword",views.forgotpassword, name='forgotpassword'), 




path("order",views.order, name='order'), 




]


