from django.contrib import admin
from django.urls import path,include
from predict import views

urlpatterns = [
    path('', views.index,name='Home'),
    path('predict', views.predict,name='predict'),

]