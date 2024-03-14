from django.contrib import admin
from django.urls import path
from tourguideapp import views

urlpatterns = [

    path('', views.home, name='Home'),
    path('my web' , views.myweb,name='myweb'),
    path('Tables/',views.Tables,name='Tables'),
    path('form/',views.form,name='form'),
]
